from data import question_data
from question_model import Question
from quiz_brain import Brain

print("IMPORTANT NOTE: Type answer as shown inside the parentheses.\n")

ready = input("Are you ready to the the quiz ? (Y/N) ")

if ready == "Y":
    print("Good Luck !!!\n")
    questions_bank = []

    for i in range(0, len(question_data)):
        question = Question(question_data[i]['text'], question_data[i]['answer'])
        questions_bank.append(question)

    user = Brain(questions_bank)

    while user.still_has_questions():
        user.next_question()

    print("You completed the quiz!")
    print(f"Your final score was: {user.user_score}/{user.question_counter}")
elif ready == "N":
    print("It is alright, but come back later")
else:
    print("I see you didn't red my note")






