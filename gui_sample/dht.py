import pyfirmata2
import time
import sys
from pyfirmata2 import Arduino
import csv
import matplotlib.pyplot as plt
from datetime import datetime

board = None
port = "COM6"
pin = 3
pin_ldr = 1
HIGH = 1
LOW = 0
filename = "temp_humidity.csv"

def main():
    global led_pin_12
    try:
        connect_arduino(port)
        led_pin_12 = board.get_pin("d:12:o")
        
        while True:
            read_analog_pin(pin)
            read_ldr_pin(pin_ldr)
            time.sleep(10)
            
    except KeyboardInterrupt:
        board.exit()
        temp_data, humid_data, time_data = read_data(filename)
        # print(temp_data, humid_data, time_data)

        plot_data(temp_data, humid_data, time_data)


def connect_arduino(port):
    
    global board
    
    try:
        print(f"Connecting to Arduino on port {port}...")
        board = Arduino(Arduino.AUTODETECT)
        
        print("Connected successfully!")
        time.sleep(2)  # Give Arduino time to initialize
        return True
        
    except Exception as e:
        print(f"Failed to connect to Arduino: {e}")
        return False
    
def disconnect_arduino():
    global board
    
    if board:
        board.exit()
        print("Disconnected from Arduino")

def read_analog_pin(pin):
   
    global board
    
    if not board:
        print("Arduino not connected")
        return None
    
    try:
        board.samplingOn(5000)

        # Give time for reading to stabilize if needed
        board.analog[pin].register_callback(dht11_read)
        board.analog[pin].enable_reporting()


        # 
        
    except Exception as e:
        print(f"Error reading analog pin A{pin}: {e}")
        return None

def dht11_read(data):
    print(f"Analog Pin  Reading: {data}")
    current_datetime = datetime.now()
    
    current_datetime = current_datetime.replace(microsecond=0)
    print(current_datetime)
    temperature, humidity = convert_dht11_values(data)
    print(f"DHT11 - Raw: {data:.3f}, Temp: {temperature}°C, , Humidity: {humidity}%")
    write_data(temperature, humidity, current_datetime )

def convert_dht11_values(analog_value):
    # print( analog_value)
    temperature = analog_value * 50
    humidity = 20 + (analog_value * 70)
   
    print(temperature, humidity)
    return round(temperature, 2), round(humidity, 2) 

def write_data(temperature, humidity, cur_time):
    temperature_file = open(filename, 'a', newline='')
    writer = csv.writer(temperature_file)
    writer.writerow([cur_time, temperature, humidity])


def read_data(filename):
   
    temperature_file = open(filename, 'r', newline='')
    
    reader = csv.reader(temperature_file)
    temp_data = []
    humid_data = []
    time_data = []
    
    for row in reader:
        time_data.append(row[0])
        temp_data.append(row[1])
        humid_data.append(row[2])

        # temp_humid_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        # time_data.append(temp_humid_date)
        
        
    return temp_data, humid_data, time_data

def plot_data(temp, hums, time_data):
    plt.title("Arduino DHT data")
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.plot(time_data, temp, color='red')
    ax1.set_ylabel('Temperature (°C)')
    ax1.set_title('Temperature and Humidity over Time')

    # Plot humidity on the second subplot
    ax2.plot(time_data, hums, color='blue')
    ax2.set_xlabel('Time (units)')
    ax2.set_ylabel('Humidity (%)')

    # Adjust layout to prevent overlapping titles/labels
    plt.tight_layout()
    
    plt.show()


def read_ldr_pin(pin_ldr):
   
    global board
    
    if not board:
        print("Arduino not connected")
        return None
    try:
        board.samplingOn(5000)

        # Give time for reading to stabilize if needed
        board.analog[pin_ldr].register_callback(read_ldr)
        board.analog[pin_ldr].enable_reporting()

    except Exception as e:
        print(f"Error reading analog pin A{pin}: {e}")
        return None
    
def read_ldr(data):
    global led_pin_12
    # print(data)
    ldr_value = float(data * 1000)
    print("ldr", ldr_value )
    
    if (ldr_value > 50):
        led_pin_12.write(HIGH)
    else:
      led_pin_12.write(LOW)

main()