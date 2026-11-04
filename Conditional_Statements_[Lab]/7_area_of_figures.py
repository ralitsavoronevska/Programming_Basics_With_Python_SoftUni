from math import pi

shape = str(input())
shape_area = 0.0

if shape == "square":
    square_side = float(input())
    shape_area = square_side * square_side
elif shape == "rectangle":
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    shape_area = rectangle_side_a * rectangle_side_b
    pass
elif shape == "circle":
    circle_radius = float(input())
    shape_area = pi * circle_radius * circle_radius
    pass
elif shape == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    shape_area = (triangle_side * triangle_height) / 2

print(f"{shape_area:.3f}")