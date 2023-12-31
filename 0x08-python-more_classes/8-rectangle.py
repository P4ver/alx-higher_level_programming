#!/usr/bin/python3
"""Define class rec."""


class Rectangle:
    """Represent of rec."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rec."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get i_a the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Calc the_area."""
        return self.__height * self.__width

    def perimeter(self):
        """Calc _permtr."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns and display the rec as '#'."""
        val = self.print_symbol

        if self.__height == 0 or self.__width == 0:
            return ""
        elif type(self.print_symbol) is list:
            return '\n'.join(
                [str(val) * self.__width for q in range(self.__height)]
            )
        elif type(self.print_symbol) is int:
            t_str = str(self.print_symbol)
            return '\n'.join(
                t_str * self.__width for q in range(self.__height)
            )
        else:
            return '\n'.join(
                [val * self.__width for q in range(self.__height)]
            )

    def __repr__(self):
        """returns the Rectangle()form."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delet object my_rec and print the flowing msg."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rec."""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        ar_1 = rect_1.__width * rect_1.__height
        ar_2 = rect_2.__width * rect_2.__height
        if ar_1 >= ar_2:
            return rect_1
        else:
            return rect_2
