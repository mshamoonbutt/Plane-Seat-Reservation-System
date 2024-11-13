from seating_class import SeatingClass

class Plane:
    def __init__(self, plane_number):
        # Initialize the Plane object with a plane number
        self.plane_number = plane_number
        
        # Define the seating classes and their respective attributes
        self.seating_classes = {
            "Business": SeatingClass("Business", 12, 200000),  # Business class with 12 seats and a price of 200000
            "Economy": SeatingClass("Economy", 24, 100000),    # Economy class with 24 seats and a price of 100000
            "Student": SeatingClass("Student", 8, 40000)       # Student class with 8 seats and a price of 40000
        }
        
        # Set the maximum cargo weight limit and initialize the total cargo weight
        self.max_cargo_limit = 2000
        self.total_cargo_weight = 0
        
        # Initialize the list of passengers
        self.passengers = []

    def add_passenger(self, passenger):
        # Get the seating class based on the passenger's seat class
        seat_class = self.seating_classes[passenger.seat_class]
        
        # Try to reserve the seat for the passenger
        if seat_class.reserve_seat(passenger.seat_number, passenger):
            # If the seat is successfully reserved, add the passenger to the list and update the total cargo weight
            self.passengers.append(passenger)
            self.total_cargo_weight += passenger.luggage_weight
            return True
        return False

    def remove_passenger(self, passenger_id):
        # Iterate over the list of passengers
        for passenger in self.passengers:
            # Check if the passenger ID matches the given passenger ID
            if passenger.passenger_id == passenger_id:
                # Get the seating class based on the passenger's seat class
                seat_class = self.seating_classes[passenger.seat_class]
                
                # Cancel the seat reservation for the passenger
                seat_class.cancel_seat(passenger.seat_number)
                
                # Remove the passenger from the list and update the total cargo weight
                self.passengers.remove(passenger)
                self.total_cargo_weight -= passenger.luggage_weight
                return passenger
        return None

    def get_total_revenue(self):
        # Initialize the total revenue variable
        total_revenue = 0
        
        # Iterate over each passenger in the list of passengers
        for passenger in self.passengers:
            # Iterate over each seating class in the seating classes dictionary
            for seat_class in self.seating_classes:
                # Check if the passenger's seat class matches the current seating class
                if passenger.seat_class == seat_class:
                    # Add the price per seat of the seating class to the total revenue
                    total_revenue += self.seating_classes[seat_class].price_per_seat
        
        # Return the total revenue
        return total_revenue
