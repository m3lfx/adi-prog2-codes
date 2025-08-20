import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.celsius_frame = tkinter.Frame(self.main_window)
        self.farenheit_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.celsius_label = tkinter.Label(self.celsius_frame, text='Enter the temperature in celsius: ')
        self.celsius_entry = tkinter.Entry(self.celsius_frame, width=10)
        self.celsius_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        self.result_label = tkinter.Label(self.farenheit_frame, text='Farenheit:')
        self.temperature = tkinter.StringVar() # To update avg_label
        self.temp_label = tkinter.Label(self.farenheit_frame, textvariable=self.temperature)
        self.result_label.pack(side='left')
        self.temp_label.pack(side='left')

        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame, text='convert', command=self.convert)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.celsius_frame.pack()
        self.farenheit_frame.pack()
        self.button_frame.pack()
        # Start the mainloop.
        tkinter.mainloop()
    
    def convert(self):
        self.temp = float(self.celsius_entry.get())
        self.result = 9/5 * self.temp + 32.0
        self.temperature.set(self.result) 

  

# Create an instance of the MyGUI class.
my_gui = MyGUI()