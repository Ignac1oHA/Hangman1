from tkinter import *
import sys

def test():
    # won is a boolean that indicates whether the participant saves William Wallace or not
    # lost when you did not save William Wallace
    # stage is the number of mistakes the participant committed
    # canvas is the GUI element on which we need to put the picture
    # img is the image picture we will display in the canvas
    global won, lost, stage, canvas, img

    text = et.get()
    if text:
        text = text[0]

    if won or lost:
        return
    if text in guessed or text not in word:
        stage +=1

        # draw the nex picture, name should be easy to link
        img_name = "stage" + str(stage) + ".gif"
        img = PhotoImage(file=img_name)
        canvas.create_image(0, 0, image=img, another=NW)

        # check if lost, with 8 tries (9 images) that is the maximum tries each participant has
        if stage == 8
            lb6.config(text="You did not saved William Wallace, shame on you", fg="black", bg="red", font=("arial", 40))
            lost = True
            guess.config(text=word, fg="green")

        # I delete the entry text, so another text can be entered an checked
        et.delete(0, END)
        return

    # second stage, we have guessed a letter
    won = True
    if text in word:
        # letter correct, is William Wallace safe?
        guessed.append(text)
        string = ""
        for c in word:
            if c in word:
                if c in guessed:
                    string += c + " "
                else:
                    string += " "
                    won = False
        guess.config(text=string)
    if won:
        lb6.config(text="You saved William Wallace, congrats mate!", fg="blue", font=("arial", 40))
        won = True
    et.delete(0, END)

window = Tk()

word = "coding"
guessed = [""]
stage = 0
won = False
window.title("Welcome to Hangman!")

# Widgets
lb = Label(master=window, text="What´s your guess?", font=("Garamond", 20), fg="blue", bg="gray")
lb2 = Label(master=window, text="Thanks for supporting us!", font=("Garamond", 12), fg="gray")
lb3 = Label(master=window, text="_ _ _ _ ", font=("Georgia", 20), fg="gray", bg="black")
lb4 = Label(master=window, text="Here are the instructions: Please guess a 4 words letter. If you are right William Wallace survives.", font=("Georgia", 8), fg="gray", bg="black")
lb5 = Label(master=window, text="Disclaimer: This game was launched long time ago, please do not hang peaople in the public square.", font=("Georgia", 8), fg="gray", bg="black")
lb6 = You did not saved William Wallace, shame on you

bt1 = Button(master=window, text="Try!", font=("Georgia", 15), command=sys.exit)
bt2 = Button(master=window, text="Exit", font=("Georgia", 15), command=sys.exit)

et_text = StringVar()
et = Entry(master=window, width=30, textvariable=et_text, font=("Arial", 25))

# Positions of the widgets
lb.grid(row=2, column=0)
lb2.grid(row=5, column=2)
lb3.grid(row=3, column=1)
lb4.grid(row=0, column=1)
lb5.grid(row=1, column=1)

bt1.grid(row=2, column=2)
bt2.grid(row=3, column=2)

et.grid(row=2, column=1, padx=10, pady=20)

canvas = Canvas()
canvas.grid()

window.mainloop()