# Contributing to ICE/CBP Monitoring Skill Template

Thank you for your interest in improving this template! This document outlines how to contribute customizations, improvements, and bug fixes.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Community Support](#community-support)

## Code of Conduct

This project follows a Code of Conduct that all contributors are expected to uphold. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## How Can I Contribute?

### 1. Reporting Issues

**Before submitting an issue:**
- Check existing issues to avoid duplicates
- Use the issue template provided
- Include your customization details (city, state, sources used)

**Good bug reports include:**
- Clear description of the problem
- Steps to reproduce
- Expected vs. actual behavior
- Your Claude version (Sonnet 4.5, Opus 4, etc.)
- Relevant file excerpts (remove sensitive info!)

### 2. Suggesting Enhancements

We welcome suggestions for:
- New data fields
- Improved search strategies
- Additional source types
- Better extraction patterns
- Documentation improvements
- Automation scripts

**Use the Feature Request template** and include:
- Use case description
- Why this benefits the broader community
- Potential implementation approach

### 3. Sharing Your Customization

If you've customized this for a specific city/region and want to share:

**Option A: Share as Example** (Recommended)
- Create a sanitized version (remove sensitive details)
- Submit as documentation example
- Help others learn from your approach

**Option B: Create City-Specific Fork**
- Fork this repository
- Customize for your location
- Link back to this template
- Follow attribution guidelines

### 4. Improving Documentation

Documentation improvements are highly valued:
- Fix typos or unclear instructions
- Add examples from real usage
- Improve customization guides
- Translate to other languages
- Create video tutorials or diagrams

### 5. Contributing Code

For Python scripts or technical improvements:
- Follow PEP 8 style guidelines
- Include docstrings
- Add comments for complex logic
- Test with multiple scenarios
- Update relevant documentation

## Getting Started

### For First-Time Contributors

1. **Fork the repository** (if this becomes a GitHub project)
2. **Clone your fork locally**
3. **Create a branch** for your contribution:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**
5. **Test thoroughly** with a customized version
6. **Commit with clear messages**
7. **Submit a pull request**

### Setting Up Your Development Environment

```bash
# Clone the repository
git clone https://github.com/[username]/ice-cbp-monitoring-template.git
cd ice-cbp-monitoring-template

# Install Python dependencies (if working on scripts)
pip install -r requirements.txt

# Create a test customization
cp -r . ../test-customization
cd ../test-customization
# Follow CUSTOMIZATION_GUIDE.md
```

## Contribution Guidelines

### File Structure Standards

When adding new files:
- Use clear, descriptive filenames
- Add to appropriate directory (reference/, scripts/, .github/)
- Update README's file structure section
- Include header comments explaining purpose

### Documentation Standards

- Use Markdown formatting consistently
- Include table of contents for long documents (>100 lines)
- Add code examples in fenced blocks with language tags
- Use clear section headers (##, ###)
- Link between related documents
- Keep line length reasonable (~80-100 chars for readability)

### Search Strategy Contributions

When contributing new search queries:
- Test queries thoroughly
- Note which sources work best
- Include expected result count ranges
- Document any geographic specificity
- Consider multilingual communities

### Example Contribution Standards

When adding extraction examples:
- Use realistic but anonymized data
- Show complete before/after
- Explain decision points
- Include quality check results
- Note source verification level

### Code Standards (Python)

```python
# Good: Clear function with docstring
def extract_date_from_alert(text: str) -> Optional[str]:
    """
    Extract date from rapid response alert text.

    Args:
        text: Alert text that may contain date patterns

    Returns:
        Date in MM/DD/YYYY format or None if not found

    Example:
        >>> extract_date_from_alert("Alert: 10/13 - 11AM activity")
        '10/13/2025'
    """
    # Implementation here
    pass
```

### Commit Message Guidelines

Use clear, descriptive commit messages:

```bash
# Good commits
git commit -m "Add Seattle-specific search queries"
git commit -m "Fix date parsing for Spanish-language alerts"
git commit -m "Docs: Clarify PACER search instructions"

# Less helpful commits
git commit -m "Update file"
git commit -m "Fix bug"
git commit -m "Changes"
```

**Format:**
```
<type>: <short description>

<optional longer description>

<optional issue reference>
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Formatting, no code change
- `refactor:` Code restructuring
- `test:` Adding tests
- `chore:` Maintenance tasks

## Pull Request Process

1. **Update documentation** to reflect your changes
2. **Test your changes** with a full customization workflow
3. **Update CHANGELOG.md** following existing format
4. **Describe your changes** clearly in the PR
5. **Link related issues** using "Fixes #123" syntax
6. **Be responsive** to review feedback
7. **Ensure CI passes** (if applicable)

### PR Template

Your PR description should include:
- **What**: What does this PR do?
- **Why**: Why is this change needed?
- **How**: How does it work?
- **Testing**: How was it tested?
- **Screenshots**: If UI/documentation changes

## Community Support

### Getting Help

- **Customization questions**: Open a Discussion (preferred) or Issue
- **Technical problems**: Open an Issue with template
- **General questions**: Check existing Discussions first
- **Security concerns**: See SECURITY.md for private disclosure

### Helping Others

- Answer questions in Issues/Discussions
- Share your experiences and tips
- Review pull requests
- Suggest documentation improvements
- Share your customized workflows (anonymized)

## Recognition

Contributors will be recognized in:
- CHANGELOG.md for their contributions
- README.md contributors section (if significant contribution)
- Release notes for major contributions

## Special Considerations

### Sensitive Information

**Never include:**
- Specific addresses or identifying information
- Personal data of community members
- Sensitive organizational details
- API keys or credentials
- Internal coordination plans

**Always:**
- Anonymize examples
- Use placeholders for sensitive data
- Sanitize screenshots
- Review before sharing

### Working with Communities

If you're customizing this as part of community work:
- Coordinate with local organizations
- Respect community privacy concerns
- Consider whether public sharing is appropriate
- Follow organizational guidelines
- Prioritize community safety

### Legal and Ethical Considerations

- Use this tool responsibly and ethically
- Follow local laws regarding documentation
- Respect privacy and data protection requirements
- Coordinate with legal advocates when appropriate
- Consider security implications of public sharing

## Attribution Requirements

When using or adapting this template:

**Appreciated:**
- Credit original template creator (Andrew Thrasher / Titus Cosulting)
- Link back to original template repository
- Note what you changed/customized
- Share improvements back to the community
- Note what worked well in your customization
- Help others who customize for similar contexts

## Questions?

- Check [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) for setup questions
- Review [README.md](README.md) for general information
- Open a Discussion for community questions
- Create an Issue for bugs or specific problems

---

**Thank you for contributing to this project!** Your work helps communities document accountability and support immigrant rights.
