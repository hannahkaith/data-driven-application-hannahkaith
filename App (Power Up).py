from tkinter import *
import requests
from tkinter import messagebox

app = Tk()
app.title("Power Up! : Trivia Game (General Knowledge)")
app.geometry('750x600')
app.resizable(0,0)
# App Icon Image
AppIcon = PhotoImage(file='icon/App icon.png')
app.iconphoto(False, AppIcon)


# functions
#   to showcase frames
def show_pages(frame):
    frame.tkraise() #tkraise() will move widget to the top of the stacking order

#   Frames to switch between diffferent pages and Choose from the difficulties
frame1 = Frame(app)
frame2 = Frame(app)
frame3 = Frame(app)
quesFrame = Frame(app)

for frame in (frame1, frame2, frame3, quesFrame):
    frame.place(y=0,x=0,height=600,width=750)
show_pages(quesFrame) # to showcase which frame goes on top 


#   to get API data
def get_data(): 
    # API request 
    url = f"https://opentdb.com/api.php?amount=1&category=9&type=boolean"  
    response = requests.get(url)
    data = response.json()

    # to print the question
    ques = data["results"][0]['question'].replace("&quot;", '"').replace("&#039;", '\'').replace("&rsquo;", "'").replace("&aring;","å")  
        # to replace certain words with its corresponding symbols
    
    # Difficulty of the questions
    diff = data["results"][0]['difficulty']
    if diff == 'easy':
        difficulty.config(text="DIFFICULTY :  EASY")
    elif diff == 'medium':
        difficulty.config(text="DIFFICULTY :  MEDIUM")
    else:
        difficulty.config(text="DIFFICULTY :  HARD")
    
    # to gurantee a clean text area
    questionLabel.delete('1.0', END)  
    questionLabel.insert(END, ques)


def check_ans():
    url = f"https://opentdb.com/api.php?amount=1&category=9&type=boolean"  
    response = requests.get(url)
    data = response.json()

    # to get the correct answer
    correct = data["results"][0]['correct_answer']
    input = answer.get()

    # to output a message box and confirm whether the input is correct or not
    if input.capitalize() == correct:
        messagebox.showinfo("Your Right!",f" KEEP IT UP :> ")
    else:
        messagebox.showwarning("UH-OH!",f" The correct answer is : {correct} ")
    
def delete_content():
    # to erase the last question
    questionLabel.delete('1.0', END) 

    # to erase the last question's difficulty
    difficulty.config(text="DIFFICULTY : ")

    # to erase the last answer of the user
    answer.set("")





# Widgets
#   Frame 1 code | Intro Page
bgpic1 = PhotoImage(file="background-img/Main BG.png")
bg = Label( frame1, image=bgpic1) 
bg.place(x=0,y=0) 

Mainbtn1 = PhotoImage(file="button-img/Main-btn1.png")
fBTN = Button(frame1,image=Mainbtn1,borderwidth=0,command=lambda:show_pages(frame2))
fBTN.place(x=390,y=430)

Mainbtn2 = PhotoImage(file="button-img/Main-btn2.png")
sBTN = Button(frame1,image=Mainbtn2,borderwidth=0,command=lambda:app.destroy())
sBTN.place(x=125,y=430)



#   Frame 2 code | Purpose of App Page
bgpic2 = PhotoImage(file="background-img/Purpose BG.png")
bg = Label( frame2,image=bgpic2) 
bg.place(x=0,y=0) 

Purposebtn1 = PhotoImage(file="button-img/Purpose-btn1.png")
fBTN = Button(frame2,image=Purposebtn1,borderwidth=0,command=lambda:show_pages(frame3))
fBTN.place(x=280,y=460)

Purposebtn2 = PhotoImage(file="button-img/Purpose-btn2.png")
sBTN = Button(frame2,image=Purposebtn2,borderwidth=0,command=lambda:show_pages(frame1))
sBTN.place(x=35,y=40)



#   Frame 3 code | Instructions Page
bgpic3 = PhotoImage(file="background-img/Ins BG.png")
bg = Label( frame3,image=bgpic3) 
bg.place(x=0,y=0)


title = PhotoImage(file="img/ins-title.png")
InsTitle = Label(frame3,image=title,bd=0)
InsTitle.place(x=445,y=165)

nextBTN = PhotoImage(file="button-img/start-btn.png")
fBTN = Button(frame3,image=nextBTN,borderwidth=0,command=lambda:show_pages(quesFrame))
fBTN.place(x=570,y=410)

backBTN = PhotoImage(file="button-img/back-btn.png")
sBTN = Button(frame3,image=backBTN,borderwidth=0,command=lambda:show_pages(frame2))
sBTN.place(x=415,y=410)


#   QuesFrame code | Question Page
answer = StringVar() # to retrieve input given by user; a bridge between the widget and the data

bgpic4 = PhotoImage(file="background-img/Question BG.png")
bg = Label(quesFrame,image=bgpic4) 
bg.place(x=0,y=0)

backbtn = PhotoImage(file="button-img/Purpose-btn2.png")
fBTN = Button(quesFrame,image=backbtn,borderwidth=0,command=lambda:show_pages(frame3))
fBTN.place(x=35,y=40)

questionLabel = Text(quesFrame,height=4,width=56,bg='#FAE4D7',fg='#CC7272',font=('Helvetica',11,'bold'))
questionLabel.place(x=150,y=245)

clearbtn = PhotoImage(file="button-img/clear-btn.png")
sBTN = Button(quesFrame,image=clearbtn,borderwidth=0,command=delete_content)
sBTN.place(x=540,y=200)

randombtn = PhotoImage(file="button-img/ques-btn.png")
fBTN = Button(quesFrame,image=randombtn,borderwidth=0,command=get_data)
fBTN.place(x=285,y=390)

difficulty = Label(quesFrame,text="DIFFICULTY :  ",fg='#E6A3A3',bg='#FAE4D7',font=('Helvetica',10,'bold'))
difficulty.place(x=130,y=205)

explanation = PhotoImage(file="img/explanation.png")
explain = Label(quesFrame,image=explanation,bd=0)
explain.place(x=170,y=455)

answerEntry= Entry(quesFrame,textvariable=answer,justify="center",width=20,fg='#235949',bg='#F9F4F0',font=('Helvetica',16))
answerEntry.place(x=180,y=480)

checkbtn = PhotoImage(file="button-img/check-btn.png")
submitAns = Button(quesFrame,image=checkbtn,borderwidth=0,command=check_ans)
submitAns.place(x=435,y=478)


# to execute the code above and display the desired output
app.mainloop()
