# Improved Quiz Program - Multiple Choice Quiz

def run_quiz():
    print("\nWelcome to the Python Quiz Game!")
    print("Type the letter of the correct answer.\n")

    questions = [
        {
            "question": "1. What is the capital of Nigeria?",
            "options": ["A. Lagos", "B. Abuja", "C. Kano"],
            "answer": "b"
        },
        {
            "question": "2. Which language is this quiz written in?",
            "options": ["A. English", "B. Java", "C. Python"],
            "answer": "c"
        },
        {
            "question": "3. What does CPU stand for?",
            "options": ["A. Central Processing Unit", "B. Computer Power Unit", "C. Central Print Utility"],
            "answer": "a"
        },
        {
            "question": "4. Which one is a web browser?",
            "options": ["A. Chrome", "B. Windows", "C. WhatsApp"],
            "answer": "a"
        },
        {
            "question": "5. What symbol is used to write comments in Python?",
            "options": ["A. //", "B. #", "C. ?"],
            "answer": "b"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Your answer: ").lower()

        if user_answer == q["answer"]:
            print("Correct ✅\n")
            score += 1
        else:
            print("Wrong ❌\n")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print(f"Quiz Completed!")
    print(f"Your Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Outstanding! 🌟 Genius level!")
    elif percentage >= 60:
        print("Good job! 👍 Keep practicing!")
    else:
        print("Don't worry, keep learning! 💪")

# Loop to replay
while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Goodbye! Thanks for playing 😊")
        break
2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
