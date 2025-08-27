import tkinter as tk
import tkinter.messagebox
import pyfirmata2

port = 'COM6'  # Windows
HIGH = 1
LOW = 0

def main():
    global cb_led1_var, cb_led2_var, led_pin_12, led_pin_9
    board = pyfirmata2.Arduino(port)
    led_pin_12 = board.get_pin("d:12:o")
    led_pin_9 = board.get_pin("d:9:o")
    root = tk.Tk()

    root.geometry("400x400")
    root.title("LED")
    top_frame = tkinter.Frame(root)

    cb_led1_var = tkinter.BooleanVar()
    cb_led2_var = tkinter.BooleanVar()
 
        # Set the intVar objects to 0.
    cb_led1_var.set(0)
    cb_led2_var.set(0)

    cb1 = tk.Checkbutton(top_frame, text='LED 1', variable=cb_led1_var, command=lambda: turn_on_led())
    cb2 = tk.Checkbutton(top_frame, text='LED 2', variable=cb_led2_var, command=lambda: turn_on_led())

    cb1.pack(pady=20)
    cb2.pack(pady=20)
    top_frame.pack()
    tk.mainloop()

def turn_on_led():
    print(port)
    

    if cb_led1_var.get():
        led_pin_12.write(HIGH)
    else:
        led_pin_12.write(LOW)
    
    if cb_led2_var.get():
        led_pin_9.write(HIGH)
    else:
        led_pin_9.write(LOW)

main()