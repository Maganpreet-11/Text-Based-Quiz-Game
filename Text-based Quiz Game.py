print("Welcome to the game!\n""We ask you 5 Questions\n""Your have 4 options\n""1 point for each correct answer\n")
start = input("Start the game(yes/no): " )
score = 0
if start == 'yes':
    print("Lets start the game!\n")
elif start == 'no':
    print("NO worries!")
    exit()
else:
    print("Invalid Input")
    exit()  

print("Question 1: Which planet is known as the Red Planet?\n""A) Earth\n""B) Mars\n""C) Jupiter\n""D) Venus")
Answer1 = input("Enter the answer(A,B,C,D): ").upper()
if Answer1 == 'B':
    score = score + 1
    print("Correct answer")
else:
    print("Wrong answer. Correct answer is B")
print("\n")
print("Question 2: What is the largest mammal in the world?\n""A) African Elephant\n""B) Blue Whale\n""C) Giraffe\n""D) Orca")
Answer2 = input("Enter the answer(A,B,C,D): ").upper()
if Answer2 == 'B':
    score = score + 1
    print("Correct answer")
else:
    print("Wrong answer. Correct answer is B")
print("\n")
print("Question 3: Who wrote the play Romeo and Juliet?\n""A) Charles Dickens\n""B) William Shakespeare\n""C) Jane Austen\n""D) Mark Twain")
Answer3 = input("Enter the answer(A,B,C,D): ").upper()
if Answer3 == 'B':
    score = score + 1
    print("Correct answer")
else:
    print("Wrong answer. Correct answer is B")
print("\n")
print("Question 4: What is the chemical symbol for water?\n""A) H2O\n""B) CO2\n""C) O2\n""D) NaCl")
Answer4 = input("Enter the answer(A,B,C,D): ").upper()
if Answer4 == 'A':
    score = score + 1
    print("Correct answer")
else:
    print("Wrong answer. Correct answer is A")
print("\n")
print("Question 5: Which continent is the Sahara Desert located in?\n""A) Asia\n""B) Africa\n""C) Australia\n""D) South America")
Answer5 = input("Enter the answer(A,B,C,D): ").upper()
if Answer5 == 'B':
    score = score + 1
    print("Correct answer")
else:
    print("Wrong answer. Correct answer is B")
print("\n")
print("Final Result:",score)
if score == 5:
    print("Excellent")
elif score == 3 or score == 4:
    print("Good")
elif score == 1 or score == 2:
    print("Needs Improvement")
else:
    print("Better luck next time")            