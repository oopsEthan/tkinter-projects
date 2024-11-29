from tkinter import *

# Timer states
WORK = "WORK"
SHORT_BREAK = "SHORT BREAK"
LONG_BREAK = "LONG BREAK"
OFF = "OFF"

# Timer default minutes
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

# Test minutes
# WORK_MIN = 1
# SHORT_BREAK_MIN = 1
# LONG_BREAK_MIN = 1

# Other constants
# ✓
BLACK = "#000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

class Timer(Canvas):
    def __init__(self) -> None:
        super().__init__()
        
        self.timer_state = OFF
        self.timer_state_color = BLACK
        self.timer_rotations = 0

        self.set_timer_visuals()
    
    def set_timer_visuals(self) -> None:
        self.tomato_png = PhotoImage(file="tomato.png")    
        tomato_width, tomato_height = self.tomato_png.width(), self.tomato_png.height()
        self.config(width=tomato_width, height=tomato_height, bg=YELLOW, highlightthickness=0)

        self.create_image(tomato_width/2, tomato_height/2, image=self.tomato_png)

        # self.timer_state_label = self.create_text(tomato_width/2, tomato_height/1.4, text=f"{self.timer_state}", font=(FONT_NAME, 16, "bold"))
        self.timer_text = self.create_text(tomato_width/2, tomato_height/1.75, text="00:00", font=(FONT_NAME, 24, "bold"), fill="#ffffff")
    
    def start_timer(self) -> None:
        if self.timer_state == OFF:
            self.timer_state = WORK
            self.timer_state_color = GREEN
            self.set_timer(WORK_MIN)

    def set_timer(self, minutes) -> None:
        self.time_left = minutes * 60
        self.format_timer()
        self.after(1000, self.countdown)

    def countdown(self) -> None:
        if self.timer_state != OFF:
            if self.time_left == 0:
                self.update_state()
            elif self.time_left > 0:
                self.time_left -= 1
                self.format_timer()
                self.after(1000, self.countdown)
    
    def update_state(self) -> None:
        # Set to short break if work is over and still under 4 rotations
        if self.timer_state == WORK and self.timer_rotations != 4:
            self.timer_rotations += 1
            self.timer_state = SHORT_BREAK
            self.timer_state_color = PINK
            self.set_timer(SHORT_BREAK_MIN)
        
        # Set to work if short break is over and still under 4 rotations
        elif self.timer_state == SHORT_BREAK:
            self.timer_state = WORK
            self.timer_state_color = GREEN
            self.set_timer(WORK_MIN)
        
        # Set to work if long break is over and reset rotations
        elif self.timer_state == LONG_BREAK:
            self.timer_rotations = 0
            self.timer_state = WORK
            self.timer_state_color = GREEN
            self.set_timer(WORK_MIN)
        
        # Set to long break if 4 rotations is over
        elif self.timer_rotations == 4:
            self.timer_state = LONG_BREAK
            self.timer_state_color = RED
            self.set_timer(LONG_BREAK_MIN)
        
        # If something goes wrong, reset completely
        else:
            self.reset_timer()

    def reset_timer(self) -> None:
        self.timer_state = OFF
        self.timer_state_color = BLACK
        self.timer_rotations = 0
        self.time_left = 0
        self.format_timer()

    def format_timer(self) -> None:
        minutes_left = self.time_left // 60
        seconds_left = self.time_left % 60
        # self.itemconfig(self.timer_state_label, text=f"{self.timer_state}")
        self.itemconfig(self.timer_text, text=f"{minutes_left:02}:{seconds_left:02}")