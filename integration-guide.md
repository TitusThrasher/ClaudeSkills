# Integration Guide: Complete Monitoring Workflows

**Template Version** - Workflows for combining search and documentation capabilities

---

## Overview

This guide demonstrates complete workflows that integrate searching, extracting, verifying, and documenting ICE/CBP enforcement activity. These workflows apply to any location once you've customized the skill for your area.

---

## Workflow 1: Daily 15-Minute Monitoring Routine

**Time Required:** 15 minutes  
**Frequency:** Every morning (and optionally evening)  
**Skill Level:** Beginner

### Steps

**1. Initiate Search (3 minutes)**

Prompt Claude:
```
"Run daily ICE monitoring for [CITY_NAME] - last 24 hours"
```

Claude will:
- Run core search queries
- Check priority news sources
- Review rapid response networks
- Prioritize findings

**2. Review Results (2 minutes)**

Claude presents findings:
```
High Priority (needs immediate documentation):
- [Source 1]: [Brief description]
- [Source 2]: [Brief description]

Medium Priority (review today):
- [Source 3]: [Brief description]

No activity detected: [Sources checked with no results]
```

**3. Extract High-Priority Items (5 minutes)**

For each high-priority finding:
```
"Extract data from [source description from results]"
```

Claude will:
- Pull structured data
- Format for database entry
- Run quality checks
- Flag any ambiguities

**4. Quick Verification (3 minutes)**

If needed:
```
"Cross-check this finding with other sources"
```

Claude searches for corroboration and reports back.

**5. Document (2 minutes)**

Copy extracted data to your database/spreadsheet.

### Example Session

```
You: "Run daily ICE monitoring for Austin - last 24 hours"

Claude: "Searching... Found 1 high-priority item:
- [Local RRT] posted Instagram alert 2 hours ago about activity at 
  [Location]. Contains specific details including detention count.

Medium priority:
- [Local News] general article about statewide operations (no Austin-specific details)

No activity found in other sources checked."

You: "Extract data from the Instagram alert"

Claude: [Provides complete structured data entry]

You: "Can you verify this with news sources?"

Claude: "Searching news... No news coverage yet (common for rapid 
response alerts). Instagram post is from verified community organization 
with track record of accurate reporting. Recommend: Document now, 
monitor for news confirmation."

You: [Copies data to database]
```

**Time Breakdown:**
- Search: 3 min
- Review: 2 min  
- Extract: 5 min
- Verify: 3 min
- Document: 2 min
**Total: 15 minutes**

---

## Workflow 2: Weekly Deep Dive (60 Minutes)

**Time Required:** 60 minutes  
**Frequency:** Once per week (Sunday recommended)  
**Skill Level:** Intermediate

### Steps

**1. Comprehensive Search (20 minutes)**

Prompt Claude:
```
"Conduct weekly deep dive search for [CITY_NAME] covering [start date] to [end date]"
```

Claude will:
- Search all major news outlets
- Check all community organizations
- Review social media systematically
- Search court filings (PACER)
- Identify patterns

**2. Prioritize Findings (5 minutes)**

Claude organizes findings:
```
Week of [dates]: Found [X] items requiring documentation

Category breakdown:
- New incidents: [X]
- Updates to existing incidents: [X]
- Pattern observations: [X]
- Background/context pieces: [X]
```

**3. Systematic Extraction (25 minutes)**

For each new incident:
```
"Extract data from item #[X]"
```

Work through list systematically.

**4. Pattern Analysis (10 minutes)**

```
"Analyze patterns in this week's incidents"
```

Claude identifies:
- Geographic patterns
- Temporal patterns (times, days)
- Tactical patterns
- Agency activity levels
- Emerging trends

**5. Quality Audit (5 minutes)**

```
"Review this week's entries for quality and consistency"
```

Claude checks:
- Data completeness
- Consistency with previous entries
- Potential duplicates
- Format compliance

