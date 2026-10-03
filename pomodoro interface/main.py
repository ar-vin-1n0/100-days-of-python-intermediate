
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0

timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    timer_txt.config(text="Timer",fg=GREEN,bg=YELLOW)
    canvas.itemconfig(timer_head, text="00:00")
    check_mark.config(text="")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS ,timer_txt
    REPS += 1

    if REPS % 8 == 0:
       count_down(LONG_BREAK_MIN*60)
       timer_txt.config(text="Break",fg=RED,bg=YELLOW)
    elif REPS % 2 == 0:
       count_down(SHORT_BREAK_MIN*60)
       timer_txt.config(text="Break",fg=PINK,bg=YELLOW)
    else:
        count_down(WORK_MIN * 60)
        timer_txt.config(text="Work",fg=GREEN,bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_head, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(REPS / 2)):
            marks += "✓"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(window,width=200,height=224,bg=YELLOW,highlightthickness=0)

timer_txt = Label(text="timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
timer_txt.grid(row=0,column=1)

tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_png)
timer_head = canvas.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="start",width=10,highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="reset",width=10,highlightthickness=0,command=reset)
reset_button.grid(row=2,column=2)

check_mark = Label(font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)


window.mainloop()