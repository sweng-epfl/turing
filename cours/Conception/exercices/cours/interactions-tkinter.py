import tkinter as tk
import tkinter.messagebox as msg

def tkinter_show(text):
    msg.Message().show(message=text, type=msg.OK)

def tkinter_input(description):
    window = tk.Tk()
    tk.Label(window, text=description).grid(row=0)
    e = tk.Entry(window)
    e.grid(row=0, column=1)
    tk.Button(window, text='OK', command=lambda: window.quit() if e.get() else None).grid(row=1)
    tk.mainloop()
    result = e.get()
    window.destroy()
    return result
