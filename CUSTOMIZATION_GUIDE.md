# ICE/CBP Monitoring Template - Customization Guide

> ⏱️ **Time Required:** 30-60 minutes
> 🎯 **Difficulty:** Low - mostly find-and-replace with research
> ✅ **Prerequisites:** None - if you can edit text files, you can do this!

## 📋 Progress Tracker

Track your progress through the customization process:

- [ ] **Step 1:** Gather Local Information (15 min) → 25% complete
- [ ] **Step 2:** Customize Core Files (20 min) → 70% complete
- [ ] **Step 3:** Test Your Customization (10 min) → 85% complete
- [ ] **Step 4:** Add Your Branding (5 min) → 95% complete
- [ ] **Step 5:** Upload and Test (10 min) → 100% complete ✨

---

## Welcome!

This template helps you create a Claude skill for monitoring and documenting ICE and CBP enforcement activity in **your** city, town, or state. This guide walks you through adapting the template files to match your local context.

---

## Overview: What You're Creating

This skill will give Claude the ability to:
1. **Search** local and national sources for ICE/CBP enforcement incidents in your area
2. **Extract** structured data from various source types (news, social media, legal docs)
3. **Document** incidents in a standardized 11-field database format
4. **Verify** information across multiple sources
5. **Track** patterns and trends over time

---

## Quick Start: 5-Step Process

---

### Step 1: Gather Your Local Information
⏱️ **15 minutes** | 📊 **Progress: 0% → 25%**

Before editing any files, collect the following information about your area:

#### Geographic Information
- [ ] **City/Town Name:** _________________
- [ ] **State:** _________________
- [ ] **Metropolitan Area (if applicable):** _________________
- [ ] **Key Neighborhoods/Districts:** (list 5-10)
  - _________________
  - _________________
  - _________________
- [ ] **Surrounding Cities/Suburbs:** (list 3-5)
  - _________________
  - _________________

#### Local News Sources
Research and list:
- [ ] **Primary Local News Outlet:** _________________
- [ ] **Local Public Radio Station:** _________________
- [ ] **Local TV News Stations:** (list 2-3)
  - _________________
  - _________________
- [ ] **Community News Sites:** (hyperlocal blogs, alt-weeklies)
  - _________________

#### Community Organizations
Find local organizations that:
- Work on immigrant rights
- Provide rapid response services
- Document enforcement activity
- Provide legal services

List 3-5 organizations:
- [ ] **Organization 1:** Name: __________ Website: __________
- [ ] **Organization 2:** Name: __________ Website: __________
- [ ] **Organization 3:** Name: __________ Website: __________

#### Social Media Presence
Identify:
- [ ] **Local Rapid Response Networks:** (Instagram, TikTok, Twitter/X handles)
  - @_______________
  - @_______________
- [ ] **Community Alert Pages:** (Facebook groups, Telegram/WhatsApp channels)
  - _______________

#### Legal Resources
- [ ] **Federal District Court:** Which district? __________
- [ ] **PACER Court Code:** (if known) __________
- [ ] **Local Legal Aid Organizations:** _______________

#### Current Context (Optional but Helpful)
- [ ] **Is there a named operation?** (e.g., "Operation Jumping Frogs")
- [ ] **Start date of increased activity:** __________
- [ ] **Any unique local factors?** (border proximity, sanctuary policies, etc.)

---

### Step 2: Customize the Core Files
⏱️ **20 minutes** | 📊 **Progress: 25% → 70%**

#### File: `SKILL.md` (Main instructions for Claude)

**Find and replace these placeholders:**

| Placeholder | Replace With | Example |
|-------------|--------------|---------|
| `[CITY_NAME]` | Your city name | "Portland" |
| `[STATE_NAME]` | Your state name | "Oregon" |
| `[METRO_AREA]` | Metropolitan area name | "Portland Metropolitan Area" |
| `[OPERATION_NAME]` | Named operation (if any) | "Operation Jumping Frogs" |
| `[START_DATE]` | When monitoring began | "October 2025" |

**Update these sections:**

1. **Purpose section** (lines 8-11):
   - Change location references
   - Update operation name if applicable
   - Adjust time frame

2. **Key Sources to Monitor** (lines 99-122):
   - Replace with your local news outlets
   - Update community organization names and websites
   - Add your local rapid response networks
   - Include your federal court info

3. **Neighborhood Examples** (throughout):
   - Replace Chicago neighborhood names with your neighborhoods
   - Update ZIP codes to match your area
   - Adjust geographic references

4. **Contact Resources** (lines 305-313):
   - Update hotline numbers for your state/region
   - Replace organization names with your local groups
   - Update websites and contact information

**Example Search/Replace:**
```
Find: "Chicago"
Replace: "Portland"

Find: "Illinois"
Replace: "Oregon"

Find: "Operation Midway Blitz"
Replace: "Jumping Frogs"

Find: "Back of the Yards"
Replace: "Bridgeton"
```

#### File: `README.md` (User-facing documentation)

**Update these sections:**

