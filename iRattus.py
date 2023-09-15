import tkinter as tk, json
from functools import partial
"""
This program is supposed to catalogue and display selected information about pet rats by reading and writing a .json file.
Educational purpose: Exercise in graphical output via tkinter, as well as exercise in using data in .json files.

todo: 
good question, actually

notes:
Changing input to a button might be exceedingly difficult for my skillset, so input remains text (for now)
    #This is because I would have to generate a variable amount of buttons, as the amount of rats in the system is also variable. I could put a max of maybe 5 rats, but
    I don't believe this viable, as it does not correlate to reality. Some owners, and breeders especially, have dozens of rats at a time.

"""
hasFrame = 0
ratLabelName = ""
hasButNew = 0
newX = 0
confirmConfirm = 0 #This is for confirmation for deleting a rat.

##########################################################################################################################################################

def ratChange(changeArg): #This function handles the changing of the attributes. changes are committed to in ratChangeDone.
    global inputChangeText, changeDoneBut, cancelChangeBut
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
        case 4:
            inputChangeText = tk.Text(frame1,height=1,width=20)
            inputChangeText.grid(column=0, row=0)
            ratChangeNumber = 1
        case 5:
            inputChangeText = tk.Text(frame1,height=1,width=20)
            inputChangeText.grid(column=0, row=1)
            ratChangeNumber = 2
        case 6:
            inputChangeText = tk.Text(frame1,height=1,width=20)
            inputChangeText.grid(column=0, row=2)
            ratChangeNumber = 3    
    changeDoneBut=tk.Button(frame1, text = "Fertig", command=partial(ratChangeDone,ratChangeNumber))
    changeDoneBut.grid(column=2,row=6)
    cancelChangeBut=tk.Button(frame1, text= "Abbrechen", command=partial(ratChangeCancel))
    cancelChangeBut.grid(column=0,row=6, sticky=tk.W)

##########################################################################################################################################################

def ratChangeCancel(): #If the user decides to cancel the changing process, this destroys the UI for it and stops any change.
    cancelChangeBut.destroy()
    changeDoneBut.destroy()
    inputChangeText.destroy()

##########################################################################################################################################################

def ratNewUI(): #builds the UI for adding a new rat. Also handles accessing the other functions, ratNewAppend() and ratNewCommit()
    global frame1, hasFrame, hasButNew, newX, existRatLabel, labelHead, buttonDel
    if hasFrame == 1:
        frame1.destroy()
        hasFrame = 0
    if hasButNew == 0:
        labelHead.config(text= "")
        buttonNew.config(text="Abbrechen", command=partial(ratNewCancel))
        buttonDel.destroy()
        newX = 0
        hasButNew = 1
        existRatLabel.config(text="Bitte gebe den Namen ein: ")
    if newX <= 6:
        buttonStart.config(command=partial(ratNewUI))
        ratNewAppend(newX)
        newX += 1


##########################################################################################################################################################

def ratNewAppend(ratNewNumber): #Prepares the attributes to append in the next function, which is ratNewCommit(). Does this by getting the input and saving it to a variable.
    global newRatAppend1, newRatAppend2, newRatAppend3, newRatAppend4, newRatAppend5, newRatAppend6, inputtxt, existRatLabel # reusing this because it saves space and i am lazy.
    match ratNewNumber:    
        case 1:
            newRatAppend1 =inputtxt.get(1.0,"end-1c")
            inputtxt.delete(1.0,"end-1c")
            print("name")
            existRatLabel.config(text="Bitte gebe das Alter ein: ")
        case 2:
            newRatAppend2 =inputtxt.get(1.0,"end-1c")
            inputtxt.delete(1.0,"end-1c")
            print("age")
            existRatLabel.config(text="Bitte gebe den das Geschlecht ein: ")
        case 3: 
            newRatAppend3 =inputtxt.get(1.0,"end-1c")
            inputtxt.delete(1.0,"end-1c")
            existRatLabel.config(text="Bitte gebe das Gewicht ein: ")
        case 4: 
            newRatAppend4 =inputtxt.get(1.0,"end-1c")
            inputtxt.delete(1.0,"end-1c")
            existRatLabel.config(text="Bitte gebe Notizen zur Gesundheit ein: ")
        case 5: 
            newRatAppend5 =inputtxt.get(1.0,"end-1c")
            inputtxt.delete(1.0,"end-1c")
            existRatLabel.config(text="Bitte gebe benutzte Medikamente ein: ")
        case 6:
            newRatAppend6 =inputtxt.get(1.0,"end-1c")
            inputtxt.delete(1.0,"end-1c")
            print("meds")
            existRatLabel.config(text="Drücke Fertig, um die Addition abzuschließen.")
            buttonStart.config(text = "Fertig", command=partial(ratNewCommit))


