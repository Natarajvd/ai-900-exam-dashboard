import re

html_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\ai900-dashboard.html"
template_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\exam-template.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace Titles
html = html.replace("<title>AI-900 Practice Dashboard</title>", "<title>{{EXAM_TITLE}} Dashboard</title>")
html = html.replace("AI-900 Prep", "{{EXAM_TITLE}}")
html = html.replace("Loading your AI-900 practice question...", "Loading your practice question...")

# Replace DOMAINS object
domain_pattern = re.compile(r"const DOMAINS = \{.*?\};", re.DOTALL)
html = domain_pattern.sub("const DOMAINS = {{DOMAINS_JS}};", html)

# Replace rawQuestions array
questions_pattern = re.compile(r"const rawQuestions = \[.*?\];", re.DOTALL)
html = questions_pattern.sub("const rawQuestions = {{QUESTIONS_JS}};", html)

# Fix specific count references, e.g. "of 90", "0 / 90" -> this happens dynamically now
# Let's clean up any hardcoded 90 since we want it completely dynamic.
# Wait, the JS updates it dynamically anyway, but initial HTML has 90. We should leave it as is, or replace with {{QUESTION_COUNT}}.
# Actually, the JS `els.qTotal.textContent = questions.length;` will override it. So it's fine.

with open(template_path, "w", encoding="utf-8") as f:
    f.write(html)

print("exam-template.html created successfully.")