1. **Overview** (top):
   - Change "Chicago" to your city
   - Update operation name
   - Adjust dates

2. **Data Structure Table** (lines 66-81):
   - Change example addresses to local ones
   - Update neighborhoods to your neighborhoods
   - Use your local ZIP codes

3. **Source Coverage** (lines 99-105):
   - List YOUR local news outlets
   - Name YOUR rapid response networks
   - Include YOUR community organizations

4. **Customization Section** (lines 182-202):
   - Update "Currently optimized for" with your geography
   - Adjust primary/secondary/context areas

5. **Contact Section** (bottom):
   - Update creator name (or remove if making public)
   - Update organization name
   - Adjust license/usage notes as appropriate

#### File: `reference/examples.md`

You have two options:

**Option A: Keep Generic (Easier)**
- Leave the Chicago examples as-is
- Add a note at the top: "These examples use Chicago data. Apply the same methodology to your local sources."

**Option B: Create Local Examples (More Work)**
- Replace each example with incidents from your area
- Use your local street names, neighborhoods, ZIP codes
- Include bilingual content if relevant to your community

**Recommendation:** Start with Option A, update later with real examples as you document incidents.

#### File: `reference/search-strategies.md`

**Update search queries to include:**
- Your city name: `"ICE [YOUR_CITY] arrest today"`
- Your neighborhoods: `"ICE activity [YOUR_NEIGHBORHOOD]"`
- Your local news sites: `site:[yourlocalnews.com] ICE`

**Example transformations:**
```
Before: "ICE Chicago arrest today"
After: "ICE Miami arrest today"

Before: "site:blockclubchicago.org ICE"
After: "site:miamiherald.com ICE"

Before: "Pilsen immigration raid"
After: "Little Havana immigration raid"
```

#### File: `reference/integration-guide.md`

**Minimal changes needed:**
- Update workflow examples to use your city name
- Change neighborhood references to your areas
- Otherwise, the workflows are largely geography-agnostic

---

### Step 3: Test Your Customization
⏱️ **10 minutes** | 📊 **Progress: 70% → 85%**

Before uploading to Claude:

1. **Do a global search** in all files for these terms:
   - "Chicago" (should appear only in examples or as comparison)
   - "Illinois" (should be replaced with your state)
   - "Operation Midway Blitz" (should be your operation name or removed)
   - "ICIRR" (should be replaced with your local org)

2. **Verify all URLs** are updated:
   - News site URLs
   - Organization websites
   - Social media handles

3. **Check geographic consistency:**
   - All neighborhoods match your area
   - ZIP codes are correct
   - Addresses are realistic for your city

---

### Step 4: Add Your Branding (Optional)
⏱️ **5 minutes** | 📊 **Progress: 85% → 95%**

If you're creating this for:
- **Personal use:** Add your name to README contact section
- **Organization:** Add your org's name and logo reference
- **Public release:** Consider adding a license and usage guidelines
- **Client work:** Brand appropriately per your agreement

You can add a `CREDITS.md` file:
```markdown
# Credits

**Adapted from:** ICE/CBP Chicago Monitoring Template
**Original Template by:** Andrew Thrasher, Titus Legal Design
**Customized for:** [Your City]
**Customized by:** [Your Name/Organization]
**Date:** [Date]

## Usage
[Your usage terms here]
```

---

### Step 5: Upload and Test
⏱️ **10 minutes** | 📊 **Progress: 95% → 100%** ✨

1. **Zip your customized folder:**
   ```bash
   zip -r ice-cbp-[yourcity]-monitoring.zip ice-cbp-[yourcity]-monitoring/
   ```

2. **Upload to Claude:**
   - Go to claude.ai
   - Navigate to Settings → Skills (or upload via Claude Code)
   - Upload your zip file
   - Wait for confirmation

3. **Test with these prompts:**
   ```
   "Run daily ICE monitoring for [YOUR_CITY] - last 24 hours"
   
   "What sources should I check for ICE activity in [YOUR_NEIGHBORHOOD]?"
   
   "Help me extract data from this news article about ICE activity"
   ```

4. **Verify Claude:**
   - Uses your city name correctly
   - References your local organizations
   - Suggests appropriate local news sources
   - Uses your local geographic terms

---

## Advanced Customization

### Adjusting Data Fields

The default schema has 11 fields. You may want to:

**Add fields:**
- "Immigration Court Location" for your district
- "State/Local Law Enforcement Involvement" 
- "Language Services Provided"
- "Legal Status of Detention" (warrant vs. administrative)

**To add a field:**
1. Add to "Data Schema" section in SKILL.md
2. Update output format template
3. Add to quality checklist
4. Update example extractions

**Remove fields:**
If certain fields don't apply to your context, mark as "Optional" and add usage notes.

### Adjusting Search Frequency

Default recommendations:
- Daily: Morning + evening (15 minutes each)
- Weekly: 60-minute deep dive

Adjust based on:
- **High activity area:** Increase to 3x daily
- **Low activity area:** Reduce to 2-3x weekly
- **Historical documentation:** Weekly is sufficient

