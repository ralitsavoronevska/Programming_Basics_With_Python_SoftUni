# Input:
# length_cm
# width_cm
# height_cm
# percentage

# Output:
# needed_liters

length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage = float(input())
fish_tank_volume = length_cm * width_cm * height_cm
fish_tank_volume_in_liters = fish_tank_volume / 1000
occupied_space = percentage / 100
needed_liters = fish_tank_volume_in_liters * (1 - occupied_space)

print(needed_liters)