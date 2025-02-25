# File Name : main.py
# Group name : Loquacious Lemurs
# Student Name: Joshua Slocumb
# email:  slocumjt@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   02/20/2025
# Course #/Section:   IS 4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: This assignment models 2 different pieces of gym equipment using classes through a single use


# Brief Description of what this module does: this module imports our treadmill and exercise modules which contain their respective classes, demonstrates
# and demonstrates their functionality along with handling any potential errors within the classes
# Citations: Perplexity AI pro 



from shantelesPackage import treadmill
from joesPackage import exercise_bike


def main():
    # Treadmill functionality Demonstration
    try:
        treadmill_class = getattr(treadmill, 'Treadmill')  # Dynamically get the class
        treadmill_instance = treadmill_class("ProRunner 2000", "LifeFitness")

        print("=== Treadmill Demo ===")
        treadmill_instance.start()
        print(treadmill_instance)
        treadmill_instance.adjust_settings(5.0, 3)
        print(repr(treadmill_instance))
        treadmill_instance.stop()

    # Gives errors back accoring to what within each class is missing
    except AttributeError:
        print("Error: Treadmill class not found in shantelesPackage/treadmill.py.  Please ensure it exists.")
    except treadmill.InvalidSpeedError as e:
        print(f"Treadmill speed error: {e}")
    except treadmill.InvalidInclineError as e:
        print(f"Treadmill incline error: {e}")
    except treadmill.TreadmillNotRunningError as e:
        print(f"Treadmill operation error: {e}")
    except Exception as e:
        print(f"Error during Treadmill operations: {e}")

    # Exercise Bike functionality demonstration
    try:
        exercise_bike_class = getattr(exercise_bike, 'ExerciseBike')  # Dynamically get the class
        exercise_bike_instance = exercise_bike_class("CycleMaster X1", "Peloton")

        print("\n=== Exercise Bike Demo ===")
        exercise_bike_instance.start()
        print(exercise_bike_instance)
        exercise_bike_instance.adjust_resistance(8)
        print(repr(exercise_bike_instance))
        exercise_bike_instance.stop()
    # Gives errors back accoring to what within each class is missing
    except AttributeError:
        print("Error: ExerciseBike class not found in joesPackage/exercise_bike.py. Please ensure it exists.")
    except exercise_bike.InvalidResistanceError as e:
        print(f"Exercise Bike resistance error: {e}")
    except exercise_bike.InvalidTimeError as e:
        print(f"Exercise Bike time error: {e}")
    except exercise_bike.BikeNotActiveError as e:
        print(f"Exercise Bike operation error: {e}")
    except Exception as e:
        print(f"Error during ExerciseBike operations: {e}")


if __name__ == "__main__":
    main()


