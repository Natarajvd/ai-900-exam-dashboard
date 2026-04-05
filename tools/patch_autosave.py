import re

html_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\ai900-dashboard.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

state_functions = """
        function saveState() {
            const state = {
                questions, currentIndex, correctCount, wrongCount,
                userAnswersArray: Array.from(userAnswers.entries()),
                flaggedArray: Array.from(flaggedQuestions),
                domainsTracking
            };
            try { localStorage.setItem('ai900_state_v2', JSON.stringify(state)); } catch(e){}
        }

        function loadState() {
            try {
                const s = localStorage.getItem('ai900_state_v2');
                if (s) {
                    const state = JSON.parse(s);
                    if (!state || !state.questions || state.questions.length === 0 || !state.domainsTracking) return false;
                    
                    questions = state.questions;
                    currentIndex = state.currentIndex || 0;
                    correctCount = state.correctCount || 0;
                    wrongCount = state.wrongCount || 0;
                    userAnswers = new Map(state.userAnswersArray || []);
                    flaggedQuestions = new Set(state.flaggedArray || []);
                    domainsTracking = state.domainsTracking;
                    return true;
                }
            } catch(e){}
            return false;
        }
"""

# Replace in `function initApp()`
initApp_old = """function initApp() {
            Object.values(DOMAINS).forEach(d => {
                domainsTracking[d] = { total: 0, correct: 0, attempted: 0 };
            });

            questions = buildQuestionBank(rawQuestions);
            
            questions.forEach(q => {
                 domainsTracking[q.domain].total += 1;
            });

            renderSidebar();
            renderPaginationDots();
            renderQuestion();
        }"""
        
initApp_new = """function initApp() {
            if (!loadState()) {
                Object.values(DOMAINS).forEach(d => {
                    domainsTracking[d] = { total: 0, correct: 0, attempted: 0 };
                });

                questions = buildQuestionBank(rawQuestions);
                
                questions.forEach(q => {
                     domainsTracking[q.domain].total += 1;
                });
            }

            renderSidebar();
            renderPaginationDots();
            renderQuestion();
            
            if (wrongCount > 0 && els.practiceWrongBtn) els.practiceWrongBtn.classList.remove('hidden');
        }"""

text = text.replace(initApp_old, state_functions + "\n        " + initApp_new)

# Add saveState() to selectOption
text = text.replace(
    "els.expBox.classList.add('animate-slide-down');\n        }",
    "els.expBox.classList.add('animate-slide-down');\n            saveState();\n        }"
)

# Add saveState() to flagBtn listener
text = text.replace(
    "renderQuestion();\n        });",
    "renderQuestion();\n            saveState();\n        });"
)

# Replace local storage reset in resetBtn
text = text.replace(
    "if(confirm('Warning: This will clear all your practice progress and reload all questions. Proceed?')) {",
    "if(confirm('Warning: This will clear all your practice progress and reload all questions. Proceed?')) {\n                localStorage.removeItem('ai900_state_v2');"
)

# Similarly remove local storage in practice wrong reset
text = text.replace(
    "if(confirm('This will create a new practice session with only your ' + wrongQIDs.length + ' wrong answers. Proceed?')) {",
    "if(confirm('This will create a new practice session with only your ' + wrongQIDs.length + ' wrong answers. Proceed?')) {\n                localStorage.removeItem('ai900_state_v2');"
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Auto-save injected")
