from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title('To do List')
        self.root.geometry('450x300+200+200')
## Labels creation:
        self.l1 =Label(self.root, text='ToDo List',  
        font ='ariel, 10 bold', width =14, bd = 3, bg = '#E9DEDE', fg ='black')
        self.l1.place(x=20, y=20)

        self.l2 =Label(self.root, text='Enter task title: ',  
        font ='ariel, 10 bold', width =14, bd = 3, bg = '#E9DEDE', fg ='black')
        self.l2.place(x=20, y =80)

## Main txt creation for task titles:
        self.main_text = Listbox(self.root, height=11, width=25, selectmode='SINGLE')
        self.main_text.place(x =250, y =50)

## Entry text window:
        self.text = Text(self.root, bd =5, height = 2, width =21, font = 'ariel, 10 bold')
        self.text.place(x=20,y =120)


## Methods : add and delete tasks:


        def addTask():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            
            self.text.delete(1.0, END)

        
        def delOne():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            
            self.main_text.delete(delete_)

        
            
## Buttons for Add and Delete text and Quit

        self.b1 = Button(self.root, text = 'Add Task', font ='sarif, 10 bold italic',
         width =15,bd = 7, bg = '#E5FFCC', fg='black', command = addTask)

        self.b1.place(x=30, y =170)

        self.b2 = Button(self.root, text = 'Delete', font ='sarif, 10 bold italic',
         width =15,bd = 7, bg = '#E5FFCC', fg='black', command = delOne)

        self.b2.place(x=30, y =210)

        self.b3 = Button(self.root, text = 'Quit', font ='sarif, 10 bold italic',
         width =15,bd = 7, bg = '#E5FFCC', fg='black', command = self.root.destroy)
        
        self.b3.place(x=30, y =250)


def main():
    root = Tk()
    window = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    