import tkinter as tk
from tkinter import messagebox 
class CalculatorApp:
    def __init__(self,root):
        self.root = root 
        self.root.title("Simple Calculator")
        self.entry = tk.Entry(root, width = 40, borderwidth = 5,font = ('Arial',14))
        self.entry.grid(row = 0,column = 0,columnspan = 5,padx = 10,pady = 10)
        buttons = [ ('7',1,0),('8',1,1),('9',1,2,),('(',1,3),(')',1,4),('4',2,0),('5',2,1),('6',2,2),
                   ('*',2,3),('/',2,4),('1',3,0),('2',3,1),('3',3,2),('+',3,3),('-',3,4),('0',4,0),('.',4,1),
                   ('c',4,2),('=',4,3),('^',4,4)]
        for (text, row, column) in buttons:
            tk.Button(root, text = text, width = 7, height = 2, font = ('Arial',14),
                      command = lambda t=text: self.handle_click(t)).grid(row=row ,column=column, padx=5, pady =5)
            root.bind('<Return>', lambda event: self.handle_click("="))
    def handle_click(self,value):
        current = self.entry.get()
        if value == '=':
            try:
                result = eval(current)
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END,str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
        elif value == 'c':
            self.clear()
        else:
            self.entry.insert(tk.END,value)
    def clear(self):
        self.entry.delete(0,tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()