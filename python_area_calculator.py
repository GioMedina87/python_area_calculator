# ------------------------------------------------------------------------------
# Eduardo G. Medina
# Project 5 - Area Calculator
# Language: Python
# Filename: python_area_calculator.py
# ------------------------------------------------------------------------------


class Rectangle:
    def __init__(self, width, height):
        # Constructor to initialize width and height
        self.width = width
        self.height = height

    def get_perimeter(self):
        # Method to calculate and return the perimeter of the rectangle
        return 2 * (self.width + self.height)

    def get_area(self):
        # Method to calculate and return the area of the rectangle
        return self.width * self.height

    def print_perimeter(self):
        # Method to print the perimeter of the rectangle
        print(f"Rectangle perimeter: {self.get_perimeter()}")

    def print_area(self):
        # Method to print the area of the rectangle
        print(f"Rectangle area: {self.get_area()}")


class Square(Rectangle):
    def __init__(self, length):
        # Constructor for the Square class, using the length for both width and height
        super().__init__(length, length)

    def print_perimeter(self):
        # Method to print the perimeter of the square
        print(f"Square perimeter: {self.get_perimeter()}")

    def print_area(self):
        # Method to print the area of the square
        print(f"Square area: {self.get_area()}")


def main():
    shapes = []  # List to store instances of rectangles and squares

    while True:
        shape_type = input("Rectangle or Square (r/s): ").lower()

        if shape_type == 'r':
            # For rectangle, get width and height from the user
            width = float(input("Width: "))
            height = float(input("Height: "))
            shape = Rectangle(width, height)
        elif shape_type == 's':
            # For square, get length from the user
            length = float(input("Length: "))
            shape = Square(length)
        else:
            print("Invalid shape")
            # Add the "Continue? y/n:" prompt for invalid input
            continue_input = input("Continue? y/n: ").lower()
            if continue_input != 'y':
                break
            else:
                continue
          
        shapes.append(shape)  # Add the created shape to the list

        continue_input = input("Continue? y/n: ").lower()
        if continue_input != 'y':
            print("\nResults\n")
            for shape in shapes:
        # Print the perimeter and area for each shape in the list
                shape.print_perimeter()
                shape.print_area()
            break
        
    print("\nThank you for using my app!")
    

if __name__ == "__main__":
    main()