### Language Considerations

**If your community is primarily English:**
- Remove Spanish-language notes from extraction guidelines
- Simplify bilingual processing sections

**If your community uses other languages:**
- Add common terms in those languages (see SKILL.md lines 162-167 for Spanish example)
- Note which sources publish in which languages
- Add translation considerations to quality guidelines

**If your community is multilingual:**
- Expand language support sections
- Document which rapid response networks use which languages
- Consider multiple language versions of rapid response guidelines

### Special Operational Contexts

**Sanctuary City:**
- Track exceptions to sanctuary policies
- Document state/federal conflicts
- Monitor court challenges
- Focus on ICE workarounds

**287(g) Jurisdiction:**
- Track local law enforcement involvement
- Document jail cooperation
- Monitor booking procedures
- Track detainer issuance

**High-Profile Operation:**
- Increase search frequency
- Add operation-specific terminology
- Track official announcements
- Monitor political statements

---

## Troubleshooting

### "Claude keeps using Chicago instead of my city"

**Solution:** You missed some replacements. Do a full-text search:
```bash
grep -r "Chicago" ice-cbp-monitoring/
```
Replace remaining instances.

### "Claude suggests news sources I didn't configure"

**Solution:** Claude may be using general knowledge. Be more explicit in prompts:
```
"Use ONLY the local sources configured in this skill"
```

### "My rapid response networks don't use Instagram"

**Solution:** Update the Instagram-specific sections:
1. Change "Instagram alerts" to your platforms (Facebook, Telegram, etc.)
2. Update image extraction guidelines to match your platform's format
3. Adjust URL format examples

### "We don't have named neighborhoods, just ZIP codes"

**Solution:** 
1. Replace neighborhood fields with ZIP-focused location tracking
2. Update examples to use ZIP+street address
3. Simplify location extraction rules

### "The data schema doesn't match our needs"

**Solution:** See "Adjusting Data Fields" above. Common changes:
- Combine "Agencies Involved" with "Description"
- Split "Use of Force" into severity levels
- Add "Source Credibility Rating"

---

## File Checklist

Before uploading, verify you've customized:

- [ ] `SKILL.md` - Main Claude instructions
  - [ ] City/state names updated
  - [ ] Local sources added
  - [ ] Neighborhood names changed
  - [ ] Contact resources updated
  
- [ ] `README.md` - User documentation  
  - [ ] Overview updated
  - [ ] Examples changed
  - [ ] Contact info updated
  
- [ ] `reference/examples.md` - Extraction examples
  - [ ] Decision: Keep generic or customize
  - [ ] If customized: All examples reflect your area
  
- [ ] `reference/search-strategies.md` - Query library
  - [ ] Search queries updated for your city
  - [ ] Local news sites added
  - [ ] Neighborhood searches customized
  
- [ ] `reference/integration-guide.md` - Advanced workflows
  - [ ] Workflow examples updated (optional)
  - [ ] Geographic references changed
  
- [ ] `scripts/ice_documentation_helper.py` - Python tools
  - [ ] Optional: Update default values in script
  - [ ] Optional: Customize for your data pipeline

---

## Getting Help

### Resources
- **Claude Prompting Guide:** docs.anthropic.com/claude/docs/prompt-engineering
- **Anthropic's Claude Skills Guide:** https://github.com/anthropics/skills

### Common Questions

**Q: Can I use this for multiple cities?**  
A: Yes! Create separate skill folders for each city. Name them uniquely: `ice-cbp-austin-monitoring`, `ice-cbp-houston-monitoring`, etc.

**Q: Can I share my customized version?**  
A: Yes, but consider:
- Remove any personal API keys or credentials
- Add appropriate licensing
- Credit the original template
- Consider community needs and safety

**Q: How often should I update this skill?**  
A: Update when:
- New reliable sources emerge
- Operation name or scope changes
- Data schema needs adjustment
- You discover better search strategies

**Q: Can I merge this with other monitoring efforts?**  
A: Yes! This skill can complement:
- Court watching programs
- Know Your Rights campaigns  
- Immigration lawyer intakes
- Policy advocacy research
- Academic/journalistic investigations

---

## Template Metadata

**Original Template Version:** 1.0  
**Template Created:** October 2025  
**Original Creator:** Andrew Thrasher, Titus Consulting 
**Template License:** MIT (see LICENSE)  
**Compatible With:** Claude Sonnet 4.5, Opus 4, Haiku 3.5

---

## Next Steps

Once customized:

1. **Test thoroughly** with real incidents from your area
2. **Refine** search queries based on what works
3. **Document** your own best practices
4. **Share** with your community (if appropriate)
5. **Iterate** - this is a living tool

**Ready to begin?** Start with Step 1: Gather Your Local Information ⬆️

---

**Questions or need help customizing?**  
Consider consulting with:
- Local immigrant rights organizations  
- Community documentation projects
- Tech-for-good consultants (like Titus Consulting!)
- Other users who have customized this template

**Good luck, and thank you for doing this important work.**
