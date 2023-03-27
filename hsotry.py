from tkinter import *
from functools import partial   # To prevent unopened windows.

class Converter:

    def __init__(self):

        # Initialize variables such as the feedback variable

        # Common Button Format
        button_font = ("Arial", "12", "bold")
        button_fg = "#232023"

        
        self.all_calculations = ['1 FÅã is -17 CÅã', '54 FÅã is 12 CÅã', 
                                 '6 CÅã is 43 FÅã', '-45 FÅã is -43 CÅã', 
                                 '4 FÅã is -16 CÅã', '5 CÅã is 41 FÅã']

        # GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()


        # Help/Info & History/Export Buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_history_button = self.history_or_info_button = Button(
            self.button_frame, text="History/Export", bg="#e1d5e7", 
            fg=button_fg, font=button_font, width=12, command=self.to_history)
        self.history_or_info_button.grid(row=1, column=0, padx=5, pady=5)

        # Flag to check if the history window is open
        self.history_window_open = False


    def to_history(self):
        # Disable the Help/Info button and open the history window
        self.to_history_button.config(state=DISABLED)
        DisplayHelp(self)


class DisplayHelp:
    def __init__(self, partner):
        background = "#f9f4ff"

        self.history_box = Toplevel()

        partner.history_window_open = True
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        self.history_frame  = Frame(self.history_box, width=300, height=200, bg=background)
        self.history_frame.grid()
        self.history_heading_label = Label(self.history_frame, bg=background, 
                                        text="Help/Info", 
                                        font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)
        
        history_text = "Below are your recent calculations - " \
            "showing 3/3 calculations. " \
            "All calculations are shown to the nearest degree"
        
        self.text_instructions_label = Label(self.history_frame, 
                                             text=history_text,
                                             width=45, justify="left",
                                             wraplength=300,
                                             padx=10, pady=10)
        self.text_instructions_label.grid(row=1)
        
        self.all_calcs_label = Label(self.history_frame,
                                     text="calculations go here",
                                     padx=10, pady=10, bg="#ffe6cc",
                                     width=40, justify="left")
        self.all_calcs_label.grid(row=2)
        
        # instructions for saving files
        save_text = "Either choose a custom file name (and push " \
            "<Export>) or simply push <Export> to save your " \
            "calculation in a text file. If the " \
            "filename already exists, it will be overwritten!"
        self.save_instructions_label = Label(self.history_frame,
                                             text=save_text,
                                             wraplength=300,
                                             justify="left", width=40,
                                             padx=10, pady=10)
        self.save_instructions_label.grid(row=3)
        
        # Filename entry widget
        self.filename_entry = Entry(self.history_frame,
                                    font=("Arial", "14"),
                                    bg="#ffffff", width=25)
        self.filename_entry.grid(row=4, padx=10, pady=10)
        
        self.filename_error_label = Label(self.history_frame,
                                          text="filename error",
                                          fg="#9C0000",
                                          font=("Arial", "12", "bold"))
        self.filename_error_label.grid(row=5)
        
        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)
        
        self.export_button = Button(self.button_frame, font=("Arial", "12", "bold"),
                                    text="Export", bg="#004C99", fg="#FFFFFF",
                                    width=12)
        
        self.dismiss_button = Button(self.history_frame, font=("Arial", "12", "bold"), 
                                     text="Dismiss", bg="#e1d5e7", fg="#232023",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=7, padx=10, pady=10)

    
    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()
            

# Main Program
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
