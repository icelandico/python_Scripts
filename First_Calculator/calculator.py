import tkinter

mainWindow = tkinter.Tk()
mainWindow.title('First calculator moja droga Isiu')
mainWindow.geometry('240x200')
mainWindow['padx'] = 10
# mainWindow.minsize(width=220, height=200)

2
#rows and columns definition
# mainWindow.columnconfigure(0, weight=1)
# mainWindow.columnconfigure(1, weight=1)
# mainWindow.columnconfigure(2, weight=1)
# mainWindow.columnconfigure(3, weight=1)
#
# mainWindow.rowconfigure(0, weight=1)
# mainWindow.rowconfigure(1, weight=1)
# mainWindow.rowconfigure(2, weight=1)
# mainWindow.rowconfigure(3, weight=1)
# mainWindow.rowconfigure(4, weight=1)
# mainWindow.rowconfigure(5, weight=1)

# Result field

resultField = tkinter.Entry(mainWindow)
resultField.grid(row=0, column = 0,sticky='nsew', columnspan=4)
# resultStr = tkinter.Label(mainWindow, text='Here\'s the result' )
# resultStr.grid(row=0, column=4, sticky ='w')


#Buttons
numbgr = [0,1,2,3,4,5]
rows = [5,5,4,4,4,4,3,3,3,3,2,2,2,2,1,1]
columns = [0,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1]
numtext = [0, '/', 1,2,3,'*', 4,5,6,'-',7,8,9,'+','C','CE']


for i in range(len(numtext)):
    btn =tkinter.Button(mainWindow, text=numtext[i], relief='raised', width=6)
    btn.grid(row=rows[i], column=columns[i], sticky ='w')
equal = tkinter.Button(mainWindow, text='=')
equal.grid(row=5, column=1, columnspan=2, sticky='nsew')

mainWindow.update()
mainWindow.minsize(btn.winfo_width() + 180, resultField.winfo_height()+ 180)
mainWindow.maxsize(btn.winfo_width() + 210, resultField.winfo_height()+ 210)
mainWindow.mainloop()


