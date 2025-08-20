

import pyfirmata2
import time
import tkinter as tk

HIGH = 1
LOW = 0 
port = 'COM3'# Windows

board = pyfirmata2.Arduino(port)
led_pin = board.get_pin('d:13:o')  # Use pin 13
led_pin_dim = board.get_pin('d:11:p') #pin pwm 3,5,6,9,10,11

def turn_on_led():
    led_pin.write(HIGH)

def turn_off_led():
    led_pin.write(LOW)

def fade_in_led():
    
    # for i in range(int(val), 5):
    for brightness in range(0, 256):
        print(brightness)
        led_pin_dim.write(brightness/100.0)
        time.sleep(0.02)
    

def fade_out_led(val):
    for i in range(int(val), -1, -1):
        led_pin_dim.write(i/100.0)
        time.sleep(0.02)

def close_window():
    turn_off_led()
    board.exit()
    root.destroy()

# def dim_led():


   

    # for i in range(100, -1, -1):
    #     led_pin_dim.write(i/100.0)
    #     time.sleep(0.02)

root = tk.Tk()
root.title("Arduino LED Control")

on_button = tk.Button(root, text="Turn ON LED", command=turn_on_led, width=20)
on_button.pack(pady=10)

off_button = tk.Button(root, text="Turn OFF LED", command=turn_off_led, width=20)
off_button.pack(pady=10)



# scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=show_value, label="Volume")
# scale.pack(pady=10)

tk.Label(root, text="Name:").pack(pady=10)
led_dim_entry = tk.Entry(root, ) 
led_dim_entry.pack(pady=10)

fade_off_button = tk.Button(root, text="DIM LED", command=lambda: fade_out_led(led_dim_entry.get()), width=20)
fade_off_button.pack(pady=10)

fade_in_button = tk.Button(root, text="DIM in LED", command=lambda: fade_in_led(), width=20)
fade_in_button.pack(pady=10)

close_button = tk.Button(root, text="Close", command=close_window, width=20)
close_button.pack(pady=10)

root.mainloop()