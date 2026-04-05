# AI-900 Practice Exam Dashboard

An interactive, web-based dashboard designed to help you prepare for the Microsoft Azure AI Fundamentals (AI-900) exam. This application reads question banks stored in Markdown (`.md`) or text (`.txt`) formats and presents them in an easy-to-use, interactive quiz interface with immediate feedback.

## Features

- Parse standard text and Markdown files for questions.
- Built-in support for Udemy exam export formats.
- Interactive web UI built with HTML, CSS, and Vanilla JavaScript.
- Clean, responsive design with Dark/Light modes.
- Session autosaving allows you to resume progress later.

## Getting Started

1. Clone or download this repository.
2. Place your question bank files (e.g., `AI-900.txt`, `Udemy-AI-900-1.md`) in the root directory. 
   *(Note: Question bank `.txt` and `.md` files are excluded in `.gitignore` by default to prevent accidental uploading of copyrighted exam materials.)*
3. Open `exam-hub.html` or `ai900-dashboard.html` in your web browser. No local web server is required for basic usage.

## Question Formatting

To learn how to format your own question banks so the dashboard can parse them properly, please consult the [`exam_format_guide.md`](exam_format_guide.md) file included in this repository.

## Utilities

A `tools/` folder contains Python scripts that can generate HTML from templates, fix formatting, and apply bulk patches to your local dashboard:
- `generate_exam.py`
- `patch_*.py`
- `fix_classlist.py`

*(Note: You'll require Python 3 if you wish to run these builder/utility scripts.)*

## License

This project is licensed under the MIT License - see the LICENSE file for details.
