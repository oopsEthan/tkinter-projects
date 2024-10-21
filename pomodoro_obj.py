from tkinter import *

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

class Timer(Canvas):
    def __init__(self):
        super().__init__()
        
        self.timer_state = "OFF"
        self.work_loops = 0

        self.set_image()
    
    def set_image(self):
        self.tomato_png = PhotoImage(file="tomato.png")    
        tomato_width, tomato_height = self.tomato_png.width(), self.tomato_png.height()
        self.config(width=tomato_width, height=tomato_height, bg=YELLOW, highlightthickness=0)

        self.create_image(100, 112, image=self.tomato_png)

        self.timer_text = self.create_text(100, 113, text="00:00", font=(FONT_NAME, 24, "bold"))

    def start_timer(self):
        self.timer_state = "WORK"
        self.set_timer(WORK_MIN)

    def set_timer(self, minutes):
        self.time_left = minutes * 60
        self.format_timer()
        self.after(1000, self.countdown)

    def countdown(self):
        if self.timer_state != "OFF":
            if self.time_left == 0:
                self.update_state()
            elif self.time_left > 0:
                self.time_left -= 1
                self.format_timer()
                self.after(1000, self.countdown)
    
    def update_state(self):
        if self.timer_state == "WORK" and self.work_loops <= 3:
            self.timer_state = "SHORT BREAK"
            self.work_loops += 1
            self.set_timer(SHORT_BREAK_MIN)
        elif self.timer_state == "SHORT BREAK":
            self.timer_state = "WORK"
            self.set_timer(WORK_MIN)
        elif self.timer_state == "LONG BREAK":
            self.timer_state = "WORK"
            self.work_loops = 0
            self.set_timer(WORK_MIN)
        elif self.work_loops >= 3:
            self.timer_state = "LONG BREAK"
            self.set_timer(LONG_BREAK_MIN)
        # If something goes wrong, reset completely
        else:
            self.reset_timer()

    def reset_timer(self):
        self.timer_state = "OFF"
        self.time_left = 0
        self.format_timer()

    def format_timer(self):
        minutes_left = self.time_left // 60
        seconds_left = self.time_left % 60
        self.itemconfig(self.timer_text, text=f"{minutes_left:02}:{seconds_left:02}")