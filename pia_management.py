from plane import Plane

# Define a class called PIAManagement
class PIAManagement:
    # Initialize the class
    def __init__(self):
        # Create a list to store planes, and add a plane with number 1 to the list
        self.planes = [Plane(1)]

    # Define a method to add a new plane to the list
    def add_plane(self):
        # Calculate the number for the new plane by adding 1 to the length of the planes list
        new_plane_number = len(self.planes) + 1
        # Create a new plane with the new plane number and add it to the planes list
        self.planes.append(Plane(new_plane_number))

    # Define a method to get a plane by its plane number
    def get_plane(self, plane_number):
        # Iterate through each plane in the planes list
        for plane in self.planes:
            # Check if the plane number matches the given plane number
            if plane.plane_number == plane_number:
                # If a match is found, return the plane
                return plane
        # If no match is found, return None
        return None
