from seat import Seat

class SeatingClass:
    def __init__(self, class_type, num_seats, price_per_seat):
        # Initialize the SeatingClass object with the provided parameters.
        self.class_type = class_type
        self.num_seats = num_seats
        self.price_per_seat = price_per_seat
        self.seats = [Seat(i + 1) for i in range(num_seats)]

    def is_seat_available(self, seat_number):
        # Check if the seat number is within the valid range and if the seat is available.
        return 1 <= seat_number <= self.num_seats and self.seats[seat_number - 1].passenger is None

    def reserve_seat(self, seat_number, passenger):
        # Reserve a seat for the given passenger if it is available.
        if self.is_seat_available(seat_number):
            self.seats[seat_number - 1].passenger = passenger
            return True
        return False

    def cancel_seat(self, seat_number):
        # Cancel the reservation for the given seat number if it is valid.
        if 1 <= seat_number <= self.num_seats:
            self.seats[seat_number - 1].passenger = None
            return True
        return False

    # This method returns a list of reserved seats in the seating class.
    def get_reserved_seats(self):
        # Create an empty list to store the reserved seats.
        reserved_seats = []
        
        # Iterate through each seat in the seating class.
        for seat in self.seats:
            # Check if the seat has a passenger assigned to it.
            if seat.passenger:
                # If the seat has a passenger, add it to the reserved seats list.
                reserved_seats.append(seat)
        
        # Return the list of reserved seats.
        return reserved_seats