### Example Session

```
You: "Conduct weekly deep dive for Austin covering October 20-26, 2025"

Claude: "Comprehensive search complete. Findings:

NEW INCIDENTS (4):
1. Oct 22 - [Neighborhood] - RRT alert, 2 detained
2. Oct 24 - [Location] - News article, workplace raid, 7 detained
3. Oct 25 - [Location] - RRT alert, federal agents, count unknown
4. Oct 26 - [Location] - Court filing references detention

UPDATES TO EXISTING (1):
5. Oct 21 incident - News follow-up with additional details

PATTERNS OBSERVED:
- 3 of 4 incidents in [Geographic cluster]
- All occurred 6-9am timeframe
- Increase in workplace focus

CONTEXT PIECES (2):
- State policy analysis (no specific incidents)
- Community impact feature (references multiple dates)

Ready to extract. Start with #1?"

You: "Yes, extract #1"

[Continue through all 4 incidents]

You: "Show me the pattern analysis in detail"

Claude: [Provides detailed breakdown with maps, timelines, observations]

You: "Audit the entries for quality"

Claude: "Quality review complete. All entries meet standards. 
Suggested improvements:
- Entry #2: Add zip code (currently blank)
- Entry #3: Cross-reference with news sources
- Minor: Standardize vehicle description format in #1"
```

---

## Workflow 3: Breaking Incident Response

**Time Required:** 5-30 minutes (depending on incident complexity)  
**Frequency:** As needed  
**Skill Level:** Intermediate to Advanced

### Steps

**1. Initial Alert (1 minute)**

When you see/hear about potential ICE activity:

```
"I'm seeing reports of possible ICE activity at [location]. 
Help me verify and document."
```

**2. Rapid Verification (3-5 minutes)**

Claude immediately:
- Searches social media (Twitter, Instagram)
- Checks rapid response networks
- Searches local news breaking alerts
- Provides initial assessment

**3. Ongoing Monitoring (during incident)**

```
"Monitor for updates on [location] incident"
```

Claude continues searching and reports new information as it emerges.

**4. Initial Documentation (5 minutes)**

Once enough information is available:
```
"Create preliminary entry for [location] incident"
```

Claude creates entry marked as "preliminary/in progress."

**5. Updates and Finalization (10-15 minutes)**

As incident concludes and more information becomes available:
```
"Update [location] entry with new information"
```

Claude refines entry with final details.

### Example Session

```
[2:15 PM]
You: "I'm seeing tweets about ICE activity at [Address]. Can you verify?"

Claude: "Searching real-time sources...

CONFIRMED by [Rapid Response Network] (posted 2:12 PM):
- Federal agents at [Address]
- Multiple vehicles
- Activity ongoing

Also found:
- 3 witness tweets (unverified)
- No news coverage yet (expected lag)

Assessment: Likely confirmed incident. Recommend monitoring."

[2:20 PM]
You: "Create preliminary entry"

Claude: [Provides preliminary entry marked IN PROGRESS]

[2:45 PM]
You: "Any updates on [Address] incident?"

Claude: "Yes! New information:
- [RRT] update: At least 2 detained
- Vehicle descriptions added
- Incident concluded around 2:30 PM
- No news coverage yet"

[3:00 PM]
You: "Update the entry with final information"

Claude: [Provides complete, finalized entry]

You: "Monitor for news coverage over next 24 hours"

Claude: "Will do. Suggest checking back this evening and tomorrow morning."
```

---

## Workflow 4: Historical Backfill

**Time Required:** Variable (2-4 hours for 1 month of history)  
**Frequency:** One-time or as needed  
**Skill Level:** Advanced

### Purpose

Document incidents that occurred before you started systematic monitoring.

### Steps

**1. Define Scope (5 minutes)**

```
"Help me backfill ICE activity for [CITY] from [start date] to [end date]"
```

