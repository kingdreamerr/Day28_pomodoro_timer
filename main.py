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
