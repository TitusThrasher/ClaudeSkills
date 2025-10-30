---
name: ice-cbp-[CITY_NAME]-monitoring
description: Monitors and documents ICE and CBP enforcement activity in [CITY_NAME], [STATE_NAME] [IF_APPLICABLE: during [OPERATION_NAME]]. Systematically searches multiple sources (news, social media, legal, community) to find incidents, then extracts structured data from images, articles, and reports. Creates comprehensive database entries with verified locations, dates, detention counts, and use-of-force details. Use for daily monitoring, weekly deep dives, and maintaining accurate enforcement documentation.
---

# ICE/CBP [CITY_NAME] Activity Monitoring & Documentation

## Purpose

This skill provides complete capability for monitoring and documenting ICE and CBP enforcement activity in [CITY_NAME], [STATE_NAME] [IF_APPLICABLE: during [OPERATION_NAME] ([START_DATE] - present)]. It combines two essential functions:

1. **Search & Monitor** - Find new incidents across multiple sources
2. **Extract & Document** - Create structured database entries from sources

## Quick Start

### Daily 15-Minute Routine

**Morning Search:**
```
"Run daily ICE monitoring for [CITY_NAME] - last 24 hours"
```

**Extract & Document:**
```
"Extract data from [source] using documentation guidelines"
```

### Weekly Deep Dive
```
"Conduct weekly monitoring and extraction for [date range]"
```

## Core Workflow

```
SEARCH → EVALUATE → EXTRACT → VERIFY → DATABASE
```

1. **Search**: Query multiple sources for incidents
2. **Evaluate**: Prioritize findings by quality and relevance  
3. **Extract**: Pull structured data from sources
4. **Verify**: Cross-check details and check for duplicates
5. **Database**: Add completed entry with all 11 fields

## Data Schema

All documented incidents include these fields:

### Required Fields
1. **Location** - Street intersection or specific address
2. **Date** - MM/DD/YYYY format
3. **Description** - Detailed narrative of what occurred
4. **Map Address** - Full address with city, state, zip for mapping

### Optional/Conditional Fields
5. **Agencies Involved** - ICE, CBP, or blank if unconfirmed
6. **Individuals Detained** - Number detained (0 if none, blank if unknown)
7. **Use of Force** - Types used (tear gas, pepper spray, flash grenades, etc.)
8. **Neighborhood** - [CITY_NAME] neighborhood or suburb name
9. **News Coverage** - URLs to news articles (pipe-separated if multiple)
10. **Rapid Response Network Report** - URLs to social media posts
11. **Zip Code** - 5-digit ZIP code

## Part 1: Search & Monitoring

### Daily Search Queries (Must-Run)

**General searches (last 24 hours):**
- `ICE [CITY_NAME] arrest today`
- `immigration enforcement [CITY_NAME] [current date]`
[IF_APPLICABLE: - `[OPERATION_NAME] [CITY_NAME]`]
- `CBP [CITY_NAME]`

**Site-specific searches:**
- `site:[LOCAL_NEWS_SITE_1] ICE`
- `site:[LOCAL_NEWS_SITE_2] immigration [CITY_NAME]`
- `site:[LOCAL_NEWS_SITE_3] ICE`

### Source Priority Levels

**High Priority** (process immediately):
- Published within 24 hours
- Contains specific locations (streets, neighborhoods)
- Mentions detention/arrest counts
- Includes witness accounts or video
- References rapid response networks

**Medium Priority** (review same day):
- General operation coverage
- Background/analysis pieces
- Community impact stories

**Lower Priority** (weekly review):
- Opinion pieces with factual info
- Event announcements
- Policy discussions

### Key Sources to Monitor

**News Outlets:**
[CUSTOMIZE: Add your local news sources here]
- [LOCAL_NEWS_OUTLET_1]
- [LOCAL_PAPER_1]
- [LOCAL_TV_STATION_1]
- [LOCAL_TV_STATION_2]
- [LOCAL_PUBLIC_RADIO]
- [COMMUNITY_NEWS_SITE]

**Rapid Response Networks:**
[CUSTOMIZE: Add your local rapid response networks here]
- [LOCAL_RAPID_RESPONSE_1] ([social media platform])
- [LOCAL_RAPID_RESPONSE_2] ([social media platform])
- [LOCAL_RAPID_RESPONSE_3] ([social media platform])

**Community Organizations:**
[CUSTOMIZE: Add your local immigrant rights organizations here]
- [LOCAL_ORG_1] ([website])
- [LOCAL_ORG_2] ([website])
- [LOCAL_ORG_3] ([website])

**Legal Sources:**
- PACER ([Federal District]) - search for ICE/CBP as defendants
- [COUNTY] Court records

### Weekly Deep Dive Searches

**Sunday comprehensive review:**
1. All major news outlets (site-specific)
2. Court filing searches (PACER)
3. Community organization updates
4. Video platforms (YouTube, TikTok)
5. Pattern analysis across sources

For complete search strategies and query library, see: `reference/search-strategies.md`

## Part 2: Documentation & Extraction

### Extracting from Social Media Alerts

Rapid response network alerts may be images, text posts, or videos. Common formats include infographic-style images (sometimes bilingual).

**Key Elements to Extract:**

**Date/Time patterns:**
- "10/13 - 11AM" or "10/2 - 2PM-3PM"
- Convert to MM/DD/YYYY format

**Location patterns:**
- Street intersections: "[Street 1] and [Street 2]"
- Specific addresses: "[Number] [Street Name]"
- General areas: "Near [Landmark]"
- Create separate entries for multiple locations in one alert

