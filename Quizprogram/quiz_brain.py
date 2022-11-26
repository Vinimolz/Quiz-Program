class Brain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_counter = 0
        self.has_questions = True
        self.user_score = 0

    def still_has_questions(self):
        if len(self.question_list) > self.question_counter:
            self.has_questions = True
            return self.has_questions
        else:
            self.has_questions = False
            return self.has_questions

    def next_question(self):
        current_question = self.question_list[self.question_counter]
        self.question_counter += 1

        user_answer = input(f"Q.{self.question_counter}: {current_question.text} (True or False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_question_answer):
        if user_answer == current_question_answer:
            print("That is right")
            self.user_score += 1
            print(f"Your current score is: {self.user_score}/{self.question_counter}\n")
        else:
            print("that is wrong")
            print(f"The correct answer was: {current_question_answer}")
            print(f"Your current score is: {self.user_score}/{self.question_counter}\n")