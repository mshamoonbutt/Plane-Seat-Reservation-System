import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox
from passenger import Passenger

# Create a window for reserving a seat
class ReserveSeatWindow(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.title("Reserve a Seat")
        self.geometry("430x220+350+300")

        self.label_font = Font(family="Helvetica", size=10)

        # Create a frame to hold the input fields
        self.info_frame = tk.Frame(self)
        self.info_frame.pack(pady=10)

        # Create labels and entry fields for name, ID, seat class, seat number, and luggage weight
        self.name_label = tk.Label(self.info_frame, text="Name:", font=self.label_font)
        self.name_entry = tk.Entry(self.info_frame, font=self.label_font, bg="white", width=30)
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a validation function for the ID entry field
        def validate_id(input_text):
            return len(input_text) <= 7

        validate_cmd = self.register(validate_id)

        self.id_label = tk.Label(self.info_frame, text="ID:", font=self.label_font)
        self.id_entry = tk.Entry(self.info_frame, font=self.label_font, bg="white", width=30, validate="key", validatecommand=(validate_cmd, '%P'))
        self.id_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.id_entry.grid(row=1, column=1, padx=5, pady=5)

        self.seat_class_label = tk.Label(self.info_frame, text="Seat Class:", font=self.label_font)
        self.seat_class_combobox = ttk.Combobox(self.info_frame, font=self.label_font, values=["Economy", "Business", "Student"], state="readonly", width=28)
        self.seat_class_combobox.current(0)
        self.seat_class_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.seat_class_combobox.grid(row=2, column=1, padx=5, pady=5)

        self.seat_number_label = tk.Label(self.info_frame, text="Seat Number:", font=self.label_font)
        self.seat_number_entry = tk.Entry(self.info_frame, font=self.label_font, bg="white", width=30)
        self.seat_number_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.seat_number_entry.grid(row=3, column=1, padx=5, pady=5)

        self.luggage_weight_label = tk.Label(self.info_frame, text="Luggage Weight (kg):", font=self.label_font)
        self.luggage_weight_entry = tk.Entry(self.info_frame, font=self.label_font, bg="white", width=30)
        self.luggage_weight_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.luggage_weight_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create a button to reserve the seat
        self.reserve_button = tk.Button(self.info_frame, text="Reserve", font=self.label_font, command=self.reserve_seat)
        self.reserve_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Function to reserve a seat
    def reserve_seat(self):
        # Get the values from the input fields
        name = self.name_entry.get()
        passenger_id = self.id_entry.get()
        seat_class = self.seat_class_combobox.get()
        seat_number = self.seat_number_entry.get()
        luggage_weight = self.luggage_weight_entry.get()

        # Validate the input fields
        if len(name) == 0:
            messagebox.showerror("Name Required", "Name field should not be empty.")
            return

        if not passenger_id.isdigit() or len(passenger_id) != 7:
            messagebox.showerror("Invalid ID", "ID should be a 7-digit integer.")
            return

        if len(seat_number) == 0:
            messagebox.showerror("Seat Number Required", "Seat Number field should not be empty.")
            return

        if len(luggage_weight) == 0:
            messagebox.showerror("Luggage Weight Required", "Luggage Weight field should not be empty.")
            return

        if not seat_number.isdigit():
            messagebox.showerror("Invalid Seat Number", "Seat Number should be a positive integer.")
            return

        seat_number = int(seat_number)
        if seat_number < 1 or seat_number > self.main_window.current_plane.seating_classes[seat_class].num_seats:
            messagebox.showerror("Invalid Seat Number", f"Seat Number should be between 1 and {self.main_window.current_plane.seating_classes[seat_class].num_seats} for {seat_class} class.")
            return

        try:
            luggage_weight = float(luggage_weight)
        except ValueError:
            messagebox.showerror("Invalid Luggage Weight", "Luggage Weight should be a number.")
            return

        if luggage_weight > 100:
            messagebox.showerror("Invalid Luggage Weight", "Luggage Weight should not exceed 100 kg.")
            return

        # Create a passenger object
        passenger = Passenger(name, passenger_id, seat_class, seat_number, luggage_weight)
        
        # Add the passenger to the plane
        if self.main_window.current_plane.add_passenger(passenger):
            self.main_window.update_all_guis()
            messagebox.showinfo("Reservation Confirmed", "Seat reserved successfully!")
            self.destroy()
        else:
            messagebox.showerror("Seat Already Reserved", "This seat is already reserved in this class.")

# Create a window for canceling a seat
class CancelSeatWindow(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.title("Cancel a Seat")
        self.geometry("290x90+500+350")

        self.label_font = Font(family="Helvetica", size=10)

        # Create a frame to hold the input field
        self.info_frame = tk.Frame(self)
        self.info_frame.pack(pady=10)

        # Create a validation function for the ID entry field
        def validate_id(input_text):
            return len(input_text) <= 7

        validate_cmd = self.register(validate_id)

        self.id_label = tk.Label(self.info_frame, text="ID:", font=self.label_font)
        self.id_entry = tk.Entry(self.info_frame, font=self.label_font, bg="white", width=30, validate="key", validatecommand=(validate_cmd, '%P'))
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a button to cancel the seat
        self.cancel_button = tk.Button(self.info_frame, text="Cancel", font=self.label_font, command=self.cancel_seat)
        self.cancel_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Function to cancel a seat
    def cancel_seat(self):
        # Get the value from the input field
        passenger_id = self.id_entry.get()

        # Validate the input field
        if not passenger_id.isdigit() or len(passenger_id) != 7:
            messagebox.showerror("Invalid ID", "ID should be a 7-digit integer.")
            return

        # Remove the passenger from the plane
        passenger = self.main_window.current_plane.remove_passenger(passenger_id)
        if passenger:
            self.main_window.update_all_guis()
            self.main_window.seat_gui.clear_seat_color(passenger)
            messagebox.showinfo("Cancellation Confirmed", "Seat cancellation successful!")
            self.destroy()
        else:
            messagebox.showerror("ID Not Found", "The provided ID is not registered.")

# Create a window for the seating plan
class SeatGUI(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.title("Seating Plan")
        self.geometry("295x550+750+50")

        self.button_font = Font(family="Helvetica", size=10)

        # Create a label for the plane number
        self.plane_label = tk.Label(self, text=f"Plane #{self.main_window.current_plane.plane_number}", font=("Helvetica", 12, "bold"))
        self.plane_label.pack(pady=10)

        # Create a frame to hold the seating plan
        self.seat_plan_frame = tk.Frame(self)
        self.seat_plan_frame.pack(padx=20, pady=0)

        # Create the seating plan
        self.create_seat_plan()

        # Create a frame to display information about seats occupied, cargo filled, and revenue
        self.info_frame = tk.Frame(self)
        self.info_frame.pack(pady=10)

        # Create labels to display the number of seats occupied
        self.seats_occupied_label = tk.Label(self.info_frame, text="Seats Occupied:", font=("Helvetica", 10))
        self.seats_occupied_value = tk.Label(self.info_frame, text="0", font=("Helvetica", 10), bg="white", width=10)
        self.seats_occupied_label.grid(row=0, column=0, padx=5, pady=2)
        self.seats_occupied_value.grid(row=0, column=1, padx=5, pady=2)

        # Create labels to display the amount of cargo filled
        self.cargo_filled_label = tk.Label(self.info_frame, text="Cargo Filled:", font=("Helvetica", 10))
        self.cargo_filled_value = tk.Label(self.info_frame, text="0", font=("Helvetica", 10), bg="white", width=10)
        self.cargo_filled_percentage = tk.Label(self.info_frame, text="%", font=("Helvetica", 10))
        self.cargo_filled_label.grid(row=1, column=0, padx=5, pady=2)
        self.cargo_filled_value.grid(row=1, column=1, padx=5, pady=2)
        self.cargo_filled_percentage.grid(row=1, column=2, padx=5, pady=2)

        # Create labels to display the revenue
        self.revenue_label = tk.Label(self.info_frame, text="Revenue:", font=("Helvetica", 10))
        self.revenue_rs_label = tk.Label(self.info_frame, text="pkr", font=("Helvetica", 10))
        self.revenue_value = tk.Label(self.info_frame, text="0", font=("Helvetica", 10), bg="white", width=10)
        self.revenue_label.grid(row=2, column=0, padx=1, pady=1)
        self.revenue_rs_label.grid(row=2, column=2, padx=1, pady=1)
        self.revenue_value.grid(row=2, column=1, padx=1, pady=1)

        # Update all the information
        self.update_all_info()

    # Function to create the seating plan
    def create_seat_plan(self):
        seat_classes = ['Business', 'Economy', 'Student']
        max_seats = [12, 24, 8]

        # Iterate over each seat class
        for class_index, class_name in enumerate(seat_classes):
            # Create a frame for the seat class
            class_frame = tk.LabelFrame(self.seat_plan_frame, text=class_name + " Class")
            class_frame.grid(row=class_index, column=0, padx=40, pady=1)

            # Iterate over each seat in the seat class
            for seat_num in range(1, max_seats[class_index] + 1):
                # Generate a seat ID based on the class name and seat number
                seat_id = self.generate_seat_id(class_name, seat_num)
                # Read the status data for the seat
                seat_status = self.read_status_data(seat_id)
                # Get the color for the seat based on its status
                seat_color = self.get_seat_color(seat_status)
                # Create a button for the seat
                seat_button = tk.Button(class_frame, text=str(seat_num), width=4, height=1, font=self.button_font, bg=seat_color)
                seat_button.grid(row=(seat_num - 1) // 4, column=(seat_num - 1) % 4, padx=1, pady=1)

    # Function to read the status data for a seat
    def read_status_data(self, seat_id):
        status_data = {}
        with open("isidata.txt", "r") as file:
            for line in file:
                parts = line.strip().split("\t\t")
                if len(parts) == 2:
                    status_data[parts[0]] = parts[1]
        return status_data.get(seat_id, "")

    # Function to generate a seat ID
    def generate_seat_id(self, class_name, seat_num):
        class_initial = class_name[0].upper()
        return f"{class_initial}{seat_num:02d}"

    # Function to get the color for a seat based on its status
    def get_seat_color(self, seat_status):
        if seat_status == "CLEAN":
            return "green"
        elif seat_status == "TERRORIST":
            return "red"
        elif seat_status == "":
            return "grey"
        else:
            return "orange"

    # Function to update the color of a seat
    def update_seat_color(self, passenger):
        seat_class = self.main_window.current_plane.seating_classes[passenger.seat_class]
        seat_num = passenger.seat_number
        seat_status = passenger.status
        seat_color = self.get_seat_color(seat_status)
        for class_frame in self.seat_plan_frame.winfo_children():
            if class_frame.cget("text") == passenger.seat_class + " Class":
                for seat_button in class_frame.winfo_children():
                    if seat_button.cget("text") == str(seat_num):
                        seat_button.config(bg=seat_color)
                        break

    # Function to highlight a seat
    def highlight_seat(self, passenger):
        for class_frame in self.seat_plan_frame.winfo_children():
            if class_frame.cget("text") == passenger.seat_class + " Class":
                for seat_button in class_frame.winfo_children():
                    if seat_button.cget("text") == str(passenger.seat_number):
                        seat_button.config(bg="yellow")
                        break

    # Function to clear the color of a seat
    def clear_seat_color(self, passenger):
        for class_frame in self.seat_plan_frame.winfo_children():
            if class_frame.cget("text") == passenger.seat_class + " Class":
                for seat_button in class_frame.winfo_children():
                    if seat_button.cget("text") == str(passenger.seat_number):
                        seat_button.config(bg="grey")
                        break

    # Function to update the color of all seats
    def update_all_seats(self):
        for passenger in self.main_window.current_plane.passengers:
            self.update_seat_color(passenger)

    # Function to update all the information
    def update_all_info(self):
        self.update_seats_occupied()
        self.update_cargo_filled()
        self.update_revenue()

    # Function to update the number of seats occupied
    def update_seats_occupied(self):
        count = len(self.main_window.current_plane.passengers)
        self.seats_occupied_value.config(text=str(count))

    # Function to update the amount of cargo filled
    def update_cargo_filled(self):
        cargo_weight = self.main_window.current_plane.total_cargo_weight
        max_cargo_limit = self.main_window.current_plane.max_cargo_limit
        percentage = (cargo_weight / max_cargo_limit) * 100 if max_cargo_limit else 0
        self.cargo_filled_value.config(text=f"{cargo_weight}")

    # Function to update the revenue
    def update_revenue(self):
        revenue = self.main_window.current_plane.get_total_revenue()
        self.revenue_value.config(text=f"{revenue}")
