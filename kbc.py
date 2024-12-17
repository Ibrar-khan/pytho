

# Define questions and their correct answers
questions = [
    "What is the capital of India?",
    "Who is the author of 'To Kill a Mockingbird'?",
    "What is the chemical symbol for water?",
    "Which planet is known as the Red Planet?",
    "Who painted the Mona Lisa?",
]

answers = [
    ("New Delhi", "A"),
    ("Harper Lee", "B"),
    ("H2O", "C"),
    ("Mars", "D"),
    ("Leonardo da Vinci", "E"),
]

# Define prize amounts for each correct answer
prizes = [1000, 2000, 5000, 10000, 20000]

# Function to display questions and get user's answer
def play_game():
    total_prize = 0
    for i in range(len(questions)):
        print("Question", i+1, ":", questions[i])
        print("Options:")
        print("A. ", answers[i][0])
        print("B. ", answers[i][1])

        # Get user's answer

        user_answer = input("Your answer (A/B/C/D/E): ").upper()

        # Check if the answer is correct
        if user_answer == answers[i][1]:
            print("Correct Answer!")
            total_prize += prizes[i]
        else:
            print("Wrong Answer! The correct answer was", answers[i][1])

    return total_prize

# Main function
def main():
    print("Welcome to Kaun Banega Crorepati!")
    print("Answer the following questions to win prizes.")
    input("Press Enter to start...")

    # Play the game
    total_amount = play_game()

    print("Congratulations! You won Rs.", total_amount, "!")
    print("Thank you for playing.")

if __name__ == "__main__":
    main()
