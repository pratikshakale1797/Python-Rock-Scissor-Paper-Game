from tkinter import *
import random

win = Tk()


class game:
    def __init__(self, win):
        self.countC = 0
        self.countU = 0
        self.btnclick = 0
        self.win = win
        win.title("Rock Paper Scissors")
        win.geometry("500x300")
        label1 = Label(win, text="Rock Paper Scissors", fg="gray", font=(25)).pack(side=TOP)

        self.entryval2 = StringVar(win, value='Lets play Game')
        self.entry2 = Entry(win, textvariable=self.entryval2, fg="green", state='readonly', borderwidth=0, font=(20))
        self.entry2.place(x=200, y=30)

        label3 = Label(win, text="Your Options:-", fg="gray", font=(18)).place(x=10, y=60)
        Rockbtn = Button(win, text="Rock", bg="magenta", fg="#15f4ee", width=15)
        Rockbtn.place(x=50, y=90)
        Rockbtn.bind('<Button-1>', self.rock)

        Paperbtn = Button(win, text="Paper", bg="gray", fg="#15f4ee", width=15)
        Paperbtn.place(x=200, y=90)
        Paperbtn.bind('<Button-1>', self.paper)

        Scissorbtn = Button(win, text="Scissors", bg="yellow", fg="#15f4ee", width=15)
        Scissorbtn.place(x=350, y=90)
        Scissorbtn.bind('<Button-1>', self.scissor)

        label4 = Label(win, text="Score", fg="gray", font=(18)).place(x=10, y=130)

        label5 = Label(win, text="Your Selected:-", fg="gray", font=(16)).place(x=50, y=160)
        self.entryval3 = IntVar(win, value='None')
        self.entry3 = Entry(win, textvariable=self.entryval3, borderwidth=0, state='readonly', fg="gray", font=(8))
        self.entry3.place(x=170, y=160)

        label6 = Label(win, text="Computer Selection:-", fg="gray", font=(16)).place(x=50, y=190)
        self.entryval4 = IntVar(win, value='None')
        self.entry4 = Entry(win, textvariable=self.entryval4, borderwidth=0, state='readonly', fg="gray", font=(8))
        self.entry4.place(x=210, y=190)

        label7 = Label(win, text="Your Score:-", fg="gray", font=(16)).place(x=300, y=160)
        self.entryval5 = IntVar(win, value=0)
        self.entry5 = Entry(win, textvariable=self.entryval5, borderwidth=0, state='readonly', fg="gray", font=(8))
        self.entry5.place(x=400, y=160)

        label8 = Label(win, text="Computer Score:-", fg="gray", font=(16)).place(x=300, y=190)
        self.entryval6 = IntVar(win, value=0)
        self.entry6 = Entry(win, textvariable=self.entryval6, borderwidth=0, state='readonly', fg="gray", font=(8))
        self.entry6.place(x=440, y=190)

    def reset(self, event=None):
        top = Toplevel()
        top.title("Match Winner...!")
        top.geometry("300x300")
        if self.countC > self.countU:
            winnerlabel = Label(top, text="Computer Winner..!", fg="green", font=(15)).pack(side=TOP)
            winnerscore = Label(top, text="Score:-", fg="gray", font=(12)).pack(side=TOP)

            correct = Label(top, text="Correct", fg="green", font=(10)).place(x=80, y=50)
            incorrect = Label(top, text="Incorrect", fg="red", font=(10)).place(x=160, y=50)
            match = Label(top, text="Match", fg="orange", font=(10)).place(x=240, y=50)

            winnerComputer = Label(top, text="Coputer", fg="blue", font=(12)).place(x=15, y=70)
            result = 10 - (self.countC + self.countU)
            correctPC = Label(top, text=self.countC, fg="green", font=(10)).place(x=80, y=70)
            incorrectPC = Label(top, text=self.countU, fg="red", font=(10)).place(x=160, y=70)
            matchPC = Label(top, text=result, fg="orange", font=(10)).place(x=240, y=70)

        else:
            winnerlabel = Label(top, text="You Winner..!", fg="green", font=(12)).pack(side=TOP)
            winnerscore = Label(top, text="Score:-", fg="gray", font=(12)).pack(side=TOP)

            correct = Label(top, text="Correct", fg="green", font=(10)).place(x=80, y=50)
            incorrect = Label(top, text="Incorrect", fg="red", font=(10)).place(x=160, y=50)
            match = Label(top, text="Match", fg="orange", font=(10)).place(x=240, y=50)

            winnerComputer = Label(top, text="Your", fg="blue", font=(12)).place(x=15, y=70)
            result = 10 - (self.countC + self.countU)
            correctPC = Label(top, text=self.countU, fg="green", font=(10)).place(x=80, y=70)
            incorrectPC = Label(top, text=self.countC, fg="red", font=(10)).place(x=160, y=70)
            matchPC = Label(top, text=result, fg="orange", font=(10)).place(x=240, y=70)

        # reset all count value and labels
        self.countC = 0
        self.countU = 0
        self.btnclick = 0
        self.entryval6.set(self.countC)
        self.entryval5.set(self.countU)
        self.entryval4.set("None")
        self.entryval3.set("None")
        self.entryval2.set("Lets play Game")

    def rock(self, event=None):
        if self.btnclick > 9:
            self.reset()
        else:
            pc = random.choice(['rock', 'paper', 'scissor'])
            self.entryval3.set("rock")
            self.entryval4.set(pc)

            if pc == 'rock':
                self.entryval2.set("match Tie")
            elif pc == 'paper':
                self.entryval2.set("Computer Win...!")
                self.countC = self.countC + 1
                self.entryval6.set(self.countC)
            else:
                self.entryval2.set("You Win...!")
                self.countU = self.countU + 1
                self.entryval5.set(self.countU)

            self.btnclick = self.btnclick + 1

    def paper(self, event=None):
        if self.btnclick > 9:
            self.reset()
        else:
            pc = random.choice(['rock', 'paper', 'scissor'])
            self.entryval3.set("paper")
            self.entryval4.set(pc)
            if pc == 'paper':
                self.entryval2.set("Match Tie")
            elif pc == 'scissor':
                self.entryval2.set("Computer Win...!")
                self.countC = self.countC + 1
                self.entryval6.set(self.countC)
            else:
                self.entryval2.set("You Win...!")
                self.countU = self.countU + 1
                self.entryval5.set(self.countU)

            self.btnclick = self.btnclick + 1

    def scissor(self, event=None):
        if self.btnclick > 9:
            self.reset()
        else:
            pc = random.choice(['rock', 'paper', 'scissor'])
            self.entryval3.set("scissor")
            self.entryval4.set(pc)
            if pc == 'scissor':
                self.entryval2.set("Match Tie")
            elif pc == 'rock':
                self.entryval2.set("Computer Win...!")
                self.countC = self.countC + 1
                self.entryval6.set(self.countC)
            else:
                self.entryval2.set("You Win")
                self.countU = self.countU + 1
                self.entryval5.set(self.countU)
            self.btnclick = self.btnclick + 1


obj = game(win)

win.mainloop()