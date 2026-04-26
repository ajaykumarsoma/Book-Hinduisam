# 🕉️ Hinduism: A Complete Journey

A comprehensive, AI-assisted scholarly exploration of Hinduism — multi-agent book generation system using CrewAI + MkDocs Material.

**🌐 Live Book:** [https://ajaykumarsoma.github.io/Book-Hinduisam](https://ajaykumarsoma.github.io/Book-Hinduisam) *(will be available after first deployment)*

---

## 📖 About This Project

This book is written **chapter by chapter** using a 4-agent AI research team:

| Agent | Role | Function |
|-------|------|----------|
| 🔍 **Research Agent** | Hindu Scripture Specialist | Sources from Vedas, Upaniṣads, Gītā, Purāṇas, Āgamas |
| 📜 **Sanskrit Scholar** | Vedic & Sanskrit Expert | Validates terms, IAST transliteration, mantras |
| ✍️ **Writer Agent** | Spiritual Literature Author | Writes 1,500–4,000 word polished chapters |
| 📝 **Editor Agent** | Senior Book Editor | Polishes flow, consistency, final Markdown |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Git
- LLM access (choose one):
  - **Ollama** (100% free, local) — [ollama.com](https://ollama.com)
  - **Groq** (free API, cloud) — [console.groq.com](https://console.groq.com)
  - **Google Gemini** (free tier) — [ai.google.dev](https://ai.google.dev)
  - **OpenAI** (paid) — [platform.openai.com](https://platform.openai.com)

### Installation

```bash
# Clone the repository
git clone https://github.com/ajaykumarsoma/Book-Hinduisam.git
cd Book-Hinduisam

# Set up environment
cp .env.example .env
# Edit .env and add your LLM credentials (see options inside file)

# Install dependencies
pip install -r requirements.txt
```

### Generate a Chapter

```bash
# Using Makefile (recommended)
make chapter N=2 TITLE="The Vedas" PROMPT="Write about the four Vedas, their structure, philosophy..."

# Or directly
python scripts/generate_chapter.py \
    --chapter-num 2 \
    --title "The Vedas" \
    --prompt "Write about the four Vedas..."
```

### Preview the Book

```bash
make serve
# Opens at http://127.0.0.1:8000
```

### Deploy to GitHub Pages

```bash
make deploy
```

---

## 📚 Chapters

- **Chapter 1:** [Prāṇa Pratiṣṭhā — Installing the Divine](chapters/chapter_01_prana_pratishtha.md) (8,750 words) ✅
  - Temple consecration science & ritual
  - Historical evolution, regional variations
  - Documented phenomena at 20+ temples (growing/breathing/sweating mūrtis)

*(More chapters will be added as they are generated)*

---

## 🏗️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Book Rendering** | MkDocs + Material Theme |
| **Hosting** | GitHub Pages (free, auto-deployed via Actions) |
| **Multi-Agent System** | CrewAI 0.51+ |
| **LLM Support** | Ollama / Groq / Gemini / OpenAI (via LiteLLM) |
| **Content Format** | Markdown with YAML frontmatter |
| **CI/CD** | GitHub Actions |

---

## 📂 Project Structure

```
Book-Hinduisam/
├── agents/               # CrewAI agent definitions
│   └── hinduism_crew.py
├── scripts/              # CLI tools
│   ├── generate_chapter.py
│   └── update_nav.py
├── config/               # Book settings
│   └── book_config.yaml
├── docs/                 # MkDocs content
│   ├── index.md
│   └── chapters/
├── chapters/             # Source chapters (mirrored to docs/)
│   └── chapter_01_prana_pratishtha.md
├── .github/workflows/    # CI/CD
│   └── deploy.yml
├── mkdocs.yml           # Book configuration
├── requirements.txt     # Python dependencies
├── Makefile            # Convenience commands
└── .env.example        # LLM credentials template
```

---

## 🎯 Features

✅ **Multi-provider LLM support** — Works with free (Ollama, Groq) or paid (OpenAI) models  
✅ **Automatic navigation** — New chapters auto-update book's table of contents  
✅ **Git integration** — Each chapter auto-commits with structured message  
✅ **Beautiful rendering** — MkDocs Material theme with search, dark mode, mobile-friendly  
✅ **Sanskrit support** — IAST transliteration, glossary tables  
✅ **GitHub Pages deployment** — One command to publish  

---

## 🤝 Contributing

This is a living book! Contributions welcome:
- **Suggest chapter topics** — Open an issue with a prompt
- **Improve existing chapters** — Submit a PR with edits
- **Add references** — Cite primary Śāstras, scholarly works
- **Report errors** — Sanskrit typos, factual corrections

---

## 📜 License

Content: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)  
Code: [MIT License](LICENSE)

---

## 🙏 Acknowledgments

- **Primary Sources:** Vedas, Upaniṣads, Bhagavad Gītā, Purāṇas, Āgamas
- **Scholarly Works:** Stella Kramrisch, S. Radhakrishnan, Devdutt Pattanaik, David Frawley
- **Technology:** CrewAI, MkDocs Material, GitHub Pages

---

**Om Shanti** 🕉️
