from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

reps=0
ticks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, ticks
    ticks=""
    reps=0
    ticks_label.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Start")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer ():
    global reps,ticks
    reps += 1

    if reps%9==0:
        ticks=""
        ticks_label.config(text=ticks)

    work_seconds = WORK_MIN*60
    short_break_seconds = SHORT_BREAK_MIN*60
    long_break_seconds = LONG_BREAK_MIN*60

    if reps%8==0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_seconds)
        ticks=f"{ticks}✓"
        ticks_label.config(text=ticks)
    elif reps%2==0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_seconds)
        ticks=f"{ticks}✓"
        ticks_label.config(text=ticks)
    else:
        timer_label.config(text="Focus", fg=GREEN)
        countdown(work_seconds)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time):
    global reps, timer
    if time>=0:
        timerr = f"{int(time//60) :02d}:{int(time%60) :02d}"
        canvas.itemconfig(timer_text, text=timerr )
        timer = window.after(1000, countdown, time-1)
    elif reps%8!=0:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = Label(text="Start", fg=RED, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
ticks_label = Label(text="",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))

start_button = Button(text="Start", bg=YELLOW, command=start_timer)
reset_button = Button(text="Reset", bg=YELLOW, command=reset_timer)

timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
ticks_label.grid(row=3, column=1)
reset_button.grid(row=2, column=2)

window.mainloop()