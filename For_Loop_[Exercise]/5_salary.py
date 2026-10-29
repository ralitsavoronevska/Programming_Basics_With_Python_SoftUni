number_open_tabs = int(input())
salary = int(input())

FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

for _ in range(number_open_tabs):
    tab_name = str(input())

    if tab_name == "Facebook":
        salary -= FACEBOOK_FINE
    elif tab_name == "Instagram":
        salary -= INSTAGRAM_FINE
    elif tab_name == "Reddit":
        salary -= REDDIT_FINE

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)