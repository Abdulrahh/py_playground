# python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animals lays the largest egg?: ",
             "Whats is the most abundant gas in the earth's atmosphere?: ",
             "How many bones are the human body?: ",
             "Which planets solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0

questions_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for  option in options[questions_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[questions_num]} is the correct answer")
    questions_num += 1
print("----------------------------")
print("         RESULT             ")
print("----------------------------")

print("answers:", end="")
for answer in answers:
    print(answer, end="")
print()
print("guesses:", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(F"Your Score is: {score}%")