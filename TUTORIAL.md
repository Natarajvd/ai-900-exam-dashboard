# 📘 Exam Quiz Dashboard — Complete Tutorial

> A step-by-step guide for creating exams, uploading questions, and using the quiz dashboard.

---

## 📋 Table of Contents
1. [What Is This?](#1-what-is-this)
2. [Quick Start](#2-quick-start)
3. [How It Works](#3-how-it-works)
4. [Creating Your First Exam File](#4-creating-your-first-exam-file)
5. [Adding Exams to the Dashboard](#5-adding-exams-to-the-dashboard)
6. [Taking a Quiz](#6-taking-a-quiz)
7. [Managing Your Exams](#7-managing-your-exams)
8. [Features Explained](#8-features-explained)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. What Is This?

A **universal quiz dashboard** that turns simple text files into interactive practice exams. Works for **any subject**:

- Certification exams (Azure, AWS, GCP, Cisco, CompTIA, etc.)
- University course quizzes
- Interview question practice
- Trivia & knowledge tests
- Corporate training assessments

You write questions in a plain text format → the dashboard parses them → you get an interactive quiz with scoring, feedback, and progress tracking.

**Everything runs in your browser.** No server, no database, no installs.

---

## 2. Quick Start

### Use the Live Site
Visit: **https://natarajvd.github.io/ai-900-exam-dashboard/**

A sample exam is pre-loaded so you can try it immediately.

### Run Locally
1. Clone or download this repo
2. Double-click **`exam-hub.html`**
3. Upload your own question files

---

## 3. How It Works

```
Your text file (.md / .txt)
        │
        ▼
  Drag & Drop / Upload
        │
        ▼
  Dashboard parses questions
        │
        ▼
  Interactive quiz with:
  • Multiple choice (A/B/C/D)
  • Instant correct/wrong feedback
  • Explanations
  • Score tracking
  • Domain breakdowns
```

All data stays in your browser's **localStorage** — nothing is uploaded to any server.

---

## 4. Creating Your First Exam File

Create a `.md` (Markdown) or `.txt` file with your questions. Here's the format:

### Basic Structure

```markdown
# Exam Title: Your Exam Name Here

## Module: Topic / Domain Name

### Q1
Your question text here?

- **A.** First option
- **B.** Second option
- **C.** Third option
- **D.** Fourth option

**Correct answer:** B

**Explanation:** Why B is the right answer.

### Q2
Second question here?

- **A.** Option A
- **B.** Option B
- **C.** Option C
- **D.** Option D

**Correct answer:** C
**Explanation:** Explanation goes here.
```

### Format Variations The Parser Accepts

| What You Write | What It Means |
|---|---|
| `### Q1` or `### Question 1` or `### 1.` | Question number |
| `- **A.** text` or `A) text` or `a) text` | Option A |
| `- **B.** text` or `B) text` or `b) text` | Option B |
| `**Correct answer:** B` or `**Answer:** B` or `**Answer: B**` | Correct option (A/B/C/D) |
| `**Explanation:** text` (optional) | Explanation text |

### Example: AWS Exam

```markdown
# AWS Cloud Practitioner Practice Exam

## Cloud Concepts

### Q1
What are the benefits of cloud computing compared to on-premises? (Choose two)

- **A.** Pay-as-you-go pricing
- **B.** Unlimited storage by default
- **C.** Global reach in minutes
- **D.** No need for security controls

**Correct answer:** A
**Explanation:** Pay-as-you-go pricing and global reach are core cloud benefits.
```

### Example: Python Quiz

```markdown
# Python Programming Quiz

## Data Types

### Q1
Which data type is immutable in Python?

- **A.** List
- **B.** Dictionary
- **C.** Tuple
- **D.** Set

**Correct answer:** C
**Explanation:** Tuples are immutable — once created, their elements cannot be changed.
```

### Checklist

- ✅ Exam title starts with `# Exam Title: `
- ✅ Module/section headers use `## Module: `
- ✅ Questions use `### Q1`, `### Q2`, etc.
- ✅ Each question has exactly 4 options (A, B, C, D)
- ✅ Each question has a `**Correct answer:**` line (A, B, C, or D)
- ✅ Explanations are optional but recommended
- ✅ Save the file as `.md` or `.txt`
- ❌ Don't use HTML tags in questions
- ❌ Don't skip any required fields (4 options + correct answer)

---

## 5. Adding Exams to the Dashboard

### Method 1: Drag & Drop
1. Open the dashboard
2. Drag your `.md` or `.txt` file onto the drop zone
3. Exam appears in your library instantly

### Method 2: Click to Upload
1. Click **"+ Add Exam"**
2. Select your question file(s)
3. They appear in the library

### Method 3: Pre-bundled (Self-Hosting)
Place your `.md`/`.txt` file in the same folder as `exam-hub.html` and upload it via drag-drop or file picker.

**Tip:** You can upload multiple exam files. Each becomes a separate quiz card in your library.

---

## 6. Taking a Quiz

1. **Library view** — see all your exams as cards
2. Click **"Start Exam"** on any card
3. **Answer questions** — click an option to select it
4. **Instant feedback** — green = correct, red = wrong
5. **Explanation** appears below each answer
6. **Navigate** — use ← → arrows or progress dots at top
7. **Flag questions** — click ⚑ to mark for review
8. Click **"Finish Exam"** when done

### After Finishing

- **Score card**: Total questions, Attempted, Correct, Wrong, Unattempted, Score %
- **Domain breakdown**: Performance per topic/module
- **Practice Again**: Retake the full exam
- **Practice Wrong Only**: Focus only on questions you missed
- **View All**: Review all questions and answers

---

## 7. Managing Your Exams

### Deleting
- Hover over any exam card → click **🗑️** → confirm deletion
- ⚠️ Permanent — cannot be undone

### Exam Order
Exams auto-sort: **Unattempted → In Progress → Completed**

### Multiple Exams
Upload as many question files as you want. Each file becomes a separate exam card.

---

## 8. Features Explained

### Progress Dots
The row of dots during an exam:
- ⬜ Empty = Not answered yet
- 🟩 Green = Answered correctly
- 🟥 Red = Answered incorrectly
- ⚑ Flagged = Marked for later review

### Practice Wrong Answers Only
After completing an exam, click **"Practice Wrong Only"** to:
- Retake only the questions you got wrong
- Focus on your weak areas
- Track improvement

### Autosave / Session Resume
If you close the browser mid-exam, your progress is saved. When you return:
- Your answers are remembered
- Your flagged questions are remembered
- You'll see **"Resume Exam?"** with Resume/Reset options

### Dark/Light Theme
Toggle with the **🌙 / ☀️** button (top-right). Saves automatically.

---

## 9. Troubleshooting

### "Questions won't load after uploading"
- Verify each question has exactly 4 options (A, B, C, D)
- Check the `**Correct answer:**` line matches one of the options
- Open browser console (F12) for error messages

### "Exam won't parse correctly"
- Make sure the file is `.md` or `.txt` (not `.docx` or `.pdf`)
- Check that question headers use `### Q1` format (three hashes)
- Ensure no HTML tags in the file

### "My progress is gone"
- Clearing browser data removes localStorage
- Data doesn't sync across browsers or devices
- Export feature is not available yet

### "I want to share my questions"
- Your `.md`/`.txt` files can be shared with anyone
- They just need to upload them to their own dashboard
- The question files are completely independent of the app

---

## 📁 File Structure

```
exam-quiz-dashboard/
├── exam-hub.html          ← Main dashboard (open this!)
├── index.html             ← Auto-redirects to exam-hub.html
├── exam_format_guide.md   ← Quick format reference
├── TUTORIAL.md            ← This file
├── README.md              ← Project overview
├── LICENSE                ← MIT License
├── .gitignore             ← Git ignore rules
└── tools/                 ← Python utilities (optional)
```

---

*Built for learners, educators, and anyone who learns by testing themselves.*
