# Example Extractions: ICE/CBP Activity Documentation

**Note:** This template file contains generic examples. As you document real incidents in your area, consider replacing these with your own examples for better local context.

---

## Example 1: Social Media Alert - Multiple Locations

**Source Type:** Community rapid response network post  
**Platform:** [Instagram/Facebook/Twitter/Telegram]

**Posted Content:**
```
COMMUNITY ALERT | 10/13 - 11AM
[Organization Name] confirmed federal agents at [Street 1]/[Street 2].
Additional activity was confirmed on [Street 3]/[Street 4]. 
At least 2 people were detained at each location.
Agents were identified driving a Black Jeep Cherokee and a White Dodge Durango.
```

### Extracted Data (Entry 1):

```
Location: [Street 1] and [Street 2]
Agencies Involved: [leave blank - not specified as ICE or CBP]
Date: 10/13/2025
Description: [Organization Name] confirmed federal agents at [Street 1]/[Street 2]. Agents were identified driving a Black Jeep Cherokee and a White Dodge Durango. At least 2 people were detained.
Individuals Detained: 2
Map Address: [Street 1] & [Street 2], [City], [State] [ZIP]
Use of Force: [blank]
Neighborhood: [Neighborhood Name]
News Coverage: [blank]
Rapid Response Network Report: [Full URL to social media post]
Zip Code: [ZIP]
```

### Extracted Data (Entry 2):

```
Location: [Street 3] and [Street 4]
Agencies Involved: [leave blank - not specified]
Date: 10/13/2025
Description: [Organization Name] confirmed federal agents at [Street 3]/[Street 4]. Additional activity from [Street 1]/[Street 2] incident. At least 2 people were detained.
Individuals Detained: 2
Map Address: [Street 3] & [Street 4], [City], [State] [ZIP]
Use of Force: [blank]
Neighborhood: [Neighborhood Name]
News Coverage: [blank]
Rapid Response Network Report: [Full URL to social media post]
Zip Code: [ZIP]
```

**Key Lessons:**
- Multiple locations in one alert = separate database entries
- Vehicle descriptions always included in Description
- Agency field left blank when not explicitly confirmed
- Each location gets its own complete entry

---

## Example 2: Social Media Alert - Agency Confirmed

**Source Type:** Community rapid response network post  
**Platform:** [Instagram/Facebook/Twitter/Telegram]

**Posted Content:**
```
COMMUNITY ALERT | 10/2 - 2PM-3PM
[Organization Name] confirmed federal agents along [Street 5] and [Street 6].
The following vehicles were identified as ICE:
- White GMC Denali
- Black Ford Expedition - [STATE] [LICENSE_PLATE]
  **Vehicle has a [distinguishing feature] sticker
```

### Extracted Data:

```
Location: [Street 5] and [Street 6]
Agencies Involved: ICE
Date: 10/02/2025
Description: [Organization Name] confirmed federal agents along [Street 5] and [Street 6]. Vehicles identified as ICE: White GMC Denali and Black Ford Expedition ([State] plate [LICENSE_PLATE] with [distinguishing feature] sticker on back window).
Individuals Detained: [blank - not specified]
Map Address: [Street 5] & [Street 6], [City], [State] [ZIP]
Use of Force: [blank]
Neighborhood: [Neighborhood Name]
News Coverage: [blank]
Rapid Response Network Report: [Full URL]
Zip Code: [ZIP]
```

**Key Lessons:**
- ICE confirmation → fill in Agencies Involved
- License plates included when provided
- Distinguishing features documented
- No detention count mentioned → left blank

---

## Example 3: Bilingual Alert (Spanish/English)

**Source Type:** Community rapid response network post  
**Platform:** [Instagram/Facebook/Twitter/Telegram]

**Posted Content:**
```
ALERTA COMUNITARIA | 10/23 - 9AM
El Equipo de [Organization] confirmó la presencia de agentes federales 
en la intersección de [Street A]/[Street B].
Se identificó a los agentes conduciendo estos vehículos:
- Jeep Wagoneer gris
- GMC Denali negro
- GMC blanco
```

### Extracted Data:

```
Location: [Street A] and [Street B]
Agencies Involved: [leave blank - not specified]
Date: 10/23/2025
Description: [Organization Name] confirmed the presence of federal agents at the intersection of [Street A]/[Street B]. Agents were identified driving these vehicles: Gray Jeep Wagoneer, Black GMC Denali, and White GMC.
Individuals Detained: [blank - not specified]
Map Address: [Street A] & [Street B], [City], [State] [ZIP]
Use of Force: [blank]
Neighborhood: [Neighborhood Name]
News Coverage: [blank]
Rapid Response Network Report: [Full URL]
Zip Code: [ZIP]
```

**Key Lessons:**
- Translate content to English for Description
- Preserve meaning and details accurately
- "Agentes federales" = federal agents (not ICE unless specified)
- Document language of original source

**Common Translation Reference:**
- agentes federales = federal agents
- detenidas/detenidos = detained
- confirmó la presencia = confirmed the presence
- personas = people/persons
- alerta comunitaria = community alert
- vehículos = vehicles
- intersección = intersection

