import re

html_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\ai900-dashboard.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

modal_html = """
    <!-- Exam Complete Modal -->
    <div id="exam-complete-modal" class="hidden fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4 transition-opacity">
        <div class="bg-white dark:bg-slate-800 rounded-2xl shadow-xl w-full max-w-lg p-8 relative transform scale-95 transition-transform duration-300">
            <div class="absolute top-4 right-4 cursor-pointer text-slate-400 hover:text-slate-600 dark:hover:text-slate-200" id="close-modal-btn">
                <i class="fa-solid fa-xmark text-xl"></i>
            </div>
            <div class="text-center mb-6">
                <div class="w-16 h-16 bg-azure-100 dark:bg-azure-900 border border-azure-200 dark:border-azure-700 text-azure-600 dark:text-azure-400 rounded-full flex items-center justify-center text-3xl mx-auto mb-4 bg-gradient-to-br from-azure-100 to-azure-200 shadow-sm">
                    <i class="fa-solid fa-trophy"></i>
                </div>
                <h2 class="text-2xl font-bold text-slate-800 dark:text-slate-100">Exam Complete!</h2>
                <p class="text-slate-500 dark:text-slate-400 mt-1">Here is how you performed.</p>
            </div>
            
            <div class="bg-slate-50 dark:bg-slate-900/50 rounded-xl p-6 border border-slate-200 dark:border-slate-700 mb-6 flex flex-col items-center shadow-inner">
                <div class="text-4xl font-black text-slate-800 dark:text-white" id="modal-score">0 / 1000</div>
                <div class="text-sm font-semibold mt-1" id="modal-status">Pending</div>
            </div>
            
            <button id="modal-practice-wrong" class="w-full py-2.5 px-4 bg-red-50 dark:bg-red-400/10 text-red-600 dark:text-red-400 border border-red-200 dark:border-red-500/30 font-semibold rounded-lg hover:bg-red-100 dark:hover:bg-red-400/20 transition disabled:opacity-50 disabled:cursor-not-allowed">
                <i class="fa-solid fa-bullseye"></i> Practice Wrong Questions
            </button>
        </div>
    </div>
"""

# Inject Modal HTML before Single File Vanilla JavaScript
text = text.replace('    <!-- Single File Vanilla JavaScript Application Logic -->', modal_html + '\n    <!-- Single File Vanilla JavaScript Application Logic -->')

# Inject fields into `els`
els_old = """            paginationDots: document.getElementById('pagination-dots'),
            resetBtn: document.getElementById('reset-btn'),
            practiceWrongBtn: document.getElementById('practice-wrong-btn')
        };"""

els_new = """            paginationDots: document.getElementById('pagination-dots'),
            resetBtn: document.getElementById('reset-btn'),
            practiceWrongBtn: document.getElementById('practice-wrong-btn'),
            examModal: document.getElementById('exam-complete-modal'),
            modalScore: document.getElementById('modal-score'),
            modalStatus: document.getElementById('modal-status'),
            modalBtnWrong: document.getElementById('modal-practice-wrong'),
            closeModalBtn: document.getElementById('close-modal-btn')
        };"""
text = text.replace(els_old, els_new)

# Inject finishExam method before function initApp()
js_modal = """
        function finishExam() {
            let score = questions.length > 0 ? Math.round((correctCount / questions.length) * 1000) : 0;
            if(els.modalScore) els.modalScore.textContent = score + ' / 1000';
            
            if (els.modalStatus) {
                if(score >= 700) {
                    els.modalStatus.textContent = "Pass";
                    els.modalStatus.className = "text-xl font-bold mt-1 text-green-600 dark:text-green-500";
                } else {
                    els.modalStatus.textContent = "Fail";
                    els.modalStatus.className = "text-xl font-bold mt-1 text-red-600 dark:text-red-500";
                }
            }
            
            if(els.modalBtnWrong) els.modalBtnWrong.disabled = (wrongCount === 0);
            
            if(els.examModal) {
                els.examModal.classList.remove('hidden');
                setTimeout(() => {
                    els.examModal.firstElementChild.classList.remove('scale-95');
                    els.examModal.firstElementChild.classList.add('scale-100');
                }, 10);
            }
        }
"""
text = text.replace('        function initApp() {', js_modal + '\n        function initApp() {')

# Inject auto finishExam inside selectOption
text = text.replace(
    "els.expBox.classList.add('animate-slide-down');\n            saveState();\n        }",
    "els.expBox.classList.add('animate-slide-down');\n            saveState();\n            if (userAnswers.size === questions.length) { setTimeout(() => finishExam(), 800); }\n        }"
)

# Inject modal listeners
listeners_inject = """
        if(els.modalBtnWrong) els.modalBtnWrong.addEventListener('click', () => { els.examModal.classList.add('hidden'); els.practiceWrongBtn.click(); });
        if(els.closeModalBtn) els.closeModalBtn.addEventListener('click', () => els.examModal.classList.add('hidden'));

        // Setup Keyboard Navigation
"""
text = text.replace('        // Setup Keyboard Navigation', listeners_inject)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Modal injected")
