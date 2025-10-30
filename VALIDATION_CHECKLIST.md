# Template Validation Checklist

Use this checklist to verify your customization is complete before uploading to Claude.

## ✅ Pre-Upload Validation

### Step 1: Placeholder Check

Run these searches across all files to find remaining placeholders:

```bash
# From the template directory
grep -r "\[CITY_NAME\]" .
grep -r "\[STATE_NAME\]" .
grep -r "\[LOCAL_" .
grep -r "\[NEIGHBORHOOD" .
grep -r "\[ORGANIZATION" .
grep -r "\[OPERATION_NAME\]" .
```

**Expected result:** No matches (or only in example files you chose to keep generic)

- [ ] No `[CITY_NAME]` placeholders found
- [ ] No `[STATE_NAME]` placeholders found
- [ ] No `[LOCAL_*]` placeholders found
- [ ] No `[NEIGHBORHOOD*]` placeholders found
- [ ] No `[ORGANIZATION*]` placeholders found
- [ ] No operation placeholders (unless not applicable)

---

### Step 2: Required Content Check

Verify you've added your local information to these key sections:

#### SKILL.md
- [ ] Line 2-3: Name and description updated with your city
- [ ] Lines 99-122: "Key Sources to Monitor" section has your sources
- [ ] Lines 305-313: "Contact Resources" section updated
- [ ] Throughout: Neighborhood names are from your area

#### README.md (or README_NEW.md)
- [ ] Title and description reference your location
- [ ] "Source Coverage" section lists your sources
- [ ] Example addresses use your city's format
- [ ] Contact section updated (if customizing for others)

#### search-strategies.md
- [ ] Search queries include your city name
- [ ] Site-specific searches use your news sites
- [ ] Neighborhood searches use your neighborhoods

---

### Step 3: Data Consistency Check

Verify consistency across files:

- [ ] City name spelled consistently everywhere
- [ ] State name spelled consistently everywhere
- [ ] News sources match across all files
- [ ] Organization names match across all files
- [ ] Neighborhood names match across all files
- [ ] ZIP codes are correct for your area

---

### Step 4: URL Validation

Check that all URLs are complete and working:

- [ ] News outlet URLs work and point to correct sites
- [ ] Organization websites are accessible
- [ ] Social media handles exist
- [ ] Court/PACER information is correct
- [ ] No broken links in documentation

---

### Step 5: File Structure Check

Ensure all files are present:

```bash
# Check file structure
ls -la
```

Required files:
- [ ] SKILL.md (main skill file - REQUIRED)
- [ ] README.md (user documentation)
- [ ] CUSTOMIZATION_GUIDE.md
- [ ] QUICK_START.md
- [ ] LICENSE
- [ ] examples.md
- [ ] search-strategies.md
- [ ] integration-guide.md
- [ ] ice_documentation_helper.py

Optional but recommended:
- [ ] CONTRIBUTING.md
- [ ] CODE_OF_CONDUCT.md
- [ ] CHANGELOG.md
- [ ] ATTRIBUTION.md
- [ ] .github/ directory with templates

---

### Step 6: Privacy & Security Check

Verify no sensitive information included:

- [ ] No real addresses of community members
- [ ] No personal identifying information
- [ ] No sensitive organizational details
- [ ] No API keys or credentials
- [ ] No internal coordination plans
- [ ] Examples are anonymized or generic

---

### Step 7: Geographic Logic Check

Verify your geographic customizations make sense:

- [ ] Neighborhoods are actually in your city
- [ ] ZIP codes match your neighborhoods
- [ ] Surrounding cities/areas are correct
- [ ] Federal court district is correct
- [ ] Metropolitan area boundaries make sense

---

### Step 8: Language & Terminology Check

If your area is multilingual:
- [ ] Added relevant language patterns (SKILL.md lines ~162-167)
- [ ] Documented which sources use which languages
- [ ] Included bilingual extraction examples (if applicable)

If your area is English-only:
- [ ] Removed or simplified bilingual sections
- [ ] Noted English-only in customization details

---

## 🧪 Test Cases

Before finalizing, test these scenarios:

### Test 1: Basic Monitoring
```
Prompt: "Run daily ICE monitoring for [YOUR_CITY] - last 24 hours"
```

Expected: Claude should:
- [ ] Reference YOUR city correctly
- [ ] Suggest YOUR local news sources
- [ ] Use YOUR geographic terminology
- [ ] Not mention template placeholders or other cities

---

### Test 2: Source Specificity
```
Prompt: "What sources should I check for ICE activity?"
```

Expected: Claude should:
- [ ] List YOUR configured sources
- [ ] Include YOUR local organizations
- [ ] Reference YOUR rapid response networks
- [ ] Use YOUR city/neighborhood names

---

### Test 3: Data Extraction
```
Prompt: "Extract incident data from this alert: [paste a sample alert using your city's address format]"
```