Claude helps you:
- Set realistic time frame
- Identify key sources for period
- Establish documentation standards

**2. Systematic Historical Search (variable)**

By time period (week by week or month by month):
```
"Search for ICE activity in [CITY] during [specific week/month]"
```

Claude searches:
- News archives
- Court filings from that period
- Social media (if still accessible)
- Organization reports/archives

**3. Extract Historical Incidents (variable)**

For each finding:
```
"Extract data from [historical source]"
```

Note: Historical sources may have less detail. Claude adapts.

**4. Historical Context Notes (10-15 minutes per time period)**

```
"Provide context for [time period]"
```

Claude helps document:
- What was happening at the time
- Why documentation may be limited
- Source availability issues
- Patterns observed

### Example Session

```
You: "I want to backfill Austin ICE activity from March 2025 through June 2025"

Claude: "That's 4 months. Recommended approach:
1. Start with March (likely most source availability)
2. Work chronologically
3. Focus on verified sources (news, court records)
4. Note: Social media may be limited/deleted

Expected time: 6-8 hours total
Suggestion: Break into weekly sessions

Ready to start with March?"

You: "Yes, start with March 1-31, 2025"

Claude: "Searching March 2025 sources...

Found in news archives:
1. March 7 - [Local News] workplace raid, [Location], 12 detained
2. March 15 - [Local News] courthouse arrests, 3 detained
3. March 23 - [Community Org] report on increased activity

Found in PACER:
4. March 18 filing - detention challenge, [Location]

Social media: Limited (many posts deleted/unavailable)

Recommend: Start with news articles #1 and #2 (most detail), 
then court filing #4, then community report #3.

Extract #1?"

[Continue systematically through time period]
```

---

## Workflow 5: Multi-Source Incident Resolution

**Use Case:** When the same incident is reported differently across sources  
**Skill Level:** Advanced

### Steps

**1. Identify Discrepancy**

```
"I have multiple sources reporting on [date/location] but with 
different details. Help me resolve."
```

**2. Compile All Sources**

Provide Claude with all versions:
```
Source 1 says: [details]
Source 2 says: [details]
Source 3 says: [details]
```

**3. Systematic Comparison**

```
"Compare these sources and identify differences"
```

Claude analyzes:
- What all sources agree on
- Where sources conflict
- Which details are unique to each source
- Source credibility assessment

**4. Resolution Strategy**

```
"How should I document this incident given the discrepancies?"
```

Claude recommends:
- Which details to include
- How to note conflicts
- Which sources to prioritize
- What to leave ambiguous

**5. Final Documentation**

```
"Create final entry incorporating your recommendations"
```

### Example Session

```
You: "Three sources report on October 15 incident at [Location] 
but with different detention counts. Help resolve.

Instagram RRT (8am): '2 people detained'
Local News (2pm): '3 people taken into custody'
Community Org (4pm): 'between 2-4 detained'"

Claude: "Analyzing...

AGREEMENT across all sources:
- Date: October 15
- Location: [Location]
- Agency: ICE (confirmed by news)
- Time frame: Morning hours
- Federal agents present

DISCREPANCIES:
- Detention count: 2 vs 3 vs 2-4

ANALYSIS:
- RRT (8am) = earliest report, may be incomplete
- News (2pm) = most specific (3), cites ICE spokesperson
- Org (4pm) = acknowledges uncertainty with range

RECOMMENDATION:
Use 3 as primary count (most authoritative source).
Note discrepancy in Description field.

REASONING:
- News article has official confirmation
- Posted after incident concluded
- RRT may have been preliminary count
- Org acknowledges uncertainty with range

Shall I create the entry with these specifications?"

You: "Yes"

Claude: [Provides entry with]:
- Individuals Detained: 3
- Description: "...3 people taken into custody according to 
  [Local News] citing ICE spokesperson. Note: Earlier reports 
  from [RRT] stated 2 detained (preliminary count), and [Org] 
  reported 2-4 detained (acknowledging uncertainty). Multiple 
  sources confirm incident details."
- News Coverage: [all URLs]
- RRT Report: [Instagram URL]
```

