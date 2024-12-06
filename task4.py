import re
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Scissor Paper Game")
root.configure(background="deeppink")

rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

user_label = Label(root, image=scissor_img, bg="deeppink")
comp_label = Label(root, image=scissor_img_comp, bg="deeppink")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


playerScore = Label(root, text=0, font = ("arial", "40", "bold"), bg="deeppink", fg="white")
computerScore = Label(root, text=0, font = ("arial", "40", "bold"), bg="deeppink", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

user_indicator = Label(root, font = ("ALGERIAN", "25", "bold"), text="\n YOU :-  \n--------------------", bg="deeppink", fg="yellow")
comp_indicator = Label(root, font = ("ALGERIAN", "25", "bold"), text="\n COMPUTER :- \n--------------------------",
                       bg="deeppink", fg="yellow")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

msg = Label(root,  font = ("arial", "20", "bold"), bg="deeppink", fg="white")
msg.grid(row=1, column=2)

def updateMessage(x):
    msg['text'] = x



def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)



def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)



def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("Oops! You loose!")
            updateCompScore()
        else:
            updateMessage("Yehh! You Win!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("Oops! You loose!")
            updateCompScore()
        else:
            updateMessage("Yehh! You Win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("Oops! You loose!")
            updateCompScore()
        else:
            updateMessage("Yehh! You Win!")
            updateUserScore()

    else:
        pass



choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)




rock = Button(root, width=20, height=2, font = ("arial", "12", "bold"), text="ROCK",
              bg="saddlebrown", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, font = ("arial", "12", "bold"), text="PAPER",
               bg="slategray", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, font = ("arial", "12", "bold"), text="SCISSOR",
                 bg="crimson", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()