start_first_pair = int(input())
start_second_pair = int(input())
diff_start_and_end_first_pair = int(input())
diff_start_and_end_second_pair = int(input())

end_first_pair = start_first_pair + diff_start_and_end_first_pair
end_second_pair = start_second_pair + diff_start_and_end_second_pair

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num_1 in range(start_first_pair, end_first_pair + 1):
    for num_2 in range(start_second_pair, end_second_pair + 1):
        if is_prime(num_1) and is_prime(num_2):
            print(f"{num_1}{num_2}")