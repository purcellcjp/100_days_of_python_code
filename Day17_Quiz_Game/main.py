from question_model import Question
from data import question_data2
from quiz_brain import QuizBrain

question_bank = []

# for itm in question_data:
#     new_q = Question(itm['text'], itm['answer'])
#     question_bank.append(new_q)

for itm in question_data2:
    new_q = Question(itm['question'], itm['correct_answer'])
    question_bank.append(new_q)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You\'ve completed the quiz!!!')
print(f'Your final score is: {quiz.score}/{quiz.question_number}')
