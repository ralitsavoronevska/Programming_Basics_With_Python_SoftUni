width = int(input())
length = int(input())

cake_size = width * length
count_pieces = 0

while cake_size > count_pieces:
    pieces = input()

    if pieces == "STOP":
        print(f"{cake_size - count_pieces} pieces are left.")
        break

    count_pieces += int(pieces)
else:
    print(f"No more cake left! You need {count_pieces - cake_size} pieces more.")