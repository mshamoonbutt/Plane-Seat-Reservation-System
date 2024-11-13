class Passenger:
    # initialize the passenger object
    def __init__(self, name, passenger_id, seat_class, seat_number, luggage_weight):
        self.name = name  # store the passenger's name
        self.passenger_id = passenger_id  # store the passenger's id
        self.seat_class = seat_class  # store the seat class
        self.seat_number = seat_number  # store the seat number
        self.luggage_weight = luggage_weight  # store the luggage weight
        self.status = self.check_id_status()  # check the status of the id

    # method to check if the passenger is clean or terrorist
    def check_id_status(self):
        with open("isidata.txt", "r") as file:  # open the file
            for line in file:  # go through each line in the file
                parts = line.strip().split("\t\t")  # split the line into parts
                if parts[0] == self.passenger_id:  # if the id matches
                    return parts[1]  # return the status
        return "Not found"  # return not found if no match
