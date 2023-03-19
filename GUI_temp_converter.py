from tkinter import *

class Converter:

    def __init__(self):

        # GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "20", "bold"))
        self.temp_heading.grid(row=0)

        instructions = "Enter a number that you want to convert, whether from Celcius to Farenheit." \
                        " Then, click a button to convert your number."
        self.temp_instructions = Label(self.temp_frame, text=instructions,
                                        wrap=500, width=80, justify="center")
        self.temp_instructions.grid(row=1)

# Main Program
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()

