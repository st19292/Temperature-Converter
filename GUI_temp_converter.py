from tkinter import *
from functools import partial   # To prevent unopened windows.

class Converter:

    def __init__(self):

        # Initialize variables such as the feedback variable
        self.var_feedback = StringVar()
        self.var_feedback.set("")
        
        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

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
        self.output_label = Label(self.temp_frame, text="",
                                        fg="#9C0000", font=("Arial", "9"), wrap=500, width=80, justify="center")
        self.output_label.grid(row=3)

        # Help/Info & History/Export Buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)
        
        self.to_celcius_button = Button(self.button_frame, text="To Degrees",
                                       bg="#ffe6cc", fg=button_fg, font=button_font, width=12, 
                                       command = lambda: self.temp_convert(-459))
        self.to_celcius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = Button(self.button_frame, text="To Farenheit",
                                       bg="#fff2cc", fg=button_fg, font=button_font, width=12,
                                       command = lambda: self.temp_convert(-273))
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = self.help_or_info_button = Button(self.button_frame, text="Help/Info",
                                       bg="#e1d5e7", fg=button_fg, font=button_font, width=12, command=self.to_help)
        self.help_or_info_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_or_export_button = Button(self.button_frame, text="History/Export",
                                       bg="#dae8fc", fg=button_fg, font=button_font, width=12, state=DISABLED)
        self.history_or_export_button.grid(row=1, column=1, padx=5, pady=5)


    # Temperature Converter
    def check_temp(self, min_value):
        
        has_error = "no"
        error = (f"Please enter a number that is more that {min_value}")

        response = self.temp_entry.get()
        
        try:
            response = float(response)
            
            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"
            
        # Sets var_has_error etc
        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"
        
        # If we have errors
        else:
            self.var_has_error.set("no")
            self.history_or_export_button.config(state=NORMAL)
            return response


    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return "{:.0f}".format(var_rounded)


    # Check Temperature Validity and Converts
    def temp_convert(self, min_val):
        to_convert = self.check_temp(min_val)
        degree_sign = u'\N{DEGREE SIGN}'

        answer = ""
        from_to = ""

        set_feedback = "yes"
        
        if to_convert == "invalid":
            set_feedback = "no"
            
        # Convert to Ceclius 
        elif min_val == -459:
            answer = (to_convert - 32) * 5 / 9
            from_to = "{} F{} is {} C{}"

        # Convert to Farenheit
        else:
            answer = to_convert * 1.8 + 32
            from_to = "{} C{} is {} F{}"

        if set_feedback == "yes":
            to_convert = self.round_ans(to_convert)
            answer = self.round_ans(answer)

            # Create user output and add to calcu;ation history
            feedback = from_to.format(to_convert, degree_sign, answer, degree_sign)
            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)
        
        self.output_answer()


    # Shows user output and clears entry widget for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()
        
        if has_errors == "yes":
            '''Red text, green entry box'''
            self.output_label.config(fg="#9C0000")
            self.temp_entry.config(bg="#F8CECC")
        else:
            self.output_label.config(fg="#004C00")
            self.temp_entry.config(fg="black")
        
        self.output_label.config(text=output)
            
    def to_help(self):
        # Disable the Help/Info button and open the help window
        self.to_help_button.config(state=DISABLED)
        DisplayHelp(self)


class DisplayHelp:
    def __init__(self, partner):
        background = "#f9f4ff"

        self.help_box = Toplevel()

        partner.help_window_open = True
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame  = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()
        self.help_heading_label = Label(self.help_frame, bg=background, 
                                        text="Help/Info", 
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)
        
        help_text = "To use the program, simply enter the temperature " \
            "that you wise to convert and then choose convert to either " \
            "degrees Celcius (centigrade) or Fareheit.. \n\n" \
            "Note that -273 degrees C (-459F) is absolute zero " \
            "(the coldest possible temperature). If you convert a " \
            "temperature that is less than -273C, you will get an error " \
            "message. \n\n" \
            "To see your calculation history and export in to a text file, " \
            "please check the history/export button."
        
        self.help_text_label = Label(self.help_frame, bg=background, 
                                     text=help_text, wrap=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)
        
        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), 
                                     text="Dismiss", bg="#e1d5e7", fg="#232023",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    
    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# Main Program
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
