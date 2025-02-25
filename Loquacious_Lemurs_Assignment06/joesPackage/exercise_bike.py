# File Name : exercise_bike.py
# Group name : Loquacious Lemurs
# Student Name: Joseph Adcock
# email: adcockjb@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 02/25/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment models 2 different pieces of gym equipment using classes through a single use.

# Brief Description of what this module does: This module defines a class modeling an excercise bike.
# Citations: ChatGPT
 
# Define the exception classes:
class InvalidResistanceError(Exception):
    """
    Appears when the user inputs an incorrect resistance level
    @param: N/A
    @return: N/A
    """
    def __init__(self, message="Level must be a positive integer"):
        """
        Tells the bike to stop
        @param: None
        @return: None
        """
        self.message = message
        super().__init__(self.message)

class InvalidTimeError(Exception):
    """
    Appears when the user inputs an incorrect resistance level
    @param: N/A
    @return: N/A
    """
    def __init__(self, message="Time must be a positive number"):
        """
        Tells the bike to stop
        @param: None
        @return: None
        """
        self.message = message
        super().__init__(self.message)

class BikeNotActiveError(Exception):
    """
    Appears when the bike is stopped without starting
    @param: N/A
    @return: N/A
    """
    def __init__(self, message="Bike must be active to stop"):
        """
        Tells the bike to stop
        @param: None
        @return: None
        """
        self.message = message
        super().__init__(self.message)


class ExerciseBike():
    """
    Model an excercise bike in a gym
    @param: N/A
    @return: N/A
    """
    # The constructor should accept two parameters: model and brand.
    def __init__(self, model, brand):
        """
        Constructor
        @param Model: The model of the bike
        @param Brand: The brand of the bike
        """
        self.model = model
        self.brand = brand
        self.is_on = False

    # Implement the functions - start(): | stop(): | adjust_resistance(level):
    def start(self):
        """
        Tells the bike to start
        @param: None
        @return: None
        """
        self.is_on = True
        print("The " + self.model + " starts...")

    def stop(self):
        """
        Tells the bike to stop
        @param: None
        @return: None
        """
        if self.is_on == False:
            raise BikeNotActiveError("Bike must be started to stop.")

        print("The " + self.model + " stops...")
        is_bike_on = False

    def adjust_resistance(self, level):
        """
        Defines the resistance level of the bike
        @param level: An integer determining the resistance level
        @return: None
        """
        if not isinstance(level, int) or level < 0:
            raise InvalidResistanceError(f"Invalid input: '{level}'. Resistance level must be a positive integer.")

        print("The " + self.model + "'s resistance level is set to " + str(level) + ".")
    
    # Define functions for string representation
    def __str__(self):
        """
        A string representation of the object
        @param: None
        @return String: A string of the object
        """
        return f"The bike is a {self.brand} {self.model}."

    def __repr__(self):
        """
        A representation of the object for debugging
        @param: None
        @return String: A string that can be used to represent the object
        """
        return f"ExerciseBike(Model='{self.model}', Brand={self.brand})"