---

## Example 4: News Article with Multiple Details

**Source Type:** Local news article  
**URL:** https://[localnews].com/ice-activity-[neighborhood]-[date]

**Article Excerpt:**
```
Federal immigration agents detained at least five people during operations 
in [Neighborhood] on Tuesday morning, according to witnesses and community 
advocates.

The enforcement action began around 6:30 a.m. near [Landmark] on [Street Name], 
where ICE agents in unmarked vehicles stopped several individuals, according 
to [Witness Name], who witnessed the events.

"I saw at least three black SUVs and agents in tactical vests," [Witness] said.

[Local Organization] confirmed the activity and said their rapid response 
team was on site by 7:15 a.m.

An ICE spokesperson confirmed the operation but declined to provide details 
about the number of arrests or the targets of the enforcement action.
```

### Extracted Data:

```
Location: [Street Name] near [Landmark]
Agencies Involved: ICE
Date: [MM/DD/YYYY - from article date]
Description: Federal immigration agents detained at least 5 people during operations in [Neighborhood] beginning around 6:30 AM near [Landmark] on [Street Name], according to [Local News] and witnesses. ICE agents in unmarked vehicles (at least three black SUVs) and wearing tactical vests were observed. An ICE spokesperson confirmed the operation but declined to provide details. [Local Organization] rapid response team arrived on site by 7:15 AM.
Individuals Detained: 5
Map Address: [Street Name], [City], [State] [ZIP]
Use of Force: [blank - none mentioned]
Neighborhood: [Neighborhood]
News Coverage: https://[localnews].com/ice-activity-[neighborhood]-[date]
Rapid Response Network Report: [if mentioned in article]
Zip Code: [ZIP]
```

**Key Lessons:**
- News articles = high verification level
- Include start time when mentioned
- Document both witness accounts and official confirmation
- Quote counts when stated: "at least five"
- Multiple vehicle descriptions included
- ICE spokesperson confirmation → Agency field filled

---

## Example 5: News Article with Use of Force

**Source Type:** Local news article  
**URL:** https://[localnews].com/ice-operation-[date]

**Article Excerpt:**
```
Immigrant rights advocates say federal agents used pepper spray during 
an immigration enforcement operation in [Neighborhood] on Wednesday.

Video shared on social media shows what appears to be federal agents 
deploying chemical spray near [Street] and [Avenue] around 10 a.m.

At least three people were taken into custody, according to [Organization].

The incident prompted protests later that evening, with community members 
gathering at [Location].
```

### Extracted Data:

```
Location: [Street] and [Avenue]
Agencies Involved: [blank - only described as "federal agents"]
Date: [MM/DD/YYYY]
Description: Federal agents used pepper spray during an immigration enforcement operation in [Neighborhood] near [Street] and [Avenue] around 10 AM, according to [Local News] and immigrant rights advocates. Video shared on social media shows agents deploying chemical spray. At least 3 people were taken into custody according to [Organization]. The incident prompted community protests later that evening.
Individuals Detained: 3
Map Address: [Street] & [Avenue], [City], [State] [ZIP]
Use of Force: Pepper spray
Neighborhood: [Neighborhood]
News Coverage: https://[localnews].com/ice-operation-[date]
Rapid Response Network Report: [social media video URL if available]
Zip Code: [ZIP]
```

**Key Lessons:**
- Use of Force documented when reported
- Video evidence mentioned in Description
- Community response noted as context
- Agency not confirmed → left blank
- Multiple source types (news + social media) cited

---

## Example 6: Court Filing

**Source Type:** Federal court filing (PACER)  
**Case:** [Case Number], [District Court]

**Filing Type:** Emergency Motion for Release

**Relevant Content:**
```
Plaintiff [Name] was detained by ICE on [Date] at approximately 
[Time] at [Location]. According to the complaint, agents did not 
present a judicial warrant at the time of detention. Plaintiff 
alleges improper detention procedures and seeks immediate release.
```

### Extracted Data:

```
Location: [Location from filing]
Agencies Involved: ICE
Date: [MM/DD/YYYY from filing]
Description: [Name] was detained by ICE at approximately [Time] at [Location], according to emergency motion for release filed in [District Court] ([Case Number]). The complaint alleges agents did not present a judicial warrant at the time of detention and alleges improper detention procedures. Legal filing source indicates [additional relevant context].
Individuals Detained: 1
Map Address: [Full address], [City], [State] [ZIP]
Use of Force: [as documented in filing, if any]
Neighborhood: [Neighborhood]
News Coverage: [any news coverage of case]
Rapid Response Network Report: [if applicable]
Zip Code: [ZIP]
```

**Key Lessons:**
- Court filings = verified source
- Note case number and court
- Include legal allegations
- Mention warrant status when relevant
- Names may need redaction based on your policy

---

## Example 7: Multiple Sources - Cross-Verification

**Scenario:** Same incident reported in multiple sources

**Source 1:** [Rapid Response Network] social media (10:30 AM)
- Reports "federal agents" at [Location]
- States "at least 2 detained"
- No agency confirmation