##########################################################################################################################################################
    
def ratNewCommit(): #Actually writes the contents to the file (or is supposed to, later.) This gives the user the chance to stop the process
    global hasButNew, buttonNew, buttonDel
    with open ("Speck.json", 'r') as db:
        ratNewDict = json.load(db)
        ratNewDict['name'].append(newRatAppend1)
        ratNewDict['age'].append(newRatAppend2)
        ratNewDict['gen'].append(newRatAppend3)
        ratNewDict['w1'].append(newRatAppend4)
        ratNewDict['health'].append(newRatAppend5)
        ratNewDict['meds'].append(newRatAppend6)


    buttonStart.config(text="OK", command=ratOpen)
    buttonNew.config(text = "Neue Ratte", command=partial(ratNewUI))
    hasButNew = 0
    labelHead.config(text= "Gebe hier einen Namen deiner Ratten ein, um Information über diese zu bekommen:")
    buttonDel= tk.Button(text = "Ratte entfernen", command=partial(ratDelUI), height= 1, width=22)
    buttonDel.pack()

    with open("Speck.json", 'w') as db:
            json.dump(ratNewDict, db)
    existRatLabelUpdate()
##########################################################################################################################################################

def ratNewCancel(): #This cancels all changes and reverts to the normal interface. Despite the name, used both for ratNew and ratDel. changing name is work.
    global hasButNew, buttonDel, confirmConfirm
    existRatLabelUpdate()
    buttonStart.config(text="OK", command=ratOpen)
    buttonNew.config(text = "Neue Ratte", command=partial(ratNewUI))
    labelHead.config(text= "Gebe hier einen Namen deiner Ratten ein, um Information über diese zu bekommen:")
    inputtxt.delete(1.0,"end-1c")
    buttonDel= tk.Button(text = "Ratte entfernen", command=partial(ratDelUI), height= 1, width=22)
    buttonDel.pack()

    hasButNew = 0
    confirmConfirm= 0

##########################################################################################################################################################

def ratDelUI():
    global existRatLabel, buttonDel, buttonNew, hasFrame
    buttonStart.config(text="OK", command=ratDelCommit)
    existRatLabel.config(text="Bitte gebe den Namen der Ratte ein, deren Daten du löschen willst:")
    buttonNew.config(text="Abbrechen", command=partial(ratNewCancel))
    buttonDel.destroy()
    if hasFrame == 1:
        frame1.destroy()
        hasFrame = 0

##########################################################################################################################################################

def ratDelCommit():
    global confirmConfirm, ratNumber, buttonDel
    x = 0
    ratSelect =  inputtxt.get(1.0,"end-1c") #All rats will be in one .json file, to cut down on filesize. therefore, this will be used to find the place of the rat's attributes
    with open("Speck.json", 'r') as db:
        ratList = json.load(db) #opens the rat file and reads out all the attributes.
        for iteRat in ratList["name"]:
            if iteRat == ratSelect:
                ratNumber = x
            else:
                x += 1
    if confirmConfirm == 1:            
        del(ratList['name'][ratNumber])
        del(ratList['age'][ratNumber])
        del(ratList['gen'][ratNumber])
        del(ratList['w1'][ratNumber])
        del(ratList['health'][ratNumber])
        del(ratList['meds'][ratNumber])
        confirmConfirm = 0
        with open("Speck.json", 'w') as db:
            json.dump(ratList, db)
        ratNewCancel()
        existRatLabelUpdate()

    else:
        existRatLabel.config(text="Bitte stelle sicher, dass du wirklich diese Ratte löschen möchtest, dann drücke erneut auf OK.")
        confirmConfirm = 1 
    

##########################################################################################################################################################

def existRatLabelUpdate(): #I transformed this into its own function, so it can be called in different places. probably slightly slower, as the file needs to be opened an additional time.
    ratLabelNameTemp = ""
    with open("Speck.json", 'r') as db:
            ratList = json.load(db)
            for iteRat in ratList["name"]:
                ratLabelNameTemp = ratLabelNameTemp + iteRat + " "
    existRatLabel.config(text=ratLabelNameTemp)

##########################################################################################################################################################

