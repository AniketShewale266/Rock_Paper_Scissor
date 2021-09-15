from tkinter import *
import random
import tkinter.messagebox as tsmg

usercount = 0
computercount = 0
roundcnt = 1
# number
# computer, user,tie


def scoreboard():
    global sco
    sco = Toplevel(root)
    sco.geometry("850x550")
    sco.title("Rock Paper Scissor Game")
    framesco = Frame(sco, bg="blue")

    whowin = StringVar()
    # uservalue.set("You Win...")
    win = Label(framesco, bg='blue', textvariable=whowin, fg='white', font="Century 28 bold")
    win.place(x=250, y=70, width=350, height=50)

    uscore = StringVar()
    # uscore.set("2")
    userscore = Label(framesco, fg='white', textvariable=uscore, font="Century 40 bold", bg='blue')
    userscore.place(x=350, y=120, width=50, height=50)

    line = Label(framesco, text=":", font="Century 40 bold", fg='white', bg='blue')
    line.place(x=397, y=130, width=50, height=50)

    cscore = StringVar()
    # cscore.set("3")
    computerscore = Label(framesco, fg='white', textvariable=cscore, font="Century 40 bold", bg='blue')
    computerscore.place(x=445, y=120, width=50, height=50)

    playagain1 = Button(framesco,text="Play Again", fg='black',
                       highlightbackground="black", highlightthickness=7,
                       font="Century 20 bold", bg='white', relief=SUNKEN,command=back,cursor="hand2")
    playagain1.place(x=330, y=200, width=200, height=70)

    if (usercount == 3):
        whowin.set("You Win...")
        # print("get")
    elif (computercount == 3):
        whowin.set("Computer Win...")
        # print("take")

    uscore.set(str(usercount))
    cscore.set(str(computercount))



    framesco.place(x=0, y=0, width=850, height=550)

    root.withdraw()
    sco.resizable(0,0)


def back():
    global computercount
    global roundcnt
    global usercount
    sco.withdraw()
    sco.destroy()
    roundcnt = 1
    usercount = 0
    computercount = 0

    roundtext.set("1")
    ustar1.config(image=img1)
    ustar2.config(image=img1)
    ustar3.config(image=img1)
    cstar1.config(image=img1)
    cstar2.config(image=img1)
    cstar3.config(image=img1)

    root.deiconify()


def randomfunction():
    global computer
    l1 = ["0","1","2"]
    computer = random.choice(l1)
    # print(computer)

def ForRock():
    global computercount
    global roundcnt
    global usercount
    if (computer == "1"):
        labelforuser.config(image=stoneleft)
        labelforcomputer.config(image=paperright)
        tsmg.showinfo("Rock Paper Scissor", "Computer Win!")
        computercount = computercount + 1
        roundcnt = roundcnt + 1
    elif (computer == "0"):
        labelforuser.config(image=stoneleft)
        labelforcomputer.config(image=stoneright)
        tsmg.showinfo("Rock Paper Scissor", "Tie!")
        roundcnt = roundcnt + 1
    else:
        labelforuser.config(image=stoneleft)
        labelforcomputer.config(image=scissorright)
        tsmg.showinfo("Rock Paper Scissor", "You Win!")
        usercount = usercount + 1
        roundcnt = roundcnt + 1

    roundtext.set(str(roundcnt))

def ForPaper():
    global computercount
    global roundcnt
    global usercount
    if (computer == "1"):
        labelforuser.config(image=paperleft)
        labelforcomputer.config(image=paperright)
        tsmg.showinfo("Rock Paper Scissor", "Tie!")
        roundcnt = roundcnt + 1
    elif (computer == "0"):
        labelforuser.config(image=paperleft)
        labelforcomputer.config(image=stoneright)
        tsmg.showinfo("Rock Paper Scissor", "You Win!")
        usercount = usercount + 1
        roundcnt = roundcnt + 1
    else:
        labelforuser.config(image=paperleft)
        labelforcomputer.config(image=scissorright)
        tsmg.showinfo("Rock Paper Scissor", "Computer Win!")
        computercount = computercount + 1
        roundcnt = roundcnt + 1

    roundtext.set(str(roundcnt))

def ForScissor():
    global computercount
    global roundcnt
    global usercount
    if (computer == "1"):
        labelforuser.config(image=scissorleft)
        labelforcomputer.config(image=paperright)
        tsmg.showinfo("Rock Paper Scissor", "You Win!")
        usercount = usercount + 1
        roundcnt = roundcnt + 1
    elif (computer == "0"):
        labelforuser.config(image=scissorleft)
        labelforcomputer.config(image=stoneright)
        tsmg.showinfo("Rock Paper Scissor", "Computer Win!")
        computercount = computercount + 1
        roundcnt = roundcnt + 1
    else:
        labelforuser.config(image=scissorleft)
        labelforcomputer.config(image=scissorright)
        tsmg.showinfo("Rock Paper Scissor", "Tie!")
        roundcnt = roundcnt + 1

    roundtext.set(str(roundcnt))

def userstars():
    if (usercount == 1):
        ustar1.config(image=userstar1)
    elif (usercount == 2):
        ustar2.config(image=userstar2)
    elif (usercount == 3):
        ustar3.config(image=userstar3)

def computerstars():
    if (computercount == 1):
        cstar1.config(image=computerstar1)
    elif (computercount == 2):
        cstar2.config(image=computerstar2)
    elif (computercount == 3):
        cstar3.config(image=computerstar3)

def stars():
    userstars()
    computerstars()