Expected: Claude should:
- [ ] Correctly parse YOUR address format
- [ ] Use YOUR neighborhood names
- [ ] Format address with YOUR city/state/ZIP
- [ ] Apply YOUR configured verification standards

---

### Test 4: Geographic Knowledge
```
Prompt: "I heard about activity near [YOUR_NEIGHBORHOOD]. How should I search for more information?"
```

Expected: Claude should:
- [ ] Recognize YOUR neighborhood name
- [ ] Suggest appropriate searches for YOUR area
- [ ] Reference YOUR local sources
- [ ] Not confuse with other cities

---

## 🎯 Quality Checks

### Completeness Check

Rate your customization (be honest!):

**Geographic Info:**
- [ ] 5/5 - All neighborhoods, ZIP codes, addresses customized
- [ ] 4/5 - Most customized, some generic placeholders remain
- [ ] 3/5 - Basic city/state done, details missing
- [ ] 2/5 - Only city name changed
- [ ] 1/5 - Minimal changes

**Source Coverage:**
- [ ] 5/5 - Comprehensive local sources added
- [ ] 4/5 - Major sources added, missing some alternatives
- [ ] 3/5 - Basic news sources only
- [ ] 2/5 - Generic sources, not local
- [ ] 1/5 - No customization

**Organization Info:**
- [ ] 5/5 - Multiple local orgs with contacts
- [ ] 4/5 - Some orgs added
- [ ] 3/5 - One or two orgs only
- [ ] 2/5 - Generic placeholders remain
- [ ] 1/5 - No customization

**Target Score:** 12-15 points total (4-5 in each category)

---

## 🚀 Ready to Upload?

Before uploading to Claude, you should have:

- [ ] All placeholders replaced (Score: 5/5 in each category above)
- [ ] All test cases passed
- [ ] No sensitive information included
- [ ] Files are properly named and structured
- [ ] Documentation reflects your customizations

If you checked all boxes above, you're ready! If not, revisit the relevant sections of [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md).

---

## 📦 Creating the Upload Package

### For claude.ai or Claude Code:

1. **Zip your folder:**
   ```bash
   cd /path/to/parent/directory
   zip -r ice-cbp-[yourcity]-monitoring.zip ice-cbp-[yourcity]-monitoring/
   ```

2. **Verify the zip:**
   ```bash
   unzip -l ice-cbp-[yourcity]-monitoring.zip
   ```
   - Should include all files
   - Should not include .git/ directory (if you cloned)
   - Should not include sensitive files

3. **Upload:**
   - claude.ai: Settings → Skills → Upload
   - Claude Code: Follow project upload instructions

---

## 🔄 Post-Upload Verification

After uploading to Claude:

### Immediate Tests

1. **Start a new conversation with Claude**
2. **Run Test 1 from above** ("Run daily ICE monitoring for [YOUR_CITY]")
3. **Check Claude's response for:**
   - [ ] Uses your city name
   - [ ] Suggests your sources
   - [ ] No placeholder text
   - [ ] Contextually appropriate

### If Something's Wrong

**Problem:** Claude uses template city instead of yours
**Solution:** Check that SKILL.md line 2-3 has your city in the description

**Problem:** Claude suggests sources you didn't configure
**Solution:** Claude may use general knowledge. Be more explicit: "Use ONLY sources configured in this skill"

**Problem:** Claude can't access the skill
**Solution:** Verify the folder structure and that SKILL.md is present

**Problem:** Extraction format is wrong
**Solution:** Check SKILL.md lines 225-243 for correct output format

---

## 📝 Maintenance Checklist

After initial deployment, periodically check:

### Monthly
- [ ] Test that Claude still uses your sources correctly
- [ ] Verify links to news sites still work
- [ ] Check if new local sources have emerged
- [ ] Review extraction accuracy

### Quarterly
- [ ] Update organization contact information
- [ ] Add newly discovered sources
- [ ] Refine search queries based on what works
- [ ] Update examples with real usage patterns

### When Template Updates
- [ ] Check [CHANGELOG.md](CHANGELOG.md) for updates
- [ ] Review what changed in new version
- [ ] Merge relevant improvements
- [ ] Re-test after merging

---

## 🆘 Troubleshooting

If validation fails, see [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) "Troubleshooting" section (lines 356+).

Common issues:
- Remaining placeholders → Use grep commands above to find them
- Inconsistent terminology → Do find-and-replace with correct terms
- Wrong geography → Double-check neighborhood/ZIP pairings
- Sources not working → Verify URLs are complete and accessible

---

## ✨ You're Ready!

Once you've completed this checklist, your customized template is ready to support your community's documentation efforts.

**Next Steps:**
1. Start with daily monitoring
2. Document your first real incident
3. Refine based on what you learn
4. Share successes (and challenges) with the community

**Questions?** See [README.md](README.md#support) for support resources.

---

**Validation Checklist Version:** 1.0
**Last Updated:** October 2025
**For Template Version:** 1.0.0
