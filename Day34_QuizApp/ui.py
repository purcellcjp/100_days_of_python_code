from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
WHITE = '#FFFFFF'
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quiz App')
        # self.window.minsize(width=350, height=800)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg=WHITE,
                                 font=(FONT_NAME, 10, 'normal'))
        self.score_label.grid(row=0, column=1)

        # Question Canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='[QUESTION]',
            fill=THEME_COLOR,
            font=(FONT_NAME, 16, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True button
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.answer_true
        )
        self.true_button.grid(row=2, column=0)

        # False Button
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.answer_false
        )
        self.false_button.grid(row=2, column=1)

        # Populate canvas text with first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text='You have reached the end of the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
