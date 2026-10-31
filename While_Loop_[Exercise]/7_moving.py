total_space = int(input()) * int(input()) * int(input()) # width * length * height

cubic_meters = 0

while cubic_meters < total_space:
    box = input()

    if box == 'Done':
        print(f"{total_space - cubic_meters} Cubic meters left.")
        break

    cubic_meters += int(box)
else:
    print(f"No more free space! You need {cubic_meters - total_space} Cubic meters more.")