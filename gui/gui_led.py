import pyfirmata2
import time
import tkinter as tk

port = 'COM5'  # Windows

board = pyfirmata2.Arduino(port)

led_pin = board.get_pin('d:11:o')  # Use pin 12

HIGH = 1
LOW = 0
class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tk.Tk()
        
        self.main_window.title("Arduino LED Control")

        self.on_button = tk.Button(self.main_window, text="Turn ON LED", command=self.turn_on_led, width=20)
        self.on_button.pack(pady=10)

        self.off_button = tk.Button(self.main_window, text="Turn OFF LED", command=self.turn_off_led, width=20)
        self.off_button.pack(pady=10)

        self.close_button = tk.Button(self.main_window, text="Close", command=self.on_closing, width=20)
        self.close_button.pack(pady=10)

        

        # Enter the tkinter main loop.
        tk.mainloop()

    def turn_on_led(self):
        led_pin.write(HIGH)

    def turn_off_led(self):
        led_pin.write(LOW)

    def on_closing(self):
        self.turn_off_led()
        board.exit()
        self.main_window.destroy()
    
    
    

# Create an instance of the MyGUI class.
my_gui = MyGUI()