---

## Workflow 6: Pattern Investigation

**Use Case:** When you notice a pattern and want to investigate  
**Skill Level:** Intermediate to Advanced

### Steps

**1. Identify Pattern**

```
"I've noticed [pattern description]. Can you help me investigate?"
```

Example patterns:
- Same location multiple times
- Particular time of day
- Specific neighborhoods
- Escalation in tactics

**2. Historical Search**

```
"Search for all ICE incidents at [location] in past [time period]"
```

or

```
"Search for all incidents involving [pattern element]"
```

**3. Analysis**

```
"Analyze this pattern - what does it tell us?"
```

Claude examines:
- Frequency
- Geographic distribution
- Temporal distribution
- Tactical elements
- Context/background

**4. Documentation**

```
"Create a pattern summary report"
```

Claude generates:
- Timeline of incidents
- Map data (addresses/coordinates)
- Common elements
- Notable variations
- Implications

### Example Session

```
You: "I've noticed several incidents near [Transit Station]. 
Is this a pattern?"

Claude: "Searching historical incidents near [Transit Station]...

Found 4 incidents within 2 blocks of [Transit Station]:
1. Oct 8 - [Street A]
2. Oct 15 - [Street B]
3. Oct 22 - [Street C]
4. Oct 29 - [Street A] (repeat location)

PATTERN ANALYSIS:

Geographic:
- All within 2-block radius
- Streets A and B have direct transit access
- [Station] is major hub for [demographic] community

Temporal:
- All on Fridays
- All 7-9am timeframe
- Weekly frequency (every Friday)

Tactical:
- All involve vehicle surveillance
- Similar vehicle descriptions (possibly same vehicles)
- 2-3 people detained per incident
- No use of force reported

Context:
- [Transit Station] serves [neighborhoods]
- Morning rush hour timing
- Possible commute surveillance pattern

Implications:
- Suggests systematic targeting of transit location
- Predictable timing (Fridays, morning)
- Community alert opportunity: Fridays 7-9am near [Station]

Recommend:
1. Alert community organizations
2. Share pattern with [RRT]
3. Monitor other major transit stations
4. Document defensive: suggest avoiding transit Fri mornings

Create formal pattern report?"

You: "Yes, create the report"

Claude: [Generates comprehensive pattern report with all data]
```

---

## Workflow 7: Database Quality Audit

**Time Required:** 30-60 minutes  
**Frequency:** Monthly  
**Skill Level:** Intermediate

### Purpose

Ensure database integrity, consistency, and completeness.

### Steps

**1. Run Audit**

```
"Audit my ICE documentation database for quality issues"
```

**2. Review Findings**

Claude checks for:
- Missing data fields
- Format inconsistencies
- Potential duplicates
- Incomplete entries
- Out-of-date information
- Verification status

**3. Prioritize Fixes**

```
"Prioritize these issues by importance"
```

Claude ranks:
- Critical (affects data usability)
- Important (incomplete documentation)
- Minor (format inconsistencies)
- Optional (enhancements)

**4. Systematic Corrections**

Work through priority issues:
```
"Help me fix issue #[X]"
```

Claude provides:
- What's wrong
- How to fix it
- What information is needed
- Where to find it

### Example Session

