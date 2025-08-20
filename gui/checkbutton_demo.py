# This program demonstrates a group of Checkbutton widgets.
import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tk.Tk()

        # Create two frames. One for the checkbuttons
        # and another for the regular Button widgets.
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Create three IntVar objects to use with the Checkbuttons.
        self.cb_var1 = tk.StringVar()
        # self.cb_var1 = tk.IntVar()
        self.cb_var2 = tk.IntVar()
        self.cb_var3 = tk.IntVar()

        # Set the intVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        # Create the Checkbutton widgets in the top_frame.
        self.cb1 = tk.Checkbutton(self.top_frame, text='Option 1', variable=self.cb_var1, onvalue="remember me")
        self.cb2 = tk.Checkbutton(self.top_frame, text='Option 2', variable=self.cb_var2, onvalue=200)
        self.cb3 = tk.Checkbutton(self.top_frame, text='Option 3', variable=self.cb_var3, onvalue=300)

        # self.cb1 = tk.Checkbutton(self.top_frame, text='Option 1', variable=self.cb_var1, )
        # self.cb2 = tk.Checkbutton(self.top_frame, text='Option 2', variable=self.cb_var2, )
        # self.cb3 = tk.Checkbutton(self.top_frame, text='Option 3', variable=self.cb_var3, )
        # Pack the Checkbuttons.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Create an OK button and a Quit button.
        self.ok_button = tk.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop.
        tk.mainloop()

    # The show_choice method is the callback function for the OK button.
    def show_choice(self):
        # Create a message string.
        self.message = 'You selected:\n'

        # Determine which Checkbuttons are selected and
        # build the message string accordingly.
        if self.cb_var1.get() == "remember me":
            print(self.cb_var1.get())
            self.message = f"{self.message} {self.cb_var1.get()}\n"
            # self.message = f"{self.message} 1\n"
        if self.cb_var2.get() == 200:
            # self.message = self.message + '2\n'
            self.message = f"{self.message} {self.cb_var2.get()}\n"
        if self.cb_var3.get() == 300:
            # self.message = self.message + '3\n'
            self.message = f"{self.message} {self.cb_var3.get()}\n"

        # Display the message in an info dialog box.
        tk.messagebox.showinfo('Selection', self.message)

# Create an instance of the MyGUI class.
my_gui = MyGUI()