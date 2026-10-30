current_word = ""
result = ""
c = False
o = False
n = False

while True:
    letter = input()
    if letter == "End":
        break

    if not letter.isalpha() or not letter.isascii():
        continue

    if letter == "c" and not c:
        c = True
    elif letter == "o" and not o:
        o = True
    elif letter == "n" and not n:
        n = True
    else:
        current_word += letter

    if c and o and n:
        result += current_word + " "
        current_word = ""

        c = False
        o = False
        n = False

print(result.strip())