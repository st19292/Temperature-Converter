from tkinter import *

class Converter:

    def __init__(self):

        # Common Button Format
        button_font = ("Arial", "12", "bold")
        button_fg = "#232023"


        # GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "24", "bold"))
        self.temp_heading.grid(row=0)

        instructions = "Enter a number that you want to convert, whether from Celcius to Farenheit." \
                        " Then, click a button to convert your number."
        self.temp_instructions = Label(self.temp_frame, text=instructions,
                                        font=("Arial", "10"), wrap=500, width=80, justify="center")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Arial", "15"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error_msg = "Please enter a number."
        self.temp_error = Label(self.temp_frame, text=error_msg,
                                        fg="#9C0000", font=("Arial", "9"), wrap=500, width=80, justify="center")
        self.temp_error.grid(row=3)

        # Help/Info & History/Export Buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)
        
        self.to_celcius_button = Button(self.button_frame, text="To Degrees",
                                       bg="#ffe6cc", fg=button_fg, font=button_font, width=12)
        self.to_celcius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = Button(self.button_frame, text="To Farenheit",
                                       bg="#fff2cc", fg=button_fg, font=button_font, width=12)
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_or_info_button = Button(self.button_frame, text="Help/Info",
                                       bg="#e1d5e7", fg=button_fg, font=button_font, width=12)
        self.help_or_info_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_or_export_button = Button(self.button_frame, text="History/Export",
                                       bg="#dae8fc", fg=button_fg, font=button_font, width=12, state=DISABLED)
        self.history_or_export_button.grid(row=1, column=1, padx=5, pady=5)

# Main Program
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
