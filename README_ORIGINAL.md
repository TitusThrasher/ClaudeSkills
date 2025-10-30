# ICE/CBP [CITY_NAME] Activity Monitoring & Documentation Skill

**Version:** Template 1.0  
**Last Updated:** [DATE]

---

## ⚠️ CUSTOMIZATION REQUIRED

**This is a template!** Before using, you must customize it for your location.

**See `CUSTOMIZATION_GUIDE.md` for detailed instructions.**

Quick checklist:
- [ ] Replace all `[PLACEHOLDERS]` with your local information
- [ ] Update news sources
- [ ] Add local organizations
- [ ] Customize search queries
- [ ] Test thoroughly

---

## Overview

This Claude Skill provides comprehensive capabilities for monitoring and documenting ICE and CBP enforcement activity in [CITY_NAME], [STATE_NAME] [IF_APPLICABLE: during [OPERATION_NAME] ([START_DATE] - present)].

## What This Skill Does

### 🔍 Search & Monitor
- Systematically searches news outlets, social media, legal sources, and community organizations
- Evaluates source quality and prioritizes findings
- Identifies patterns and tracks enforcement trends
- Conducts daily quick checks and weekly deep dives

### 📝 Extract & Document  
- Extracts structured data from social media alerts [IF_BILINGUAL: (bilingual [LANGUAGE_1]/[LANGUAGE_2])]
- Processes news articles for verified details
- Handles community notices and legal documents
- Creates complete database entries with 11 standardized fields

## Quick Start

### Installation

1. **Customize this template first!** See `CUSTOMIZATION_GUIDE.md`
2. Upload the customized skill folder to Claude (claude.ai or Claude Code)
3. The skill will be automatically available for use
4. Start with a daily monitoring prompt

### Basic Usage

**Daily Monitoring (15 minutes):**
```
Prompt: "Run daily ICE monitoring for [CITY_NAME] - last 24 hours"

Claude will:
1. Search key sources
2. Prioritize findings
3. Report what needs documentation
```

**Extract Data from Source:**
```
Prompt: "Extract incident data from [paste social media alert text or news URL]"

Claude will:
1. Identify source type
2. Extract structured data
3. Format for database entry
4. Run quality checks
```

**Weekly Deep Dive (60 minutes):**
```
Prompt: "Conduct weekly ICE monitoring deep dive for [date range]"

Claude will:
1. Search all major sources comprehensively
2. Extract all new incidents
3. Provide pattern analysis
4. Suggest database updates
```

## Data Structure

The skill documents 11 fields per incident:

| Field | Example |
|-------|---------|
| Location | "[Street 1] and [Street 2]" |
| Agencies Involved | "ICE" (or blank) |
| Date | "10/13/2025" |
| Description | "[Source] confirmed..." |
| Individuals Detained | "2" (or blank) |
| Map Address | "[Address], [CITY], [STATE] [ZIP]" |
| Use of Force | "Pepper spray" (or blank) |
| Neighborhood | "[NEIGHBORHOOD_NAME]" |
| News Coverage | "https://[localnews].../\|https://..." |
| Rapid Response Report | "https://[socialmedia].com/..." |
| Zip Code | "[ZIP_CODE]" |

## File Structure

```
ice-cbp-[city]-monitoring/
├── CUSTOMIZATION_GUIDE.md            # How to customize this template
├── SKILL.md                          # Main skill instructions (Claude reads this)
├── README.md                         # This file (user documentation)
├── reference/
│   ├── examples.md                   # Extraction examples
│   ├── search-strategies.md          # Comprehensive query library
│   └── integration-guide.md          # Advanced workflows
└── scripts/
    └── ice_documentation_helper.py   # Python automation tools
```

## Key Features

### Source Coverage
[CUSTOMIZE: Update with your sources]
- ✅ [LOCAL_NEWS_1], [LOCAL_NEWS_2], [LOCAL_NEWS_3]
- ✅ [Social media] rapid response networks [IF_BILINGUAL: (bilingual)]
- ✅ [Social platform] real-time monitoring
- ✅ PACER ([federal district] court filings)
- ✅ Community organization updates ([ORG_1], [ORG_2], [ORG_3])

### Data Quality
- ✅ Three-level verification system (Confirmed/Reported/Alleged)
- ✅ Duplicate detection
- ✅ Cross-source verification
- ✅ [IF_BILINGUAL: Bilingual content processing ([LANGUAGE_1]/[LANGUAGE_2])]
- ✅ Quality assurance checklist

### Efficiency
- ✅ Daily routine takes 15 minutes
- ✅ Weekly deep dive in 60 minutes
- ✅ Progressive disclosure - details loaded only when needed
- ✅ Python helpers for automation
- ✅ Systematic search query library

## Example Workflows

### Workflow 1: Processing Social Media Alert

**You:** "I have a new alert from [LOCAL_RAPID_RESPONSE]. The [post/image] shows: '[EXAMPLE_ALERT_TEXT]'"

**Claude with this skill:**
1. Identifies this as rapid response network alert
2. Extracts: Date, Location, Detained count (if mentioned), Vehicle descriptions
3. Formats complete database entry
4. Runs quality checks
5. Provides formatted output ready to add to database

### Workflow 2: Daily Monitoring