def ratChangeDone(ratChangeNumber):
    with open ("Speck.json", 'r') as db:
        ratChangeDict = json.load(db)
        outputChangeText = inputChangeText.get(1.0, "end-1c"),
    match ratChangeNumber:
        case 1:
            ratChangeDict['name'][ratNumber] = outputChangeText[0]
        case 2:
            ratChangeDict['age'][ratNumber] = outputChangeText[0]
        case 3:
            ratChangeDict['gen'][ratNumber] = outputChangeText[0]
        case 4:
            ratChangeDict['w1'][ratNumber] = outputChangeText[0]
        case 5:
            ratChangeDict['health'][ratNumber] = outputChangeText[0]
        case 6:
            ratChangeDict['meds'][ratNumber] = outputChangeText[0]    
    with open ("Speck.json", 'w', encoding='utf-8') as db:
        json.dump(ratChangeDict, db)
    inputChangeText.destroy()
    existRatLabelUpdate()
    ratOpen()

##########################################################################################################################################################

def ratOpen():
    global frame1, hasFrame, ratNumber
    if hasFrame == 1:
        frame1.destroy()
        hasFrame = 0
    frame1 = tk.Frame(window, height="200", width="1000")
    frame1['borderwidth'] = '20'
    frame1['relief'] = 'sunken'
    frame1.columnconfigure(0, weight = 1)
    frame1.columnconfigure(0, weight = 3)
    frame1.pack()
    hasFrame = 1    

    labelResult1 = tk.Label(frame1, text = "")
    labelResult1.grid(column=0,row=0, sticky=tk.W, padx=5)

    labelResult2 = tk.Label(frame1, text = "")
    labelResult2.grid(column=0,row=1, sticky=tk.W, padx=5)

    labelResult3= tk.Label(frame1, text = "")
    labelResult3.grid(column=0,row=2, sticky=tk.W, padx=5)
    
    labelResult4 = tk.Label(frame1, text = "")
    labelResult4.grid(column=0,row=3, sticky=tk.W, padx=5)

    labelResult5 = tk.Label(frame1, text = "")
    labelResult5.grid(column=0,row=4, sticky=tk.W, padx=5)

    labelResult6= tk.Label(frame1, text = "")
    labelResult6.grid(column=0,row=5, sticky=tk.W, padx=5)
    try:
        global ratSelect, ratLabelName
        x = 0
        ratSelect =  inputtxt.get(1.0,"end-1c") #All rats will be in one .json file, to cut down on filesize. therefore, this will be used to find the place of the rat's attributes
        with open("Speck.json", 'r') as db:
            ratList = json.load(db) #opens the rat file and reads out all the attributes.
            for iteRat in ratList["name"]:
                if iteRat == ratSelect:
                    ratNumber = x
                else:
                    x += 1

        labelResult1.config(text = "Name: " + ratList["name"][ratNumber]) #This shows each attribute as its own, small label. 
        labelResult2.config(text = "Alter: " + ratList["age"][ratNumber])  
        labelResult3.config(text = "Geschlecht: " + ratList["gen"][ratNumber])
        labelResult4.config(text = "Gewicht: " + ratList["w1"][ratNumber])
        labelResult5.config(text = "Gesundheit: " + ratList["health"][ratNumber])  
        labelResult6.config(text = "Medizin: " + ratList["meds"][ratNumber])


        buttonChange1 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,1)) #These are the buttons to change a rat attribute.
        buttonChange1.grid(column=2,row=0)

        buttonChange2 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,2))
        buttonChange2.grid(column=2,row=1)

        buttonChange3 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,3))
        buttonChange3.grid(column=2,row=2)

        buttonChange4 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,4))
        buttonChange4.grid(column=2,row=3)

        buttonChange5 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,5))
        buttonChange5.grid(column=2,row=4)

        buttonChange6 = tk.Button(frame1, text = "Anpassen", command=partial(ratChange,6))
        buttonChange6.grid(column=2,row=5)

        window.mainloop()

    except:
        labelResult1.config(text = "Bitte geben einen Namen ein, der im System vorhanden ist!")

##########################################################################################################################################################

window = tk.Tk()
window.geometry('600x600') #todo: find a good resolution 
window.title("iRattus") #Name is WIP.

labelHead = tk.Label(window, text= "Gebe hier einen Namen deiner Ratten ein, um Information über diese zu bekommen:")
labelHead.pack()

existRatLabel = tk.Label(text="")
existRatLabel.pack()
existRatLabelUpdate()

inputtxt = tk.Text(window,height = 1,width = 20)
inputtxt.pack()

buttonStart= tk.Button(text="OK", command=ratOpen, height= 1, width=22) 
buttonStart.pack() #Ideally, I would have done this in a grid. What a fool I am.

buttonNew= tk.Button(text = "Neue Ratte", command=partial(ratNewUI), height= 1, width=22)
buttonNew.pack()

buttonDel= tk.Button(text = "Ratte entfernen", command=partial(ratDelUI), height= 1, width=22)
buttonDel.pack()

window.mainloop()