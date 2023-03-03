from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
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




# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_title.config(text="Long Break", fg=RED)
        count_down(long_sec)
    elif reps % 2 == 0:
        timer_title.config(text="Break", fg=PINK)
        count_down(short_break)
    else:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps,timer
    time_minutes = math.floor(count / 60)
    time_seconds = count % 60
    if time_seconds < 10:
        time_seconds = f"0{time_seconds}"
    canvas.itemconfig(text_time, text=f"{time_minutes}:{time_seconds}")
    if count > 0:
       timer = window.after('1000', count_down, count - 1)
    else:
        start_timer()
        complete=""
        work = math.floor(reps/2)
        for _ in range(work):
            complete += "✅"
            mark.config(text=complete)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=image)
text_time = canvas.create_text(103, 130, text="00:00", fill="white",font=(FONT_NAME, 35, 'bold'))
canvas.grid(columnspan=3, row=1)
timer_title = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timer_title.grid(column=1, row=0)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)
mark = Label(bg=YELLOW, font=(FONT_NAME, 15), fg="#07332E")


mark.grid(column=1, row=3)

reset_btn = Button(text="Reset", borderwidth=1, command=reset)
reset_btn.grid(column=2, row=2)

window.mainloop()
