#!/usr/bin/env python3
"""
ICE/CBP Documentation Helper
Template Version - Customize for your location

This script provides automated helpers for processing ICE/CBP activity reports.
Useful for batch processing images, text extraction, and CSV generation.

Requirements:
    pip install pillow pytesseract requests
    
Note: Install tesseract-ocr system package for OCR functionality
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# ===== CUSTOMIZATION SECTION =====
# Update these values for your location

DEFAULT_CITY = "[CITY_NAME]"
DEFAULT_STATE = "[STATE_NAME]"
DEFAULT_STATE_ABBR = "[STATE_ABBR]"  # e.g., "TX"

# Your local sources for automatic attribution
LOCAL_SOURCES = {
    "rrt1": "[LOCAL_RAPID_RESPONSE_1]",
    "rrt2": "[LOCAL_RAPID_RESPONSE_2]",
    "news1": "[LOCAL_NEWS_1]",
    "news2": "[LOCAL_NEWS_2]",
}

# Common local neighborhoods and their ZIP codes
NEIGHBORHOOD_ZIPS = {
    "[NEIGHBORHOOD_1]": "[ZIP_1]",
    "[NEIGHBORHOOD_2]": "[ZIP_2]",
    "[NEIGHBORHOOD_3]": "[ZIP_3]",
    # Add more as needed
}

# ==================================


def extract_text_from_image(image_path: str) -> Optional[str]:
    """
    Extract text from an image using OCR.
    
    Args:
        image_path: Path to image file
        
    Returns:
        Extracted text or None if error
    """
    try:
        from PIL import Image
        import pytesseract
        
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except ImportError:
        print("Error: PIL and/or pytesseract not installed.")
        print("Install with: pip install pillow pytesseract")
        return None
    except Exception as e:
        print(f"Error extracting text from {image_path}: {e}")
        return None


def parse_alert_text(text: str) -> Dict:
    """
    Parse common alert patterns from text.
    Customize patterns based on your local sources.
    
    Args:
        text: Alert text to parse
        
    Returns:
        Dictionary with extracted fields
    """
    data = {
        "location": None,
        "date": None,
        "detained_count": None,
        "vehicles": [],
        "agency": None,
        "raw_text": text
    }
    
    lines = text.split('\n')
    
    # Look for date patterns
    # Common: "10/13 - 11AM" or "October 13 - 11:00 AM"
    for line in lines:
        if '-' in line and any(char.isdigit() for char in line):
            # Basic date extraction - customize for your format
            date_parts = line.split('-')[0].strip()
            # Add current year if not present
            if '/' in date_parts and len(date_parts.split('/')) == 2:
                month, day = date_parts.split('/')
                data["date"] = f"{month}/{day}/{datetime.now().year}"
    
    # Look for detention counts
    # Common: "at least X people detained" or "X detenidas"
    for line in lines.lower():
        if 'detained' in line or 'detenidas' in line or 'detenidos' in line:
            # Extract numbers
            import re
            numbers = re.findall(r'\b\d+\b', line)
            if numbers:
                data["detained_count"] = int(numbers[0])
    
    # Look for vehicle descriptions
    # Common: "Black Jeep Cherokee" or "White Ford Expedition"
    vehicle_keywords = ['jeep', 'ford', 'gmc', 'dodge', 'chevrolet', 'toyota']
    for line in lines:
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in vehicle_keywords):
            data["vehicles"].append(line.strip())
    
    # Look for agency confirmation
    for line in lines.lower():
        if 'ice' in line and ('confirmed' in line or 'identified' in line):
            data["agency"] = "ICE"
        elif 'cbp' in line or 'border patrol' in line:
            data["agency"] = "CBP"
    
    return data


def format_for_database(data: Dict, source_url: str = None) -> str:
    """
    Format extracted data into database entry format.
    
    Args:
        data: Parsed data dictionary
        source_url: URL of the source
        
    Returns:
        Formatted string ready for database
    """
    output = []
    
    output.append(f"Location: {data.get('location', '[Needs manual entry]')}")
    output.append(f"Agencies Involved: {data.get('agency', '[Leave blank]')}")
    output.append(f"Date: {data.get('date', '[Needs manual entry]')}")
    
    # Build description
    desc_parts = []
    if source_url:
        desc_parts.append(f"Source: {source_url}")
    if data.get('detained_count'):
        desc_parts.append(f"{data['detained_count']} people detained")
    if data.get('vehicles'):
        desc_parts.append(f"Vehicles: {', '.join(data['vehicles'])}")
    
    description = ". ".join(desc_parts) if desc_parts else "[Needs manual entry]"
    output.append(f"Description: {description}")
    
    output.append(f"Individuals Detained: {data.get('detained_count', '[Blank]')}")
    output.append(f"Map Address: [Needs manual entry - full address with {DEFAULT_CITY}, {DEFAULT_STATE_ABBR}]")
    output.append(f"Use of Force: [Blank unless specified]")
    output.append(f"Neighborhood: [Needs manual entry]")
    output.append(f"News Coverage: [Blank or URLs separated by |]")
    output.append(f"Rapid Response Network Report: {source_url or '[Blank]'}")
    output.append(f"Zip Code: [Needs manual entry]")
    
    return "\n".join(output)


def process_image(image_path: str, source_url: str = None):
    """
    Process a single image: extract text, parse, format.
    
    Args:
        image_path: Path to image file
        source_url: Optional URL of the source
    """
    print(f"\nProcessing: {image_path}")
    print("=" * 60)
    
    # Extract text
    print("Extracting text...")
    text = extract_text_from_image(image_path)
    
    if not text:
        print("Failed to extract text. Please process manually.")
        return
    
    print("\nExtracted Text:")
    print("-" * 60)
    print(text)
    print("-" * 60)
    
    # Parse
    print("\nParsing data...")
    data = parse_alert_text(text)
    
    # Format
    print("\nFormatted for database:")
    print("=" * 60)
    formatted = format_for_database(data, source_url)
    print(formatted)
    print("=" * 60)
    
    # Optionally save to file
    output_file = Path(image_path).stem + "_extracted.txt"
    with open(output_file, 'w') as f:
        f.write("RAW TEXT:\n")
        f.write(text)
        f.write("\n\n")
        f.write("FORMATTED OUTPUT:\n")
        f.write(formatted)
    
    print(f"\nSaved to: {output_file}")


def process_folder(folder_path: str):
    """
    Process all images in a folder.
    
    Args:
        folder_path: Path to folder containing images
    """
    folder = Path(folder_path)
    
    if not folder.is_dir():
        print(f"Error: {folder_path} is not a directory")
        return
    
    # Find all image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(folder.glob(f"*{ext}"))
        image_files.extend(folder.glob(f"*{ext.upper()}"))
    
    if not image_files:
        print(f"No image files found in {folder_path}")
        return
    
    print(f"Found {len(image_files)} image(s) to process")
    
    for image_file in sorted(image_files):
        process_image(str(image_file))
        print("\n" + "="*80 + "\n")


def export_to_csv(data_list: List[Dict], output_file: str):
    """
    Export multiple entries to CSV format.
    
    Args:
        data_list: List of data dictionaries
        output_file: Path to output CSV file
    """
    import csv
    
    fieldnames = [
        "Location",
        "Agencies Involved",
        "Date",
        "Description",
        "Individuals Detained",
        "Map Address",
        "Use of Force",
        "Neighborhood",
        "News Coverage",
        "Rapid Response Network Report",
        "Zip Code"
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)
    
    print(f"Exported to {output_file}")


def interactive_mode():
    """
    Interactive mode for manual data entry.
    """
    print("\n" + "="*60)
    print("ICE/CBP Documentation Helper - Interactive Mode")
    print("="*60)
    
    data = {}
    
    print("\nEnter data (press Enter to skip optional fields):")
    
    data["Location"] = input("Location (street intersection or address): ").strip()
    data["Agencies Involved"] = input("Agencies Involved (ICE, CBP, or blank): ").strip()
    data["Date"] = input("Date (MM/DD/YYYY): ").strip()
    data["Description"] = input("Description: ").strip()
    data["Individuals Detained"] = input("Individuals Detained (number or blank): ").strip()
    data["Map Address"] = input(f"Map Address (full address with {DEFAULT_CITY}, {DEFAULT_STATE_ABBR}): ").strip()
    data["Use of Force"] = input("Use of Force (types or blank): ").strip()
    data["Neighborhood"] = input("Neighborhood: ").strip()
    data["News Coverage"] = input("News Coverage (URLs separated by |): ").strip()
    data["Rapid Response Network Report"] = input("Rapid Response Network Report (URL): ").strip()
    data["Zip Code"] = input("Zip Code: ").strip()
    
    print("\n" + "="*60)
    print("FORMATTED OUTPUT:")
    print("="*60)
    
    for key, value in data.items():
        print(f"{key}: {value}")
    
    print("="*60)
    
    # Ask to save
    save = input("\nSave to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Filename (default: entry.txt): ").strip() or "entry.txt"
        with open(filename, 'w') as f:
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
        print(f"Saved to {filename}")


def main():
    """
    Main entry point for the script.
    """
    parser = argparse.ArgumentParser(
        description=f"ICE/CBP Documentation Helper for {DEFAULT_CITY}, {DEFAULT_STATE}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process a single image
  python ice_documentation_helper.py --extract-image alert.jpg
  
  # Process all images in a folder
  python ice_documentation_helper.py --process-folder images/
  
  # Interactive data entry
  python ice_documentation_helper.py --interactive
  
  # With source URL
  python ice_documentation_helper.py --extract-image alert.jpg --url "https://instagram.com/p/..."
        """
    )
    
    parser.add_argument(
        '--extract-image',
        metavar='FILE',
        help='Extract text and parse data from an image'
    )
    
    parser.add_argument(
        '--process-folder',
        metavar='FOLDER',
        help='Process all images in a folder'
    )
    
    parser.add_argument(
        '--url',
        metavar='URL',
        help='Source URL to include in output'
    )
    
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Interactive data entry mode'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='ICE/CBP Documentation Helper - Template v1.0'
    )
    
    args = parser.parse_args()
    
    # No arguments - show help
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    # Process commands
    if args.extract_image:
        process_image(args.extract_image, args.url)
    
    elif args.process_folder:
        process_folder(args.process_folder)
    
    elif args.interactive:
        interactive_mode()


if __name__ == '__main__':
    main()
