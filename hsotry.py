from tkinter import *
from functools import partial   # To prevent unopened windows.

class Converter:

    def __init__(self):

        # Initialize variables such as the feedback variable

        # Common Button Format
        button_font = ("Arial", "12", "bold")
        button_fg = "#232023"

        
        # testing only 5 data points
        self.all_calculations = ['1 F* is -17 C*', '54 F* is 12 C*', 
                                 '6 C* is 43 F*', '-45 F* is -43 C*', 
                                 '4 F* is -16 C*']

        # GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()


        # Help/Info & History/Export Buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_history_button = self.history_or_info_button = Button(
            self.button_frame, text="History/Export", bg="#dae8fc", 
            fg=button_fg, font=button_font, width=12, 
            command=lambda: self.to_history(self.all_calculations))
        self.history_or_info_button.grid(row=1, column=0, padx=5, pady=5)

        # Flag to check if the history window is open
        self.history_window_open = False


    def to_history(self, all_calculations):
        # Disable the Help/Info button and open the history window
        self.to_history_button.config(state=DISABLED)
        HistoryExport(self, all_calculations)


class HistoryExport:
    def __init__(self, partner, all_calculations):


        # Maximum number of calculations
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        # Calculation list to string
        calc_string_text = HistoryExport.get_calc_string(all_calculations)
        

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
        

        # Text and Background Changes 
        num_calcs = len(all_calculations)
        if num_calcs > max_calcs:
            '''Peach Color'''
            calc_background = "#FFE6CC"
            showing_all = "Here are your calculations " \
                f"{max_calcs}/{num_calcs} calculations shown. Please export " \
                "your calcultions to see your full calculation " \
                "history"
        else:
            '''Pale Green Color'''
            calc_background = "#B4FACB"
            showing_all = "Below is your calculation history."


        # History Text and Label
        history_text = f"{showing_all} \n\nAll calculations are shown to " \
        "the nearest degree."
        
        self.text_instructions_label = Label(self.history_frame, 
                                             text=history_text,
                                             width=45, justify="left",
                                             wraplength=300,
                                             padx=10, pady=10)
        self.text_instructions_label.grid(row=1)
        
        self.all_calcs_label = Label(self.history_frame,
                             text="\n".join(all_calculations[-5:]),
                             padx=10, pady=10, bg=calc_background,
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
                                     text="Dismiss", bg="#dae8fc", fg="#232023",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=7, padx=10, pady=10)


    @staticmethod
    def get_calc_string(var_calculations):
        # Get maximum calculation to display
        max_calcs = 5
        calc_string = ""

        # Workout how many times to loop
        if len(var_calculations) >= max_calcs:
            stop = max_calcs
        else:
            stop = len(var_calculations)
        
        # Iterate to all but the last item
        for item in range(0, stop - 1):
            calc_string += var_calculations[len(var_calculations) - item - 1]
            '''add final item without final line break'''
            calc_string += "\n"

        calc_string += var_calculations[-max_calcs]
        return calc_string
    
    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()
            

# Main Program
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
