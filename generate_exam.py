import sys
import re
import json
import os

def parse_markdown(md_text):
    exam_title = "Practice Exam"
    domains = {}
    questions = []
    
    current_domain = "General"
    
    # State flags
    current_q_text = None
    current_options = []
    current_answer = None
    current_explanation = None
    
    lines = md_text.split('\n')
    
    def save_question():
        nonlocal current_q_text, current_options, current_answer, current_explanation
        if current_q_text:
            # Map answer letter/text to index
            ans_idx = 0
            clean_ans = current_answer.strip() if current_answer else ""
            
            # If answer is just a letter like 'B'
            if len(clean_ans) == 1 and clean_ans.isalpha():
                ans_idx = ord(clean_ans.upper()) - 65
            else:
                # Try to find matching option text
                for i, opt in enumerate(current_options):
                    if clean_ans.lower() in opt.lower():
                        ans_idx = i
                        break

            # Safety fallback for index
            if ans_idx < 0 or ans_idx >= len(current_options):
                ans_idx = 0

            # Clean up the actual options to remove "A) ", "B. ", etc.
            clean_options = []
            for opt in current_options:
                opt_clean = re.sub(r'^[A-Za-z][\)\.]\s*', '', opt).strip()
                clean_options.append(opt_clean)

            # Generate default explanation if missing
            exp = current_explanation if current_explanation else "No explanation provided."

            questions.append({
                "domain": current_domain,
                "text": current_q_text.strip(),
                "options": clean_options,
                "answer": ans_idx,
                "explanation": exp.strip()
            })
            
        current_q_text = None
        current_options = []
        current_answer = None
        current_explanation = None

    state = "NONE"

    for line in lines:
        line_s = line.strip()
        if not line_s:
            continue
        
        # 1. Title
        title_m = re.match(r'^#\s+(.*)', line_s)
        if title_m:
            exam_title = title_m.group(1).strip()
            continue
            
        # 2. Domain
        domain_m = re.match(r'^##\s+(.*)', line_s)
        if domain_m:
            raw_d = domain_m.group(1).strip()
            key = f"D{len(domains) + 1}"
            domains[key] = raw_d
            current_domain = f"DOMAINS.{key}"
            continue
            
        # 3. Question
        # Match "**Question 1:** text", "Question 1: text", "1. text", "1. **Question:** text"
        q_m = re.match(r'^(?:\*\*)?Question(?: \d+)?:(?:\*\*)?\s*(.*)', line_s, flags=re.IGNORECASE)
        if not q_m:
            q_m = re.match(r'^\d+\.\s+(?:\*\*)?(?:Question:?\s*)?(?:\*\*)?\s*(.*)', line_s, flags=re.IGNORECASE)
            
        if q_m:
            save_question()
            current_q_text = q_m.group(1)
            state = "Q"
            continue
            
        # 4. Answer
        a_m = re.match(r'^(?:\*\*)?Answer:(?:\*\*)?\s*(.*)', line_s, flags=re.IGNORECASE)
        if a_m:
            current_answer = a_m.group(1)
            state = "A"
            continue
            
        # 5. Explanation
        e_m = re.match(r'^(?:\*\*)?Explanation:(?:\*\*)?\s*(.*)', line_s, flags=re.IGNORECASE)
        if e_m:
            current_explanation = e_m.group(1)
            state = "E"
            continue
            
        # Options or Multi-line continuations
        if state == "Q":
            # Match list item: "- A) Option" or "* Option"
            opt_m = re.match(r'^[\-\*]\s+(.*)', line_s)
            if opt_m:
                current_options.append(opt_m.group(1))
            else:
                # Match lettered option without dash: "A) Option"
                opt_m2 = re.match(r'^[A-E][\)\.]\s+(.*)', line_s)
                if opt_m2:
                    current_options.append(line_s.strip())
                else:
                    # Continuation of question text
                    if not current_options:
                        current_q_text += " " + line_s

        elif state == "E":
            current_explanation += " " + line_s
            
    # Save the last question
    save_question()

    # Default domain fallback
    if not domains:
        domains["D1"] = "General Topics"
        for q in questions:
            q["domain"] = "DOMAINS.D1"

    # Stringify DOMAINS_JS
    domains_js_lines = []
    for k, v in domains.items():
        domains_js_lines.append(f'"{k}": "{v}"')
    domains_js = '{ ' + ', '.join(domains_js_lines) + ' }'
    
    # Stringify QUESTIONS_JS
    formatted_questions = []
    for q in questions:
        formatted_questions.append(f"""            {{ domain: {q['domain']}, text: {json.dumps(q['text'])}, options: {json.dumps(q['options'])}, answer: {q['answer']}, explanation: {json.dumps(q['explanation'])} }}""")
    questions_js = "[\n" + ",\n".join(formatted_questions) + "\n        ]"
    
    return exam_title, domains_js, questions_js


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_exam.py <input.md> [output.html]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        base = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"{base}-dashboard.html"
        
    template_path = "exam-template.html"
    if not os.path.exists(template_path):
        template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exam-template.html")
        if not os.path.exists(template_path):
            print("Error: exam-template.html not found.")
            sys.exit(1)

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            md_text = f.read()
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        sys.exit(1)
        
    exam_title, domains_js, questions_js = parse_markdown(md_text)
    
    print(f"Parsed Exam Title: {exam_title}")
    q_count = len(questions_js.split('domain:')) - 1
    print(f"Extracted {q_count} questions.")
    
    if q_count == 0:
        print("Warning: 0 questions extracted. Please check the formatting against exam_format_guide.md.")

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    html = html.replace("{{EXAM_TITLE}}", exam_title)
    html = html.replace("{{DOMAINS_JS}}", domains_js)
    html = html.replace("{{QUESTIONS_JS}}", questions_js)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Successfully generated: {output_file}")

if __name__ == "__main__":
    main()
