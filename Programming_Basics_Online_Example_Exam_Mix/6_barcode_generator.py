# https://alpha.judge.softuni.org/contests/06-barcode-generator/2507/practice#6

start = input()
end = input()

s1 = int(start[0])
s2 = int(start[1])
s3 = int(start[2])
s4 = int(start[3])

e1 = int(end[0])
e2 = int(end[1])
e3 = int(end[2])
e4 = int(end[3])

for num1 in range(s1,e1 +1):
    for num2 in range(s2,e2 + 1):
        for num3 in range(s3,e3 + 1):
            for num4 in range(s4,e4 + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f"{num1}{num2}{num3}{num4}", end=' ')