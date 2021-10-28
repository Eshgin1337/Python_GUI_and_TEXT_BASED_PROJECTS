import tkinter
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN*60
    short_break_seconds = SHORT_BREAK_MIN*60
    long_break_seconds = LONG_BREAK_MIN*60
    if reps % 2 == 1:
        count_down(work_seconds)
        label.config(text="Work Time", fg=GREEN)
    elif reps % 8 == 0:
        label.config(text="Long Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        label.config(text="Short Break", fg=PINK)
        count_down(short_break_seconds)
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
            check_mark_label.config(text=mark)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = tkinter.Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 40, "bold"))
label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_mark_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
check_mark_label.grid(row=3, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_png = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_png)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
