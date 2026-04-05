import re
import traceback

html_path = r"c:\Users\natar\OneDrive\Desktop\AI-900\ai900-dashboard.html"
try:
    with open(html_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Timer Display span removal
    text = re.sub(
        r'<div class="flex items-center gap-3 lg:gap-4">\s*<div class="flex items-center gap-2 bg-slate-100 px-3 py-1\.5 rounded-lg border border-slate-200 text-slate-700 font-bold shadow-inner">\s*<i class="fa-regular fa-clock text-azure-600"></i>\s*<span id="timer-display" class="tracking-wider">.*?</span>\s*</div>',
        '<div class="flex items-center gap-4">', text
    )

    # 2. Review Flagged Btn
    text = re.sub(
        r'<button id="review-flagged-btn"[\s\S]*?</button>', '', text
    )

    # 3. Modal HTML
    text = re.sub(
        r'<!-- Exam Complete Modal -->[\s\S]*?<!-- Single File Vanilla JavaScript Application Logic -->',
        '<!-- Single File Vanilla JavaScript Application Logic -->', text
    )

    # 4. Timer/State variables
    text = re.sub(r'let timeRemaining = 3600; // 60 minutes\s*let timerInterval = null;\s*let examFinished = false;', '', text)

    # 5. Timer/State functions
    text = re.sub(r'function saveState\(\) \{[\s\S]*?try \{ localStorage\.setItem\(\'ai900_state\', JSON\.stringify\(state\)\); \} catch\(e\)\{\}\s*\}', '', text)
    text = re.sub(r'function loadState\(\) \{[\s\S]*?return false;\s*\}', '', text)
    text = re.sub(r'function formatTime\(\w+\) \{[\s\S]*?return `.*?\`;\s*\}', '', text)
    text = re.sub(r'function startTimer\(\) \{[\s\S]*?,\s*1000\);\s*\}', '', text)
    text = re.sub(r'function finishExam\(\w*\) \{[\s\S]*?\}', '', text)
    
    # 5.1 Remove "STATE PERSISTENCE & TIMERS" comment box
    text = re.sub(r'/\*{50,}\s*\* STATE PERSISTENCE & TIMERS\s*\*{50,}/', '', text)

    # 6. initApp function rewrite
    initApp_clean = '''        function initApp() {
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
        }'''
    text = re.sub(r'function initApp\(\) \{[\s\S]*?finishExam\(true\);\s*\}', initApp_clean, text)

    # 7. Clean action bindings (extractSubPractice, reviewFlagged, modal button clicks)
    practice_wrong_clean = '''        els.practiceWrongBtn.addEventListener('click', () => {
            let wrongQIDs = [];
            for (let [qId, data] of userAnswers.entries()) {
                if (!data.isCorrect) wrongQIDs.push(qId);
            }
            if (wrongQIDs.length === 0) {
                alert("You don't have any wrong answers to practice!");
                return;
            }
            
            if(confirm('This will create a new practice session with only your ' + wrongQIDs.length + ' wrong answers. Proceed?')) {
                let newQuestions = questions.filter(q => wrongQIDs.includes(q.id));
                newQuestions.forEach(q => {
                    q.options = shuffleArray(q.options);
                });
                questions = shuffleArray(newQuestions);
                
                userAnswers.clear();
                flaggedQuestions.clear();
                correctCount = 0;
                wrongCount = 0;
                currentIndex = 0;
                
                Object.values(DOMAINS).forEach(d => {
                    domainsTracking[d].correct = 0;
                    domainsTracking[d].attempted = 0;
                    domainsTracking[d].total = 0;
                });
                
                questions.forEach(q => {
                     domainsTracking[q.domain].total += 1;
                });
                
                renderSidebar();
                renderPaginationDots();
                renderQuestion();
                els.practiceWrongBtn.classList.add('hidden');
            }
        });'''
        
    text = re.sub(r'function extractSubPractice\(.*?\) \{[\s\S]*?els\.closeModalBtn\.addEventListener.*?hidden\'\)\);', practice_wrong_clean, text)
    
    # 8. Extra cleanup of els practiceWrongBtn block
    text = re.sub(r'els\.practiceWrongBtn\.addEventListener\(\'click\'.*?els\.practiceWrongBtn\.addEventListener\(\'click\'', "els.practiceWrongBtn.addEventListener('click'", text, flags=re.DOTALL)

    # Overwrite
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Done")
except Exception as e:
    print(traceback.format_exc())
