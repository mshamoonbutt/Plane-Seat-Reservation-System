# RUN MAIN FILE



# Name: Muhammad Shamoon Butt
# Roll No: 271046574
# Lab ID: 6
'''Classes: ReserveSeat, Main Window, SeatGUI, CancelSeat
Resources for help:
https://www.geeksforgeeks.org/python-tkinter-tutorial/
StackOverflow
ChatGPT ( not complete code or design :) )
https://www.youtube.com/playlist?list=PLu0W_9lII9ajLcqRcj4PoEihkukF_OTzA
https://youtu.be/OPUSBBD2OJw?si=uMu0QMKPDHRm5iEt
https://youtu.be/wEv3BworNK8?si=WnU0QZBXf572qvjo
https://youtu.be/t1gDxErjwlc?si=cq9B5SlIwHcUlMRq
https://youtu.be/nSn55h_NVIo?si=P46CydPLd8MQ2aYN
https://youtu.be/JCeBUgbMBak?si=-LhkjorvF1SUm-Xi
https://youtu.be/tpwu5Zb64lQ?si=4girmNIiiqv7nQq1
https://youtu.be/Aim_7fC-inw?si=kCG1RN3ydGLG0Pvv
https://youtu.be/ZWYhXncauUA?si=-f0i9PGjs2xZl8UR
''' 


'''
Main layout: DONE
Plane Seat Layout: DONE
Reserve Seat Layout: DONE
Cancel Seat Layout: DONE
Seats can be reserved: DONE
Box made by loops: DONE 
Box Coloring: DONE
Error Handling: DONE
Updating revenue, cargo, limit: DONE
Save / Load information to file: DONE
Add new plane and select: DONE
Generic plane seating window: NOT DONE(Bit difficult ending project due to finals)
Submit early: DONE
'''


# importing necessary modules and files
import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import *
from pia_management import *
from passenger import *
from gui_windows import *