**Detention info:**
- "At least X people were detained" → use X
- "Multiple" or "Several" without number → leave blank

**Vehicle details (always include):**
- Make, model, color, license plate
- Example: "Black Jeep Cherokee", "White Dodge Durango"

**Agency confirmation:**
- Only fill if explicitly stated: "confirmed federal agents", "ICE", "CBP"
- Otherwise leave blank and note "federal agents" in description

[IF_APPLICABLE: Common terms in [PRIMARY_LANGUAGE]:
- [TERM_1] = [ENGLISH_TRANSLATION]
- [TERM_2] = [ENGLISH_TRANSLATION]
- [TERM_3] = [ENGLISH_TRANSLATION]
- [TERM_4] = [ENGLISH_TRANSLATION]]

### Extracting from News Articles

**Priority information:**
- Verified details from reporters
- Official statements (ICE, CBP, city officials)
- Use of force descriptions
- Legal status of detentions
- Context about operations
- Human impact stories

**Citation format:**
Multiple sources separated by " | "
```
https://[localnews1].com/article | https://[localnews2].com/article
```

### Quality Standards & Verification

**Verification Levels:**
1. **Confirmed** - Verified by rapid response network, news media, or official sources
2. **Reported** - Single source, awaiting confirmation  
3. **Alleged** - Unverified social media (generally do not include)

**Best Practices - DO:**
- Cross-reference multiple sources when available
- Note conflicts between sources in Description
- Include specific vehicle descriptions
- Document use of force with specifics
- Preserve information in all relevant languages
- Link to original posts (full URLs)
- Create separate entries for multiple locations
- Include temporal context ("starting as early as 6am")

**Best Practices - DON'T:**
- Include unverified rumors
- Assume detention numbers if not stated
- Guess at agencies - leave blank if unconfirmed
- Combine distinct incidents
- Add editorial commentary

**Handling Ambiguity:**

If detention count unclear:
- "At least X" → use X as minimum
- "Multiple" without number → leave blank
- Range given → use lower number or leave blank with note

If location unclear:
- Include general area in Location field
- Add specifics to Description

If agency unconfirmed:
- Leave "Agencies Involved" blank
- Note "federal agents" in Description

### Output Format

Provide extracted data in this order:

```
Location: [Street intersection or address]
Agencies Involved: [ICE, CBP, or blank]
Date: [MM/DD/YYYY]
Description: [Detailed narrative including source, detentions, vehicles, context]
Individuals Detained: [Number or blank]
Map Address: [Full address for mapping: Street, [CITY_NAME], [STATE], [ZIP]]
Use of Force: [Types used or blank]
Neighborhood: [Neighborhood name]
News Coverage: [URLs separated by |]
Rapid Response Network Report: [Social media URL]
Zip Code: [5-digit code]
```

## Quality Assurance Checklist

Before finalizing an entry, verify:
- [ ] Date is in MM/DD/YYYY format
- [ ] Location is specific as possible
- [ ] Description includes source attribution
- [ ] URLs are complete and working
- [ ] No duplicate entries for same incident
- [ ] Use of Force documented if applicable
- [ ] Vehicle information captured when available
- [ ] Neighborhood and zip code added when known
- [ ] Agency confirmed only if explicitly stated
- [ ] Detention count accurate or left blank if unknown

## Common Pitfalls to Avoid

1. Duplicate entries - check existing database first
2. Mixing incidents - keep separate events separate
3. Incomplete URLs - always use full social media URLs
4. Inconsistent date formats - always MM/DD/YYYY
5. Vague locations - be as specific as sources allow
6. Over-interpreting - stick to what sources state
7. Missing context - include operational details in Description
8. Ignoring multilingual content - critical details may be language-specific

## Progressive Disclosure Resources

For detailed guidance, Claude should read these files as needed:

**Complete extraction examples:**
`reference/examples.md` - Real-world examples showing extraction from various source types

**Advanced search strategies:**
`reference/search-strategies.md` - Comprehensive query library, neighborhood searches, pattern tracking

**Integration workflows:**
`reference/integration-guide.md` - Complete workflows combining search and documentation

**Python helper script:**
`scripts/ice_documentation_helper.py` - Automate data extraction from text/OCR

## When to Use This Skill

**Daily monitoring:**
- Morning and evening searches for new incidents
- Real-time monitoring during breaking events
- Verification of community reports

**Weekly deep dives:**
- Comprehensive source reviews
- Pattern analysis across time periods
- Database quality audits

**Historical backfill:**
- Documenting past incidents as sources emerge
- Cross-referencing and updating existing entries

**Emergency response:**
- Rapid verification during active incidents
- Coordinating multiple source types
- Real-time documentation for legal/advocacy use

## Contact Resources

[CUSTOMIZE: Add your local/state resources]

**Hotline:** [LOCAL_HOTLINE_NAME]: [PHONE_NUMBER]

**Key Organizations:**
- [LOCAL_ORG_1] ([LOCAL_ORG_1_NAME])
- [LOCAL_ORG_2] ([LOCAL_ORG_2_NAME])
- [LOCAL_ORG_3] ([LOCAL_ORG_3_NAME])
- [LOCAL_ORG_4] ([LOCAL_ORG_4_NAME])

---

*This skill combines systematic search methodology with structured data extraction to create comprehensive, verified documentation of immigration enforcement activity in [CITY_NAME], [STATE_NAME].*
