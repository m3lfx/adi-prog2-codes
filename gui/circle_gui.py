import circle as c 

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.circle_frame = tkinter.Frame(self.main_window)
        self.radius_frame = tkinter.Frame(self.main_window)
        self.area_frame = tkinter.Frame(self.main_window)
        self.area_result_frame = tkinter.Frame(self.main_window)
        self.circuference_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.radius_label = tkinter.Label(self.radius_frame, text='Enter the radius of circle: ')
        self.radius_entry = tkinter.Entry(self.radius_frame, width=10)
        
        self.radius_label.pack(side='left')
        self.radius_entry.pack(side='left')

        self.area_label = tkinter.Label(self.area_frame, text='Area of Circle:')
        self.area = tkinter.StringVar() # To update avg_label
        # self.area_label = tkinter.Label(self.area_frame, textvariable=self.area)
        self.area_label.pack(side='left')

        self.area_result = tkinter.Label(self.area_result_frame, )
        self.area_result = tkinter.StringVar() # To update avg_label
        
        self.area_result.pack(side='left')
       

        # Create and pack the button widgets.
        self.area_button = tkinter.Button(self.button_frame, text='get area', command=lambda: self.get_area(self.radius_entry.get(), self.area_label))
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.area_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.circle_frame.pack()
        self.radius_frame.pack()
        self.button_frame.pack()
        self.area_frame.pack()
        # Start the mainloop.
        tkinter.mainloop()
    
    def get_area(self, radius, rad_label):
        print(radius)
        self.area = c.area(radius)
        print(self.area)
        
        rad_label.config(text=f"{self.area:.2f}")
       

    
   

  

# Create an instance of the MyGUI class.
my_gui = MyGUI()
