import re
import json

file_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\AI-900.txt"
html_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\ai900-dashboard.html"

# Ensure mapping matches the DOMAINS in HTML
DOMAINS = {
    "Domain 1": "AI Workloads & Concepts",
    "Domain 2": "Machine Learning Concepts",
    "Domain 3": "Computer Vision Workloads",
    "Domain 4": "Natural Language Processing",
    "Domain 5": "Conversational AI Workloads"
}

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

questions = []
current_domain_key = None
seen_questions = set()

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Check for domain header
    if line.startswith("Domain "):
        # e.g. "Domain 1: AI Workloads and Responsible AI"
        m = re.match(r"(Domain \d+)", line)
        if m:
            current_domain_key = m.group(1)
        continue
    
    # Check for question line
    # Format: 1. Question: [text] Answer: [text]. ([explanation]).
    m = re.match(r"^\d+\.\s*Question:\s*(.*?)\s*Answer:\s*(.*?)\.\s*\((.*?)\)\.?$", line)
    
    # Sometimes there is no period before the parenthesis, or the parenthesis is missing
    if not m:
        m = re.match(r"^\d+\.\s*Question:\s*(.*?)\s*Answer:\s*(.*?)\s*\((.*?)\)\.?$", line)
    if not m:
        m = re.match(r"^\d+\.\s*Question:\s*(.*?)\s*Answer:\s*(.*?)$", line)
        if m:
            q_text = m.group(1)
            a_text = m.group(2)
            exp_text = "No explanation provided."
        else:
            print("Failed to parse:", line)
            continue
    else:
        q_text = m.group(1)
        a_text = m.group(2)
        exp_text = m.group(3)
        
    # Deduplicate
    q_lower = q_text.lower().strip()
    if q_lower in seen_questions:
        continue
    seen_questions.add(q_lower)
    
    domain_val = DOMAINS.get(current_domain_key, "AI Workloads & Concepts")
    
    questions.append({
        "domain": domain_val,
        "text": q_text,
        "answer": a_text,
        "explanation": exp_text
    })

print(f"Extracted {len(questions)} unique questions.")

# Generate distractors
import random

# Collect all answers per domain to use as distractors
domain_answers = {}
for q in questions:
    domain_answers.setdefault(q["domain"], []).append(q["answer"])

formatted_questions = []

# Generic distractors in case a domain doesn't have enough answers
generic_distractors = ["Computer Vision", "Anomaly Detection", "Azure Machine Learning", "Classification", "Regression", "Clustering", "Object Detection", "Optical Character Recognition", "Sentiment Analysis", "Named Entity Recognition", "Language Detection", "Azure Bot Service"]

for q in questions:
    correct = q["answer"]
    domain = q["domain"]
    
    # Get 3 other unique answers from the same domain
    pool = [a for a in domain_answers[domain] if a != correct]
    # Remove duplicates from pool
    pool = list(set(pool))
    
    distractors = []
    if len(pool) >= 3:
        distractors = random.sample(pool, 3)
    else:
        distractors = pool[:]
        while len(distractors) < 3:
            cand = random.choice(generic_distractors)
            if cand not in distractors and cand != correct:
                distractors.append(cand)
                
    options = [correct] + distractors
    # Randomize order
    random.shuffle(options)
    correct_idx = options.index(correct)
    
    # Determine the DOMAIN key to inject into JS (e.g., DOMAINS.WORKLOADS)
    domain_var = ""
    for k, v in DOMAINS.items():
        if v == domain:
            if k == "Domain 1": domain_var = "DOMAINS.WORKLOADS"
            elif k == "Domain 2": domain_var = "DOMAINS.ML"
            elif k == "Domain 3": domain_var = "DOMAINS.VISION"
            elif k == "Domain 4": domain_var = "DOMAINS.NLP"
            elif k == "Domain 5": domain_var = "DOMAINS.BOT"
            break
            
    formatted_questions.append(f"""            {{ domain: {domain_var}, text: {json.dumps(q['text'])}, options: {json.dumps(options)}, answer: {correct_idx}, explanation: {json.dumps(q['explanation'])} }}""")

js_array_str = "[\n" + ",\n".join(formatted_questions) + "\n        ]"

# Now read the HTML file and replace the rawQuestions array
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace the array
pattern = re.compile(r"const rawQuestions = \[\s*// Domain 1.*?\n        \];", re.DOTALL)
new_html = pattern.sub(lambda _: f"const rawQuestions = {js_array_str};", html_content)

if new_html == html_content:
    print("Warning: regex for rawQuestions replacement didn't match anything. Looking for generic array.")
    pattern2 = re.compile(r"const rawQuestions = \[.*?\];", re.DOTALL)
    new_html = pattern2.sub(lambda _: f"const rawQuestions = {js_array_str};", html_content)

# Fix hardcoded "40" in the HTML spanning multiple exact matches
new_html = new_html.replace('of 40</span>', f'of {len(questions)}</span>')
new_html = new_html.replace('0 / 40</span>', f'0 / {len(questions)}</span>')
new_html = new_html.replace('1</span> of 40', f'1</span> of {len(questions)}')

# Verify we also replace "Domain Loading..." just in case
new_html = new_html.replace('Domain Loading...', 'Domain')

# We also should ensure the JS updates total-q-count dynamically
with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Successfully updated HTML with {len(questions)} questions.")
