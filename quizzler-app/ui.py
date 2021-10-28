from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.config(padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question.",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        self.correct_image = PhotoImage(file="images/true.png")
        self.wrong_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=self.correct_image, highlightthickness=0, command=self.true_button)
        self.correct_button.config(padx=50, pady=50)
        self.correct_button.grid(row=2, column=0)
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.false_button)
        self.wrong_button.config(padx=50, pady=50)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.\nYour final "
                                                            f"score is {self.quiz.score}/10")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def false_button(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def true_button(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
