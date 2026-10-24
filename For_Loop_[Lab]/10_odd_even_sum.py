n = int(input())
even_sum = 0
odd_sum = 0

for idx in range(n):
    new_number = int(input())
    if idx % 2 == 0:
        even_sum += new_number
    else:
        odd_sum += new_number

if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    print(f"No")
    print(f"Diff = {abs(odd_sum - even_sum)}")