def score():
    if(usercount==3):
        # root.destroy()
        scoreboard()
        # root.withdraw()

    elif(computercount==3):
        # root.destroy()
        scoreboard()
        # root.withdraw()


def mainfunrock(event):
    randomfunction()
    ForRock()
    labelforuser.config(image=blank1)
    labelforcomputer.config(image=blank2)
    stars()
    score()

def mainfunpaper(event):
    randomfunction()
    ForPaper()
    labelforuser.config(image=blank1)
    labelforcomputer.config(image=blank2)
    stars()
    score()

def mainfunscissor(event):
    randomfunction()
    ForScissor()
    labelforuser.config(image=blank1)
    labelforcomputer.config(image=blank2)
    stars()
    score()

def close(event):
    root.destroy()


root = Tk()
root.title("Rock Paper Scissor Game")
root.geometry("850x550")
root.wm_iconbitmap("icongame.ico")

# global labelforuser
# global labelforcomputer
# global blank1, roundtext, stoneleft, stoneright, paperleft, paperright, scissorleft, scissorright
# global blank2, userstar1, userstar2, userstar3, computerstar1, computerstar2, computerstar3
# global ustar1, ustar2, ustar3, cstar1, cstar2, cstar3

f1 = Frame(root, bg="blue", highlightbackground="black", highlightthickness=1)
l1 = Label(f1, text="ROUND", bg='blue', fg='white', font="Century 20 bold")
l1.place(x=355, y=20, width=130, height=50)

roundtext = StringVar()
roundtext.set("1")
labelroundcnt = Label(f1, textvariable=roundtext, bg='blue', fg='white', font="Century 20 bold");
labelroundcnt.place(x=475, y=20, width=50, height=50)

img1 = PhotoImage(file="s.png")

You = Label(f1, text="Your Score", fg='white', font="Century 14 bold", bg='blue')
You.place(x=5, y=50, width=150, height=30)

ustar1 = Label(f1, image=img1, bg='blue')
ustar1.place(x=10, y=85, width=51, height=47)

ustar2 = Label(image=img1, bg='blue')
ustar2.place(x=80, y=85, width=51, height=47)

ustar3 = Label(image=img1, bg='blue')
ustar3.place(x=150, y=85, width=51, height=47)

Computer = Label(f1, text="Computer Score", fg='white', font="Century 14 bold", bg='blue')
Computer.place(x=650, y=50, width=185, height=30)

cstar1 = Label(image=img1, bg='blue')
cstar1.place(x=645, y=85, width=51, height=47)

cstar2 = Label(image=img1, bg='blue')
cstar2.place(x=715, y=85, width=51, height=47)

cstar3 = Label(image=img1, bg='blue')
cstar3.place(x=785, y=85, width=51, height=47)

f1.place(x=0, y=0, width=850, height=150)

# left Frame
f2 = Frame(root, bg="blue", highlightbackground="black", highlightthickness=1)

userclick = Label(f2, text="Click Your Choice", font="Century 14 bold", bg="blue", fg="white")
userclick.place(x=15, y=10, width=180, height=30)

r = PhotoImage(file="stone_leftnew.png")
p = PhotoImage(file="paper_leftnew.png")
s = PhotoImage(file="scissor_leftnew.png")

rock = Button(f2, text="Rock", image=r,cursor="hand2")
rock.place(x=30, y=50, width=140, height=80)
rock.bind("<Button-1>", mainfunrock)

paper = Button(f2, text="Paper", image=p,cursor="hand2")
paper.place(x=30, y=150, width=140, height=80)
paper.bind("<Button-1>", mainfunpaper)

scissor = Button(f2, text="Scissor", image=s,cursor="hand2")
scissor.place(x=30, y=250, width=140, height=80)
scissor.bind("<Button-1>", mainfunscissor)

exitbtn = Button(f2, text="Exit", cursor="hand2", fg='white', bd=5, relief=RAISED,
                     bg='blue', font="Century 10 bold",
                     highlightbackground="black", highlightthickness=1)
exitbtn.place(x=20, y=345, width=70, height=40)
exitbtn.bind("<Button-1>", close)

f2.place(x=0, y=150, width=210, height=430)

userstar1 = PhotoImage(file="starnew1.png")
userstar2 = PhotoImage(file="starnew1.png")
userstar3 = PhotoImage(file="starnew1.png")

computerstar1 = PhotoImage(file="starnew1.png")
computerstar2 = PhotoImage(file="starnew1.png")
computerstar3 = PhotoImage(file="starnew1.png")

    # ustar1.config(image=userstar1) #use to change to label image
    # ustar1['image'] =userstar1 #use to change to label image

    # middle frame
stoneleft = PhotoImage(file="stone_left.png")
stoneright = PhotoImage(file="stone_right.png")
paperleft = PhotoImage(file="paper_left.png")
paperright = PhotoImage(file="paper_right.png")
scissorleft = PhotoImage(file="scissor_left.png")
scissorright = PhotoImage(file="scissor_right.png")
blank1 = PhotoImage(file="")
blank2 = PhotoImage(file="")

f3 = Frame(root, bg='white', highlightbackground="black", highlightthickness=1)

labelforuser = Label(f3, text="", bg='white', image=blank1)
labelforuser.place(x=50, y=100, width=252, height=216)

labelforcomputer = Label(f3, text="", bg='white', image=blank2)
labelforcomputer.place(x=350, y=100, width=252, height=216)

# labelforuser.config(image=paperleft)
# labelforcomputer.config(image=stoneright)

f3.place(x=210, y=150, width=640, height=400)




root.resizable(0,0)
root.mainloop()