# defining the main window class
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # creating an instance of PIAManagement class
        self.management = PIAManagement()
        self.current_plane = self.management.get_plane(1)

        # configuring the main window
        self.title("PIA Airline Reservation")
        self.resizable(True, True)
        self.geometry("550x410+180+100")
        self.configure(bg='lightgrey')

        # defining the font for labels
        self.label_font = Font(family="Helvetica", size=15, weight="bold")

        # creating the label for the main window
        self.label = tk.Label(self, text="PIA Ticket Reservation", font=self.label_font, bg="lightgrey")
        self.label.grid(row=0, column=0, columnspan=4, pady=5)

        # creating three frames for different seat classes
        self.frame1 = tk.Frame(self, bg="lightgrey")
        self.frame2 = tk.Frame(self, bg="lightgrey")
        self.frame3 = tk.Frame(self, bg="lightgrey")

        # placing the frames in the main window
        self.frame1.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
        self.frame2.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
        self.frame3.grid(row=1, column=2, padx=1, pady=1, sticky="nsew")

        # configuring the grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # creating titles for each frame
        title1 = tk.Label(self.frame1, text="Business Class", bg="white", font=("Helvetica", 10, "bold"))
        title2 = tk.Label(self.frame2, text="Economy Class", bg="white", font=("Helvetica", 10, "bold"))
        title3 = tk.Label(self.frame3, text="Student Class", bg="white", font=("Helvetica", 10, "bold"))

        # placing the titles in the frames
        title1.pack(side="top", fill="x", padx=1, pady=1)
        title2.pack(side="top", fill="x", padx=1, pady=1)
        title3.pack(side="top", fill="x", padx=1, pady=1)

        # creating listboxes for each frame
        self.box1 = tk.Listbox(self.frame1, width=20, height=18, bg="white", borderwidth=1)
        self.box2 = tk.Listbox(self.frame2, width=20, height=18, bg="white", borderwidth=1)
        self.box3 = tk.Listbox(self.frame3, width=20, height=18, bg="white", borderwidth=1)
        self.box1.pack(side="top", fill="both", expand=True)
        self.box2.pack(side="top", fill="both", expand=True)
        self.box3.pack(side="top", fill="both", expand=True)

        # binding events to listboxes
        self.box1.bind("<<ListboxSelect>>", lambda event: self.on_name_click(event, "Business"))
        self.box2.bind("<<ListboxSelect>>", lambda event: self.on_name_click(event, "Economy"))
        self.box3.bind("<<ListboxSelect>>", lambda event: self.on_name_click(event, "Student"))

        # initializing previous selection
        self.previous_selection = None

        # creating buttons for different actions
        self.btn_reservation = tk.Button(self, text="Seat Reservation", command=self.reserve_seat)
        self.btn_cancellation = tk.Button(self, text="Seat Cancellation", command=self.cancel_seat)
        self.btn_load = tk.Button(self, text="Load from File", command=self.load_from_file)
        self.btn_save = tk.Button(self, text="Save File", command=self.save_to_file)
        self.btn_add_plane = tk.Button(self, text="Add Plane", command=self.add_plane)

        # placing the buttons in the main window
        self.btn_reservation.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.btn_cancellation.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        self.btn_load.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        self.btn_save.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.btn_add_plane.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        # configuring the grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # creating a combobox for plane selection
        self.plane_selection = ttk.Combobox(self, values=["Plane 1"], state="readonly", width=1)
        self.plane_selection.current(0)
        self.plane_selection.grid(row=3, column=2, padx=5, pady=5, sticky="ew")
        self.plane_selection.bind("<<ComboboxSelected>>", self.show_seat_gui)

        # opening the seat GUI
        self.open_seat_gui()

    # method for seat reservation
    def reserve_seat(self):
        ReserveSeatWindow(self)

    # method for seat cancellation
    def cancel_seat(self):
        CancelSeatWindow(self)

    # method for loading data from a file
    def load_from_file(self):
        fname = askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if fname:
            with open(fname, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(" ")
                    if len(parts) == 5:
                        passenger = Passenger(parts[0], parts[1], parts[2], int(parts[3]), float(parts[4]))
                        self.current_plane.add_passenger(passenger)
                self.update_all_guis()

    # method for saving data to a file
    def save_to_file(self):
        fname = asksaveasfile(mode='w', defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if fname:
            for passenger in self.current_plane.passengers:
                fname.write(f"{passenger.name} {passenger.passenger_id} {passenger.seat_class} {passenger.seat_number} {passenger.luggage_weight}\n")
            fname.close()

    # method for adding a new plane
    def add_plane(self):
        self.management.add_plane()
        self.plane_selection['values'] = [f"Plane {plane.plane_number}" for plane in self.management.planes]
        self.plane_selection.current(len(self.management.planes) - 1)
        self.show_seat_gui(None)

    # method for showing the seat GUI
    def show_seat_gui(self, event):
        selected_plane_number = int(self.plane_selection.get().split()[-1])
        self.current_plane = self.management.get_plane(selected_plane_number)
        self.open_seat_gui()

    # method for opening the seat GUI
    def open_seat_gui(self):
        if hasattr(self, 'seat_gui') and self.seat_gui.winfo_exists():
            self.seat_gui.destroy()
        self.seat_gui = SeatGUI(self)
        self.update_all_guis()

    # method for updating the reservation boxes. 
    def update_reservation_boxes(self):
        self.box1.delete(0, tk.END)
        self.box2.delete(0, tk.END)
        self.box3.delete(0, tk.END)
        for passenger in self.current_plane.passengers:
            if passenger.seat_class == "Business":
                self.box1.insert(tk.END, passenger.name)
            elif passenger.seat_class == "Economy":
                self.box2.insert(tk.END, passenger.name)
            elif passenger.seat_class == "Student":
                self.box3.insert(tk.END, passenger.name)

    # method for handling name click event. it highlights the box when repected name is clicked
    def on_name_click(self, event, seat_class):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            name = widget.get(index)
            for passenger in self.current_plane.passengers:
                if passenger.name == name and passenger.seat_class == seat_class:
                    self.update_seat_highlight(passenger)
                    break

    # method for updating the seat highlight. it colors the selected seat to yellow and return to previous color 
    def update_seat_highlight(self, passenger):
        if self.previous_selection:
            self.seat_gui.update_seat_color(self.previous_selection)
        self.seat_gui.highlight_seat(passenger)
        self.previous_selection = passenger

    # method for updating all GUIs
    def update_all_guis(self):
        self.update_reservation_boxes()
        self.seat_gui.update_all_seats()
        self.seat_gui.update_all_info()


# running the main window
if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()