class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(current_question.answer, user_answer )

    def check_answer(self, correct_answer, user_answer ):
        if correct_answer.lower() == user_answer.lower():
            print("got it")
            self.score += 1
        else:
            print("wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Currect score: {self.score}/{self.question_number}")
        print("\n")