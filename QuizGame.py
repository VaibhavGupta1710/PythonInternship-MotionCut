logo = """
 _____  _           _____       _         _____                  
|_   _|| |_  ___   |     | _ _ |_| ___   |   __| ___  _____  ___ 
  | |  |   || -_|  |  |  || | || ||- _|  |  |  || .'||     || -_|
  |_|  |_|_||___|  |__  _||___||_||___|  |_____||__,||_|_|_||___|
                      |__|                                       
"""

import random

# Initialize score
score = 0

def ques1():
    global score
    print("Brass gets discoloured in air because of the presence of which of the following gases in air?\n")
    print("a. Oxygen\nb. Nitrogen\nc. Hydrogen Sulphide\nd. Carbon Dioxide\n")
    ans1 = input("Enter your answer from a to d: ")
    if ans1 == "c":
        score += 20
        print("Correct Answer\n")
    else:
        print("Wrong Answer, the correct answer is c. Hydrogen Sulphide\n")
    return

def ques2():
    global score
    print("Which was the 1st non-Test playing country to beat India in an international match?\n")
    print("a. Canada\nb. Sri Lanka\nc. Zimbabwe\nd. East Africa\n")
    ans2 = input("Enter your answer from a to d: ")
    if ans2 == "b":
        score += 20
        print("Correct Answer\n")
    else:
        print("Wrong Answer, the correct answer is b. Sri Lanka\n")
    print("Sri Lanka got the status of Test playing country in 1981, and beat India in the 1979 World Cup. Before this they were champion of ICC non-test playing countries.\n")
    return

def ques3():
    global score
    print("The headquarters of the National Power Training Institute is located in?\n")
    print("a. Pune\nb. Bhopal\nc. Faridabad\nd. Lucknow\n")
    ans3 = input("Enter your answer from a to d: ")
    if ans3 == "c":
        score += 20
        print("Correct Answer\n")
    else:
        print("Wrong Answer, the correct answer is c. Faridabad\n")
    return

def ques4():
    global score
    print("Which of the following is the capital of Arunachal Pradesh?\n")
    print("a. Itanagar\nb. Dispur\nc. Imphal\nd. Panaji\n")
    ans4 = input("Enter your answer from a to d: ")
    if ans4 == "a":
        score += 20
        print("Correct Answer\n")
    else:
        print("Wrong Answer, the correct answer is a. Itanagar\n")
    return

def ques5():
    global score
    print("'OS' computer abbreviation usually means?\n")
    print("a. Order of Significance\nb. Open Software\nc. Operating System\nd. Optical Sensor\n")
    ans5 = input("Enter your answer from a to d: ")
    if ans5 == "c":
        score += 20
        print("Correct Answer\n")
    else:
        print("Wrong Answer, the correct answer is c. Operating System\n")
    return

def start_quiz():
    global score
    score = 0  # Reset score at the start of the quiz
    print("Let's start the quiz\n")
    q1 = ques1
    q2 = ques2
    q3 = ques3
    q4 = ques4
    q5 = ques5
    questions = [q1, q2, q3, q4, q5]
    random.shuffle(questions)
    q = [1, 2, 3, 4, 5]
    for i, j in zip(q, questions):
        print(f"Question {i}:")
        j()
    print(f"Your final score is: {score}\n")

def quiz():
    print(logo)
    stop_quiz = False
    while not stop_quiz:
        print("Welcome to the quiz\n")
        start = input("Do you want to start the quiz? (y/n): ")
        if start.lower() == "y":
            print("Let's start the quiz\n")
            start_quiz()
        elif start.lower() == "n":
            stop_quiz = True
            break
        else:
            print(logo)
            print("Invalid input")
            continue

        replay = input("Do you want to play again? (y/n): ")
        if replay.lower() == "n":
            stop_quiz = True
        elif replay.lower() == "y":
            print(logo)
        elif replay.lower() != "y":
            print("Invalid input, exiting.")
            stop_quiz = True



quiz()
