from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quiz_Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.quiz = quiz_brain

        self.score_label = Label(text=f"Score : {self.score}", foreground="white", background=THEME_COLOR, font=("Arial", 20, "bold"))

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, command=self.true_button_pressed)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, command=self.false_button_pressed)


        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.false_button.grid(row=2, column=0)
        self.true_button.grid(row=2, column=1)
        
        self.next_question()

        self.window.mainloop()

    def true_button_pressed(self):
        if self.quiz.check_answer("True"):
            self.score+=1
            self.score_label.config(text=f"Score : {self.score}")
            self.canvas.config(background="Green")
        else:
            self.canvas.config(background="red")

        if self.quiz.still_has_questions():        
            self.window.after(1000, self.next_question)
        else:
            self.result()

    
    def false_button_pressed(self):
        if self.quiz.check_answer("False"):
            self.score+=1
            self.score_label.config(text=f"Score : {self.score}")
            self.canvas.config(background="Green")
        else:
            self.canvas.config(background="red")
        
        if self.quiz.still_has_questions():
            self.window.after(1000, self.next_question)
        else:
            self.result()

    def next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def result(self):
        self.canvas.destroy()
        self.score_label.config(font=("Arial", 50, "bold"))
        self.score_label.grid(row=0, column=0, columnspan=2, pady=100, padx=100)
        self.false_button.destroy()
        self.true_button.destroy()