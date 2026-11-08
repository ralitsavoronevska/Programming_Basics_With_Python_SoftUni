# https://alpha.judge.softuni.org/contests/04-easter-eggs-battle/1637/practice#7

count_eggs_player_one = int(input())
count_eggs_player_two = int(input())

while True:
    command = input()

    if command == 'End':
        print(f"Player one has {count_eggs_player_one} eggs left.")
        print(f"Player two has {count_eggs_player_two} eggs left.")
        break

    if command == 'one':
        count_eggs_player_two -= 1
    elif command == 'two':
        count_eggs_player_one -= 1

    if count_eggs_player_one == 0:
        print(f"Player one is out of eggs. Player two has {count_eggs_player_two} eggs left.")
        break
    elif count_eggs_player_two == 0:
        print(f"Player two is out of eggs. Player one has {count_eggs_player_one} eggs left.")
        break