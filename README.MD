# Rectangle-Class-Implementation

This repository contains the implementation of a `Rectangle` class in Python, demonstrating basic Object-Oriented Programming (OOP) principles. The class includes attributes for length, width, and color, along with methods to describe the rectangle, calculate its area and perimeter, and change its color.

## Features

- **Attributes**: length, width, color
- **Constructor**: initializes all attributes
- **Methods**:
  - `describe()`: returns a description of the rectangle
  - `area()`: calculates and returns the area of the rectangle
  - `perimeter()`: calculates and returns the perimeter of the rectangle
  - `change_color(new_color)`: changes the color of the rectangle

## Usage

Here is an example of how to use the `Rectangle` class:

```python
class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def describe(self):
        return f'The rectangle has a length of {self.length}, width of {self.width}, and is {self.color}.'

    def area(self):
        return f'The area of the rectangle is: {self.length * self.width}'

    def perimeter(self):
        return f'The perimeter of the rectangle is: {2 * (self.length + self.width)}'

    def change_color(self, new_color):
        self.color = new_color
        print(f'The color has been changed to {new_color}.')

# Example usage
rect1 = Rectangle(5, 4, 'white')
print(rect1.describe())
print(rect1.area())
print(rect1.perimeter())
rect1.change_color('purple')
print(rect1.describe())

rect2 = Rectangle(10, 5, 'green')
print(rect2.describe())
print(rect2.area())
print(rect2.perimeter())
rect2.change_color('blue')
print(rect2.describe())
