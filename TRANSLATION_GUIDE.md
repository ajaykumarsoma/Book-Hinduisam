# Telugu Translation Guide

## 📋 Translation Status

| File | English Lines | Telugu Status | Priority |
|------|---------------|---------------|----------|
| `index.md` | 280 | ✅ COMPLETE | P0 - Critical |
| `about.md` | 166 | ✅ COMPLETE | P0 - Critical |
| `chapter_05_definition_hindu.md` | 1,873 | 🟡 IN PROGRESS (150 lines done) | P1 - High |
| `chapter_00_etymology_war_of_words.md` | 1,076 | ❌ TODO | P1 - High |
| `chapter_01_prana_pratishtha.md` | ~900 | ❌ TODO | P2 - Medium |
| `chapter_02_temple_worship_questions.md` | ~600 | ❌ TODO | P2 - Medium |
| `chapter_03_pagan_roots_abrahamic.md` | ~1,200 | ❌ TODO | P2 - Medium |
| `chapter_04_atheist_communist_hypocrisy.md` | ~600 | ❌ TODO | P2 - Medium |
| `contribute.md` | ~100 | ❌ TODO | P3 - Low |
| `references/bibliography.md` | ~200 | ❌ TODO | P3 - Low |
| `references/glossary.md` | ~150 | ❌ TODO | P3 - Low |

**Total:** ~6,500 lines | **Completed:** ~600 lines (9%) | **Remaining:** ~5,900 lines (91%)

---

## 🎯 Translation Workflow

### Method 1: Manual Translation (Highest Quality)

**Best for:** Critical content, cultural concepts, Sanskrit terminology

**Steps:**
1. Copy English `.md` file
2. Rename to `.te.md` (e.g., `about.md` → `about.te.md`)
3. Translate content line by line
4. Preserve:
   - Markdown formatting (`#`, `**`, `*`, `-`, etc.)
   - Sanskrit terms in Devanagari (शिव, विष्णु, शक्ति)
   - Code blocks and diagrams
   - Links and references
5. Test: `mkdocs build`
6. Review for accuracy

**Example:**
```markdown
<!-- English -->
## Part 1: The Revolutionary Sanskrit Definition

<!-- Telugu -->
## భాగం 1: విప్లవాత్మక సంస్కృత నిర్వచనం
```

---

### Method 2: AI-Assisted Translation (Faster)

**Best for:** Large volumes, technical content

**Tools:**
- Google Translate API
- DeepL API
- GPT-4 with Telugu support
- Azure Translator

**Steps:**
1. Extract text from `.md` file (preserve formatting markers)
2. Send to translation API/AI
3. Review and correct:
   - Sanskrit terminology
   - Cultural concepts
   - Technical accuracy
4. Reinsert into markdown structure
5. Test build

---

### Method 3: Community Translation (Scalable)

**Best for:** Distributing work, engaging community

**Steps:**
1. Create GitHub issues for each chapter
2. Assign to Telugu-speaking volunteers
3. Set up review process:
   - Native speaker reviews
   - Technical accuracy checks
   - Cultural sensitivity review
4. Merge approved translations

---

## 📐 Translation Rules

### **1. Preserve Sanskrit Terms**

❌ **DON'T translate:**
- Deity names: शिव (Śiva), विष्णु (Viṣṇu), शक्ति (Śakti)
- Technical terms: ॐ (Om), ह्रीं (Hrīṃ), दुं (Duṃ)
- Scripture names: वेद (Veda), पुराण (Purāṇa), उपनिषद् (Upaniṣad)

✅ **DO translate:**
- Explanatory text
- Descriptions
- Instructions
- Navigation labels

**Example:**
```markdown
<!-- English -->
The Durgā mantra: ॐ ह्रीं दुं दुर्गायै नमः

<!-- Telugu -->
దుర్గా మంత్రం: ॐ ह्रीं दुं दुर्गायै नमः
```

---

### **2. Preserve Markdown Formatting**

**Headers:**
```markdown
# అధ్యాయం 1    (H1 - Chapter title)
## భాగం 1       (H2 - Major section)
### 1.1 విభాగం (H3 - Subsection)
```

**Emphasis:**
```markdown
**బోల్డ్ టెక్స్ట్**
*ఇటాలిక్ టెక్స్ట్*
`కోడ్ టెక్స్ట్`
```

**Lists:**
```markdown
- అంశం 1
- అంశం 2
  - ఉప అంశం 2.1

1. మొదటిది
2. రెండవది
```

**Links:**
```markdown
[టెక్స్ట్](url)
[ఇతర పేజీకి వెళ్ళండి](other_page.md)
```

---

### **3. Preserve Tables**

```markdown
| కాలం | సంఘటన | సమస్య |
|--------|-------|-------|
| క్రీ.పూ. 1500 | ఋగ్వేదం | "హిందూ" లేదు |
| క్రీ.పూ. 600 | పర్షియన్ | ప్రజలను సూచిస్తుంది |
```

---

### **4. Preserve Code Blocks and Diagrams**

❌ **DON'T translate:**
- Mermaid diagram syntax
- Code examples
- YAML configurations

✅ **DO translate:**
- Labels within diagrams
- Comments in code
- Descriptions

---

## 🔧 Automated Translation Script

See `scripts/translate_to_telugu.py` for automation tool.

**Usage:**
```bash
python scripts/translate_to_telugu.py docs/chapter_01_prana_pratishtha.md
```

**Features:**
- Preserves markdown formatting
- Skips Sanskrit terms
- Translates only English text
- Creates `.te.md` file automatically

---

## ✅ Quality Checklist

Before submitting translation:

- [ ] All English text translated to Telugu
- [ ] Sanskrit terms preserved in Devanagari
- [ ] Markdown formatting intact
- [ ] Links working
- [ ] Tables rendering correctly
- [ ] Mermaid diagrams displaying
- [ ] Build succeeds: `mkdocs build`
- [ ] Visual review: `mkdocs serve`
- [ ] Native speaker review (if possible)

---

## 🚀 Quick Start for Contributors

### Step 1: Setup
```bash
git clone https://github.com/ajaykumarsoma/Book-Hinduisam.git
cd Book-Hinduisam
pip install -r requirements.txt
```

### Step 2: Create Telugu Translation
```bash
# Copy English file
cp docs/chapter_01_prana_pratishtha.md docs/chapter_01_prana_pratishtha.te.md

# Edit Telugu version
nano docs/chapter_01_prana_pratishtha.te.md
```

### Step 3: Test
```bash
mkdocs build
mkdocs serve  # Visit http://localhost:8000/te/
```

### Step 4: Submit
```bash
git add docs/chapter_01_prana_pratishtha.te.md
git commit -m "Add Telugu translation: Chapter 1"
git push origin telugu-translation
# Create Pull Request on GitHub
```

---

## 📞 Help & Support

- **Questions:** Open an issue on GitHub
- **Discussions:** Join GitHub Discussions
- **Email:** (if available)

---

**🕉️ సత్యమేవ జయతే**

