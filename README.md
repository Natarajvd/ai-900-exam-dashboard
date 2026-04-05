# Exam Quiz Dashboard

**Upload any Q&A file → take interactive quizzes → track your progress.**

A lightweight, browser-based exam practice tool. Works for any subject — certification prep, classroom quizzes, interview practice, trivia — if you can write questions in a simple text format, you can quiz yourself.

**🔗 Live Demo:** https://natarajvd.github.io/ai-900-exam-dashboard/

---

## ✨ Features

- **Universal** — supports any exam or quiz topic (Azure, AWS, medical, dev ops, trivia — anything)
- **Drag & drop** — upload `.md` or `.txt` question files, get instant quizzes
- **Instant feedback** — see correct answers and explanations as you go
- **Domain tracking** — score breakdown by topic/module
- **Practice wrong answers** — focus on what you missed
- **Autosave** — close the browser, come back, resume mid-exam
- **Dark & light themes**
- **Zero dependencies** — runs in any browser, no server, no database
- **100% client-side** — your data never leaves your machine

---

## 🚀 Get Started

### Option 1: Use the Live Site
Open [https://natarajvd.github.io/ai-900-exam-dashboard/](https://natarajvd.github.io/ai-900-exam-dashboard/) — start quizzing immediately. A sample exam is pre-loaded.

### Option 2: Run Locally
1. Clone or download this repo
2. Double-click `exam-hub.html`
3. Upload your question files and go

No server, no install, no config.

---

## 📝 Question Format

Questions are written in a simple, human-readable Markdown format:

```markdown
# Exam Title: Your Exam Name Here

## Module: Module Name

### Q1
Your question text goes here?

- **A.** First option
- **B.** Second option
- **C.** Third option
- **D.** Fourth option

**Correct answer:** B

**Explanation:** Why B is correct.

### Q2
Second question?
...
```

Full format guide with examples: [TUTORIAL.md](TUTORIAL.md)

**The parser is smart** — it handles variations like:
- `### Q1` or `### Question 1`
- `- **A.** text` or `A) text` or `a) text`
- `**Correct answer:** B` or `**Answer:** B`

---

## 📖 Full Tutorial

Detailed step-by-step guide: [TUTORIAL.md](TUTORIAL.md)

Covers:
- How the dashboard works
- Adding and managing exams
- Question format guide
- Taking exams (scoring, flagging, navigation)
- Troubleshooting

---

## 🛠 Project Structure

```
├── exam-hub.html          ← Main dashboard (open this!)
├── index.html             ← Auto-redirects to exam-hub.html
├── exam_format_guide.md   ← Question format quick reference
├── TUTORIAL.md            ← Complete tutorial & how-to
├── README.md              ← This file
├── LICENSE                ← MIT License
├── .gitignore             ← Ignores .txt/.md question files
└── tools/                 ← Python utilities (optional)
```

---

## ⚠️ Legal Disclaimer

This project provides **tooling only** — it does not include, distribute, or endorse any exam content.

- Users are solely responsible for ensuring any question banks they use comply with applicable exam NDAs, certification program terms, and copyright law.
- Do not use this tool with actual exam questions, exam dumps, or any material obtained in violation of an exam Non-Disclosure Agreement.
- This tool is intended only for legitimate practice questions from authorized sources or user-created content.

---

## 📜 License

MIT License — see [LICENSE](LICENSE).

---

## 🤝 Built With

- Built with [OpenClaw](https://openclaw.ai) — an AI agent framework that turns natural language into working code
- Powered by Tailwind CSS, Vanilla JS, and localStorage