**You:** "Run daily monitoring"

**Claude with this skill:**
1. Searches 5 core news queries
2. Checks 3 priority news sites
3. Reviews latest social media
4. Prioritizes findings as High/Medium/Low
5. Reports: "Found X high-priority items requiring extraction"
6. You then say "Extract the first one"
7. Claude processes and provides structured data

### Workflow 3: Verifying Community Report

**You:** "Someone reported ICE activity at [NEIGHBORHOOD] this morning but I can't verify. How should I search?"

**Claude with this skill:**
1. Suggests specific search queries for [NEIGHBORHOOD]
2. Checks rapid response networks
3. Looks for recent news coverage
4. Searches [social platforms] with location filters
5. Advises on verification requirements
6. If found, extracts and documents

## Advanced Features

### Pattern Tracking
Claude can identify:
- Repeated staging locations
- Time-of-day patterns
- Neighborhood targeting trends
- Escalation in tactics
- New operational approaches

### Multi-Source Integration
Claude combines:
- Social media alerts (real-time community reports)
- News articles (verified details, official statements)
- Court filings (legal context, complaints)
- Community notices (pattern warnings)

### Quality Control
- Automatic duplicate detection
- Cross-source verification
- Conflict notation in descriptions
- Source quality assessment
- Verification level tracking

## Customization

### Search Frequency
- Daily: Morning + evening (recommended)
- 2-3x per week: Moderate monitoring
- Weekly only: Historical documentation

### Geographic Scope
[CUSTOMIZE based on your area]
Currently optimized for:
- Primary: [CITY_NAME] city limits
- Secondary: [SURROUNDING_AREAS]
- Context: [METRO_AREA/REGION]

### Source Priorities
Adjust which sources to prioritize based on:
- Your geographic focus
- Your verification requirements
- Your time availability

## Python Helper Tools

The included `ice_documentation_helper.py` script provides:
- OCR text extraction from images
- Automated pattern matching
- Batch processing capabilities
- CSV export formatting

**Usage:**
```bash
python scripts/ice_documentation_helper.py --extract-image alert.jpg
python scripts/ice_documentation_helper.py --process-folder images/
```

## Support Resources

### Key Organizations
[CUSTOMIZE: Add your local organizations]
- **[ORG_1]**: [website]
- **[ORG_2]**: [website]
- **[ORG_3]**: [website]

### Hotline
[CUSTOMIZE: Add your local/state hotline]
- **[HOTLINE_NAME]**: [PHONE_NUMBER]

### Documentation
- See `CUSTOMIZATION_GUIDE.md` for setup instructions
- See `reference/examples.md` for detailed extraction examples
- See `reference/search-strategies.md` for complete query library
- See `reference/integration-guide.md` for advanced workflows

## Tips for Best Results

1. **Be specific in your prompts:**
   - ✅ Good: "Run daily monitoring for [CITY_NAME], [DATE]"
   - ❌ Vague: "Check for ICE stuff"

2. **Provide context when available:**
   - ✅ "This is an alert from [LOCAL_RAPID_RESPONSE]"
   - ❌ Just pasting text without context

3. **Use the quality checklist:**
   - Ask Claude to run the checklist before finalizing entries

4. **Leverage progressive disclosure:**
   - Ask for specific reference files when you need detailed guidance
   - "Show me examples of extracting from news articles"

5. **Build on patterns:**
   - "Are there any patterns in the past week's incidents?"
   - "What neighborhoods have the most activity?"

## Maintenance & Updates

This skill should be updated:

- Add new source URLs as they emerge
- Update search queries based on evolving terminology
- Adjust geographic scope
- Add new rapid response networks
- Refine data schema as needed

## Contact & Credits

**Template Created By:** Andrew Thrasher  
**Original Organization:** Titus Legal Design  
**Template Website:** tituslegaldesign.com  
**Template LinkedIn:** linkedin.com/in/andrewmthrasher

**Customized For:** [YOUR_CUSTOMIZATION_INFO]  
**Customized By:** [YOUR_NAME/ORG]  
**Date Customized:** [DATE]

## Version

**Template Version:** 1.0  
**Template Release Date:** October 2025  
**Your Customization Date:** [DATE]  
**Compatible with:** Claude Sonnet 4.5, Opus 4, Haiku (with reduced complexity)

## License & Usage

[CUSTOMIZE: Add your licensing terms]

This skill template is provided for documentation purposes related to immigration enforcement accountability. Use responsibly and in accordance with ethical documentation practices.

**Suggested License:** Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)
- Allows adaptation and sharing
- Requires attribution to original creator
- Derivative works must use same license

---

## Before First Use

**📋 Customization Checklist:**
- [ ] Read `CUSTOMIZATION_GUIDE.md` thoroughly
- [ ] Replace all `[PLACEHOLDERS]` in all files
- [ ] Update all local news sources
- [ ] Add all local organizations
- [ ] Customize search queries for your area
- [ ] Update neighborhood names and ZIP codes
- [ ] Test with "Run daily monitoring" prompt
- [ ] Verify Claude uses your local information
- [ ] Create your first real extraction

**⚠️ This template will not work correctly until customized!**

**Ready to customize?** Start with `CUSTOMIZATION_GUIDE.md`
