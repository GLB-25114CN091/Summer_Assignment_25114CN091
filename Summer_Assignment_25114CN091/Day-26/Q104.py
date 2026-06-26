def quiz_application():
    print(" Quiz Application ")
    questions = [
        {"q": "What is the capital of India?", "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"], "answer": "B"},
        {"q": "Which language is used for web apps?", "options": ["A. Python", "B. Java", "C. JavaScript", "D. All of the above"], "answer": "D"},
        {"q": "Where is Gl bajaj located?", "options": ["A. Haryana", "B. Goa", "C. Nodia", "D. Greater Nodia"], "answer": "D"}
    ]

    score = 0
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['q']}")
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print(f"\nYour final score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_application()
