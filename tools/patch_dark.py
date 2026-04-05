import re

html_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\ai900-dashboard.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Tailwind config
text = text.replace(
    "tailwind.config = {", 
    "tailwind.config = {\n            darkMode: 'class',"
)

# 2. Update CSS logic
text = text.replace("background-color: #f8fafc; /* slate-50 */", "/* background-color: #f8fafc; Removed for dark mode */")

# 3. Add dark mode classes
# Text colors
text = text.replace('text-slate-800', 'text-slate-800 dark:text-slate-100')
text = text.replace('text-slate-700', 'text-slate-700 dark:text-slate-200')
text = text.replace('text-slate-600', 'text-slate-600 dark:text-slate-300')
text = text.replace('text-slate-500', 'text-slate-500 dark:text-slate-400')
# Background colors
text = text.replace('bg-white', 'bg-white dark:bg-slate-800 transition-colors')
text = text.replace('bg-slate-50', 'bg-slate-50 dark:bg-slate-900 transition-colors')
text = text.replace('bg-slate-100', 'bg-slate-100 dark:bg-slate-700 transition-colors')
# Border colors
text = text.replace('border-slate-200', 'border-slate-200 dark:border-slate-700')
text = text.replace('border-slate-100', 'border-slate-100 dark:border-slate-700')
# Body Base
text = text.replace('<body class="', '<body class="bg-slate-50 dark:bg-slate-900 ')

# 4. Inject Theme Toggle HTML into the Header
# Find <header> and insert toggle
toggle_html = '''
            <div class="flex items-center gap-3">
                <button id="theme-toggle" class="w-10 h-10 rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 dark:text-slate-400 dark:hover:bg-slate-700 transition-colors focus:outline-none shadow-sm">
                    <i class="fa-solid fa-moon text-lg dark:hidden"></i>
                    <i class="fa-solid fa-sun text-lg hidden dark:block"></i>
                </button>
            </div>
'''
# We inject right before the flag button, or just append it to the header flex. The current header has 2 children: the left section and the flag button.
header_search = r'(<header class="[^"]*?flex items-center justify-between[^"]*?">\s*<div class="flex items-center gap-4">.*?</div>)'
header_replace = r'\1\n            <div class="flex items-center gap-3">\n                <button id="theme-toggle" class="w-9 h-9 rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 dark:text-slate-400 dark:hover:bg-slate-700 transition-colors focus:outline-none">\n                    <i class="fa-solid fa-moon text-lg dark:hidden"></i>\n                    <i class="fa-solid fa-sun text-lg hidden dark:block"></i>\n                </button>'
text = re.sub(header_search, header_replace, text, flags=re.DOTALL)

# Wait, if flag-btn is there, we need to wrap it or put it adjacent.
# Let's see: original had <button id="flag-btn"...
# So the regex `(<header...</div>)` matches the first div and puts the new div after it. That means the flag button comes next. That's fine!

# 5. Inject Dark Mode JS Toggle Logic
js_inject = '''
        /*******************************************************
         * INITIALIZATION & DARK MODE
         *******************************************************/
        const themeBtn = document.getElementById('theme-toggle');
        // Check local storage
        if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }

        themeBtn.addEventListener('click', () => {
            document.documentElement.classList.toggle('dark');
            if (document.documentElement.classList.contains('dark')) {
                localStorage.theme = 'dark';
            } else {
                localStorage.theme = 'light';
            }
        });
'''
text = text.replace('        function initApp() {', js_inject + '\n        function initApp() {')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Dark Mode injected")
