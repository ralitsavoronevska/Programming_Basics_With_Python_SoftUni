x = float(input())
y = float(input())
h = float(input())

# Walls
side_wall_area = x * y
window_area = 1.5 * 1.5
total_side_walls_area = 2 * side_wall_area - 2 * window_area
back_wall_area = x * x
entrance_area = 1.2 * 2
total_front_and_back_area = 2 * back_wall_area - entrance_area
total_wall_area = total_side_walls_area + total_front_and_back_area
green_paint = total_wall_area / 3.4
print(f"{green_paint:.2f}")

# Roof
two_roof_rectangles_area = 2 * side_wall_area
two_roof_triangles_area = 2 * (x * h/2)
total_roof_area = two_roof_rectangles_area + two_roof_triangles_area
red_paint = total_roof_area / 4.3
print(f"{red_paint:.2f}")