```
You: "Audit my database (37 entries from Oct 1-31)"

Claude: "Database audit complete. Quality: Good overall, some issues found.

CRITICAL (fix immediately):
- Entry #14: No date (shows 'TBD')
- Entry #22: Location too vague ('Downtown')

IMPORTANT (fix soon):
- 5 entries missing Zip Code
- Entry #9: News coverage URL is broken
- Entry #17: Should cross-reference with #18 (same incident)

MINOR (fix when convenient):
- 3 entries: Inconsistent neighborhood spelling
- Entry #25: Description could be more specific

OPTIONAL ENHANCEMENTS:
- 8 entries could add vehicle details from sources
- Consider adding 'Use of Force' details to Entry #31

Recommendations:
1. Fix Critical issues today (2 items)
2. Fix Important issues this week (7 items)
3. Minor fixes in next audit cycle
4. Optional as time permits

Start with Entry #14 (missing date)?"

You: "Yes, let's fix #14"

Claude: "Entry #14 issue: Date shows 'TBD'

Looking at entry content:
- Source: [RRT Instagram]
- URL: [URL]
- Description mentions 'early October'

I can search for:
1. The actual Instagram post date
2. News coverage that might specify date
3. Other entries around same time for context

What would you like me to do?"

You: "Search for the Instagram post date"

Claude: [Retrieves post, determines date, provides correction]
```

---

## Integration Tips

### Combine Workflows

**Example combination:**
- Daily monitoring (Workflow 1) on weekdays
- Weekly deep dive (Workflow 2) on Sundays
- Monthly quality audit (Workflow 7) first Sunday of month
- Pattern investigation (Workflow 6) as needed

### Customize Prompts

**Develop your own shorthand:**
```
Instead of: "Run daily ICE monitoring for Austin - last 24 hours"
You could use: "Daily Austin check"
```

Claude adapts to your style.

### Save Effective Patterns

Document prompts that work well:
```
My most effective prompts:
1. Daily: "[X prompt]"
2. Weekly: "[Y prompt]"
3. Verification: "[Z prompt]"
```

### Progressive Complexity

**Start simple:**
- Week 1-2: Daily monitoring only
- Week 3-4: Add weekly deep dives
- Month 2: Add pattern analysis
- Month 3: Historical backfill

**Build skills gradually.**

---

## Troubleshooting Workflows

### "Too Time-Consuming"

**Solutions:**
- Reduce frequency (every other day instead of daily)
- Focus on high-priority sources only
- Use automation where possible
- Share workload with others

### "Missing Context"

**Solutions:**
- Read reference files: `search-strategies.md`, `examples.md`
- Build local knowledge over time
- Connect with community organizations
- Attend rapid response trainings

### "Inconsistent Results"

**Solutions:**
- Standardize your prompts
- Use quality checklist every time
- Document your own best practices
- Regular quality audits

---

## Advanced Integration: With Other Tools

### Integration with Spreadsheets

```
1. Claude extracts data
2. You copy to Google Sheets/Excel
3. Use spreadsheet for:
   - Mapping (address column)
   - Timeline visualization
   - Pattern analysis
   - Sharing with partners
```

### Integration with Community Tools

```
1. Document with Claude
2. Share with:
   - Rapid response networks
   - Legal aid organizations  
   - Advocacy groups
   - Researchers/journalists
```

### Integration with Legal Work

```
1. Claude documents incidents
2. Legal team uses for:
   - Pattern evidence
   - Individual case support
   - Policy advocacy
   - Know Your Rights materials
```

---

## Workflow Templates

### Create Your Own Workflows

**Template:**
```
Workflow Name: [Name]
Purpose: [What it accomplishes]
Time Required: [Duration]
Frequency: [How often]
Skill Level: [Beginner/Intermediate/Advanced]

Steps:
1. [Step with prompt example]
2. [Step with prompt example]
3. [etc.]

Expected Output: [What you'll have at the end]
```

**Save and refine based on your experience.**

---

## Conclusion

These workflows demonstrate how to combine Claude's search and documentation capabilities into complete, efficient processes. Adapt them to your needs, your schedule, and your community's context.

**Remember:**
- Start simple, add complexity as needed
- Document what works for you
- Share effective workflows with others
- Iterate and improve over time

**Questions or need a custom workflow?** Consider the patterns in these examples and adapt to your specific needs.
