import tkinter as tk, json
from functools import partial
"""
This program is supposed to catalogue and display selected information about pet rats by reading and writing a .json file.
Educational purpose: Exercise in graphical output via tkinter, as well as exercise in using data in .json files.

todo: 
A way to add new rats into the system; let the user input their data and have it converted to a .json file. perhaps implement a max?
Change rat name input to buttons, to avoid having to use try except. also visually more appealing.

"""


def ratChange(changeArg):
    global inputChangeText
    global outputChangeText
    match changeArg:
        case 1:
            inputChangeText = tk.Text(frame1,height=1,width=20)
            inputChangeText.grid(column=0, row=0)
            ratChangeNumber = 1
        case 2:
            inputChangeText = tk.Text(frame1,height=1,width=20)
            inputChangeText.grid(column=0, row=1)
            ratChangeNumber = 2
        case 3:
            inputChangeText = tk.Text(frame1,height=1,width=20)
            inputChangeText.grid(column=0, row=2)
            ratChangeNumber = 3
    global changeDoneBut
    changeDoneBut=tk.Button(frame1, text = "Fertig", command=partial(ratChangeDone,ratChangeNumber))
    changeDoneBut.grid(column=2,row=4)

def ratChangeDone(ratChangeNumber):
    with open (fileselect, 'r') as db:
        ratChangeDict = json.load(db)
        outputChangeText = inputChangeText.get(1.0, "end-1c"),
    match ratChangeNumber:
        case 1:
            ratChangeDict |= {'name':outputChangeText[0]}
        case 2:
            ratChangeDict |= {'age':outputChangeText[0]}
        case 3:
            ratChangeDict |= {'gen':outputChangeText[0]}
    with open (fileselect, 'w', encoding='utf-8') as db:
        json.dump(ratChangeDict, db)
    inputChangeText.destroy()
    changeDoneBut.destroy()
    ratOpen()


def ratOpen():
    try:
        global fileselect
        fileselect =  inputtxt.get(1.0,"end-1c")+".json" #Gets the text from the input space and appends ".json"
        with open(fileselect, 'r') as db:
            ratList = json.load(db) #Opens the selected rat's .json file.
        labelResult1.config(text = "Name: " + ratList["name"])  #This is terrible and I will change this. Update: this is somewhat better.
        labelResult2.config(text = "Alter: " + ratList["age"])   #My hope is that this is so terrible I'm never allowed to write UI again.
        labelResult3.config(text = "Geschlecht: " + ratList["gen"])

        buttonChange1 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,1))
        buttonChange1.grid(column=2,row=0)
        buttonChange2 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,2))
        buttonChange2.grid(column=2,row=1)
        buttonChange3 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,3))
        buttonChange3.grid(column=2,row=2)
        window.mainloop()

    except:
       labelResult1.config(text = "Bitte geben einen Namen ein, der im System vorhanden ist!")
       print(fileselect)

window = tk.Tk()
window.geometry('1280x720')
window.title("RatApp") #Name is WIP.

labelHead = tk.Label(window, text= "Gebe hier einen Namen deiner Ratten ein, um Information über diese zu bekommen:")
labelHead.pack()

inputtxt = tk.Text(window,height = 1,width = 20)
inputtxt.pack()

buttonStart= tk.Button(text="Start!", command=ratOpen)
buttonStart.pack()

frame1 = tk.Frame(window, height="200", width="1000")
frame1['borderwidth'] = '20'
frame1['relief'] = 'sunken'
frame1.columnconfigure(0, weight = 1)
frame1.columnconfigure(0, weight = 3)
frame1.pack()

labelResult1 = tk.Label(frame1, text = "")
labelResult1.grid(column=0,row=0, sticky=tk.W, padx=5)

labelResult2 = tk.Label(frame1, text = "")
labelResult2.grid(column=0,row=1, sticky=tk.W, padx=5)

labelResult3= tk.Label(frame1, text = "")
labelResult3.grid(column=0,row=2, sticky=tk.W, padx=5) # I am very sure there is a better way to do this, but this works for now.

window.mainloop()