**Source 2:** [Local News] article (2:00 PM same day)
- Confirms ICE operation at [Location]
- Reports "three people detained"
- Includes ICE spokesperson statement

**Source 3:** [Community Organization] update (3:00 PM)
- Confirms ICE at [Location]
- States "between 2-4 people detained"
- Provides vehicle descriptions

### Extracted Data (Combined):

```
Location: [Location]
Agencies Involved: ICE
Date: [MM/DD/YYYY]
Description: ICE operation at [Location] confirmed by multiple sources. [Rapid Response Network] initially reported at 10:30 AM that federal agents detained at least 2 people. [Local News] confirmed ICE involvement and reported 3 people detained according to ICE spokesperson. [Community Organization] stated between 2-4 people detained and identified vehicles: [vehicle descriptions]. Discrepancy in detention counts noted across sources (range: 2-4).
Individuals Detained: 3
Map Address: [Full address], [City], [State] [ZIP]
Use of Force: [blank]
Neighborhood: [Neighborhood]
News Coverage: https://[localnews].com/article
Rapid Response Network Report: [social media URL]
Zip Code: [ZIP]
```

**Key Lessons:**
- When counts differ, note the discrepancy
- Use most authoritative/recent count as primary
- List all sources in News Coverage field
- Cross-verification increases confidence level
- Time stamps show how story developed

---

## Example 8: Vague Report - Low Priority

**Source Type:** Unverified social media post  
**Platform:** [Twitter/Facebook community group]

**Posted Content:**
```
I think I saw ICE this morning in [General Area]??? Anyone else see this?
```

### Handling:

**DO NOT create database entry yet**

**Action:**
1. Flag for monitoring
2. Search for additional sources
3. Check rapid response networks
4. Search local news
5. Only document if confirmed by reliable source

**If confirmed by reliable source later:**
- Create entry using reliable source
- May mention original report as context
- Never rely solely on unverified social media

**Key Lessons:**
- Unconfirmed = do not document yet
- Question marks indicate uncertainty
- Vague location ("General Area")
- No specific details
- Wait for verification

---

## Example 9: Time-Sensitive Alert - Ongoing Incident

**Source Type:** Real-time social media alert  
**Status:** Incident in progress

**Posted Content:**
```
ACTIVE NOW - [Organization] reporting federal agents at [Location]
ONGOING - updates to follow
[Time stamp: 8:47 AM]
```

### Initial Documentation (Partial Entry):

```
Location: [Location]
Agencies Involved: [blank - pending confirmation]
Date: [MM/DD/YYYY]
Description: [PRELIMINARY ENTRY - INCIDENT IN PROGRESS] [Organization] reported at 8:47 AM that federal agents are actively conducting an operation at [Location]. Entry will be updated as more information becomes available.
Individuals Detained: [blank - not yet known]
Map Address: [Address], [City], [State] [ZIP]
[Remaining fields: pending updates]
```

**Follow-up Actions:**
1. Monitor source for updates
2. Search news for coverage
3. Check for additional community reports
4. Update entry when incident concludes
5. Change "PRELIMINARY" to final version

**Key Lessons:**
- Can create preliminary entry for active incidents
- Clearly mark as "IN PROGRESS" or "PRELIMINARY"
- Plan to update with final information
- Essential for real-time documentation
- Helps rapid response coordination

---

## Template for Your Own Examples

As you document incidents in your area, create your own example library:

```
## Example [NUMBER]: [Brief Description]

**Source Type:** [Social media/News/Court/Community org]
**Date of Incident:** [MM/DD/YYYY]

**Source Content:**
[Quote or describe the original source]

### Extracted Data:

Location: 
Agencies Involved: 
Date: 
Description: 
Individuals Detained: 
Map Address: 
Use of Force: 
Neighborhood: 
News Coverage: 
Rapid Response Network Report: 
Zip Code: 

**Key Lessons:**
- [What this example teaches about extraction]
- [Any unique challenges or decisions]
- [Why this example is instructive]
```

---

## Quick Reference: Extraction Patterns

### Date Formats to Convert
- "10/13 - 11AM" → 10/13/2025
- "Oct 2, 2PM-3PM" → 10/02/2025
- "Tuesday morning" → [Look up actual date]

### Location Patterns
- "51st and Racine" → "51st St and Racine Ave"
- "near [Landmark]" → "[Nearest intersection] near [Landmark]"
- "on [Street] between [A] and [B]" → "[Street] between [A] and [B]"

### Detention Counts
- "At least X" → Use X, note "at least" in Description
- "Multiple"/"Several" → Leave blank, note in Description
- "Between X-Y" → Use lower number or leave blank, note range

### Agency Identification
- "Federal agents" → Leave blank
- "ICE agents" → ICE
- "Border Patrol" → CBP
- "Confirmed as ICE" → ICE

### Vehicle Descriptions Format
- Always: Make, Model, Color
- If available: License plate, state, distinguishing features
- Example: "Black Ford Expedition (Illinois 311432, Mexican flag sticker)"

---

**Remember:** These are templates. Your real extractions will have the local specificity that makes them most useful. Build your own example library as you go!
