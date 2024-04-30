from tkinter import *
import calendar

def showCalendar():
    year = int(year_field.get())
    gui = Toplevel()
    gui.title("Calendar for the year")
    gui.geometry("550x600")
    gui.config(background='grey')
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.pack()

if __name__ == '__main__':
    root = Tk()
    root.config(background='grey')
    root.title("Calendar")
    root.geometry("250x140")

    cal = Label(root, text="Calendar", bg='grey', font=("times", 28, "bold"))
    year = Label(root, text="Enter year", bg='dark grey')
    year_field = Entry(root)
    button = Button(root, text='Show Calendar', fg='Black', bg='Blue', command=showCalendar)

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)

    root.mainloop()
