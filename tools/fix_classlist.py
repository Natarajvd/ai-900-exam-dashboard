import re

html_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\ai900-dashboard.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

fixes = [
    ("'bg-white dark:bg-slate-800 transition-colors'", "'bg-white', 'dark:bg-slate-800', 'transition-colors'"),
    ("'bg-slate-50 dark:bg-slate-900 transition-colors'", "'bg-slate-50', 'dark:bg-slate-900', 'transition-colors'"),
    ("'bg-slate-100 dark:bg-slate-700 transition-colors'", "'bg-slate-100', 'dark:bg-slate-700', 'transition-colors'"),
    ("'border-slate-200 dark:border-slate-700'", "'border-slate-200', 'dark:border-slate-700'"),
    ("'border-slate-100 dark:border-slate-700'", "'border-slate-100', 'dark:border-slate-700'"),
    ("'text-slate-800 dark:text-slate-100'", "'text-slate-800', 'dark:text-slate-100'"),
    ("'text-slate-700 dark:text-slate-200'", "'text-slate-700', 'dark:text-slate-200'"),
    ("'text-slate-600 dark:text-slate-300'", "'text-slate-600', 'dark:text-slate-300'"),
    ("'text-slate-500 dark:text-slate-400'", "'text-slate-500', 'dark:text-slate-400'")
]

for bad, good in fixes:
    text = text.replace(bad, good)
    
# Also check for double quotes just in case
for bad, good in fixes:
    bad_dq = bad.replace("'", '"')
    good_dq = good.replace("'", '"')
    text = text.replace(bad_dq, good_dq)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed classList spaces in JS.")
