import tkinter as tk
from tkinter import messagebox, ttk
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

filename = "temp_humidity.csv"

def main():
    root = tk.Tk()
    root = root
    root.title("Main Application - Menu Window Demo")
    root.geometry("600x400")
    root.configure(bg='#f0f0f0')
    top_frame = tk.Frame(root)
    top_frame.pack()
    create_menu(root)
    show_table(top_frame, filename)
    plot_data(root, filename)
    root.mainloop()

def create_menu(root):
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # Windows Menu
    windows_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Reports", menu=windows_menu)
    windows_menu.add_command(label="Temperature", command=lambda: open_temp_viewer('window_dht.py') )
   
    windows_menu.add_separator()

    tools_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="LED", menu=tools_menu)
    tools_menu.add_command(label="Status", command=lambda: open_led_viewer('led_gui.py')  )

def open_temp_viewer(filename):
    os.chdir("D:\\python-lec\\dht") 
    os.system('python '+ filename)

def open_led_viewer(filename):
    os.chdir("D:\\python-lec\\dht") 
    os.system('python '+ filename)

def read_data(filename):
   
    temperature_file = open(filename, 'r', newline='')
    
    reader = csv.reader(temperature_file)
    temp_data = []
    humid_data = []
    time_data = []
    
    for row in reader:
        temp_data.append(row[1])
        humid_data.append(row[2])

        # temp_humid_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        # time_data.append(temp_humid_date)
        time_data.append(row[0])
        
    return temp_data, humid_data, time_data

def plot_data(root, filename):
    temp_data, humid_data, time_data = read_data(filename)
    plt.title("Arduino DHT data")
    fig = plt.Figure(figsize=(6, 4), dpi=800)
    # ax = fig.add_subplot(111)
    fig, (ax1, ax2) = plt.subplots(2, 1,  sharex=True)

    ax1.plot(time_data, temp_data, color='red')
    ax1.set_ylabel('Temperature (°C)')
    ax1.set_title('Temperature and Humidity over Time')

    # Plot humidity on the second subplot
    ax2.plot(time_data, humid_data, color='blue')
    ax2.set_xlabel('Time (units)')
    ax2.set_ylabel('Humidity (%)')

    # Adjust layout to prevent overlapping titles/labels
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # 5. Draw the canvas
    canvas.draw()

def show_table(frame, filename):
    # Create a new window for the table
    

    # Create a Treeview widget
    tree = ttk.Treeview(frame, show="headings", columns=('time', 'temp', 'hum') )
    tree.heading("time", text="time")  # For the default tree label column
    tree.heading("temp", text="temperature")
    tree.heading("hum", text="humidity")
    tree.pack(padx=10, pady=10, expand=True, fill='both')

    # Read the CSV file
    csvfile = open(filename, 'r', newline='')
   
    reader = csv.reader(csvfile)
    rows = list(reader)
    print(rows)
    if not rows:
        return
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
        
    csvfile.close()
   
main()