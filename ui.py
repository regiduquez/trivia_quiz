THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain): # declares the parameter data type
        self.question = quiz_brain
        self.score = 0
        self.your_answer = str
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300)
        self.canvas_txt = self.canvas.create_text(
            150,125,
            width=280,
            text="SAMPLE TRIVIA",
            font=('Arial',14, 'italic'),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=(20, 20))

        self.score_label = Label(text=f"Score:0",background=THEME_COLOR,foreground='white', font=('Arial',10, 'bold'))
        self.score_label.grid(row=0, column=1,pady=(20, 20))

        true_img =PhotoImage(file='images/true.png')
        self.true = Button(image=true_img,command=self.click_true)
        self.true.grid(column=0, row=2,pady=(20, 20))

        false_img = PhotoImage(file='images/false.png')
        self.false = Button(image=false_img,command=self.click_false)
        self.false.grid(column=1, row=2,pady=(20, 20))
        self.get_next()



        self.window.mainloop()

    def get_next(self):
        if self.question.still_has_questions():
            q_text = self.question.next_question()
            self.canvas.itemconfig(self.canvas_txt, text=q_text)
            self.canvas.config(background='white')

        else:
            self.canvas.itemconfig(self.canvas_txt, text="You've Reach The end of the Quiz!")
            self.false.config(state='disabled')
            self.true.config(state='disabled')



    def click_true(self):
        self.update_score('True')
        self.window.after(1000,self.get_next)



    def click_false(self):
        self.update_score('False')
        self.window.after(1000, self.get_next)


    def update_score(self,answer: str):
        if self.question.check_answer(answer):
            self.score +=1
            self.feedback('green')
        else:
            self.feedback('red')
        print(self.question.check_answer(answer))
        self.score_label.config(text=f"Score: {self.score}")

    def feedback(self,color: str):
        self.canvas.config(background=color)

