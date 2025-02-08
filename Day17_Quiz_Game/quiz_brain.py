class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(
            f'Q.{self.question_number}: {cur_question.text} (True/False)?: '
        )
        self.check_answer(response, cur_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Correct!!!')
            # update correct answer score
            self.score += 1

        else:
            print('Wrong!!!')

        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')
