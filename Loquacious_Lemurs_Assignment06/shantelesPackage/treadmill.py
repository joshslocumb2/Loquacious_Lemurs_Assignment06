# File Name : treadmill.py
# Group name : Loquacious Lemurs
# Student Name: Shantele King
# email: King4sl@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:  02/20/2025
# Course #/Section:  IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This assignment models 2 different pieces of gym equipment using classes through a single use
# Brief Description of what this module does: This module goes over the attributes of a treadmill and what happened when it is in use.
# Citations: ChatGPT
 


class Treadmill:
    def __init__(self, model, brand, speed=0.0, incline=0):
        self._model = model
        self._brand = brand
        self._speed = speed
        self._incline = incline
        self._is_running = False

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        try:
            if value < 0:
                raise ValueError("Speed cannot be negative")
            self._speed = float(value)
        except ValueError as e:
            print(f"Error setting speed: {e}")

    @property
    def incline(self):
        return self._incline

    @incline.setter
    def incline(self, value):
        try:
            if not 0 <= value <= 15:
                raise ValueError("Incline must be between 0-15")
            self._incline = int(value)
        except ValueError as e:
            print(f"Error setting incline: {e}")

    def start(self):
        self._is_running = True
        print(f"{self._brand} {self._model} started")

    def stop(self):
        self._is_running = False
        print(f"{self._brand} {self._model} stopped")

    def adjust_settings(self, new_speed, new_incline):
        self.speed = new_speed
        self.incline = new_incline
        print(f"Settings adjusted: {self._speed} km/h, {self._incline}% incline")

    def __str__(self):
        return f"{self._brand} {self._model} - Current speed: {self._speed} km/h, Incline: {self._incline}%"

    def __repr__(self):
        return f"Treadmill(model='{self._model}', brand='{self._brand}', speed={self._speed}, incline={self._incline})"