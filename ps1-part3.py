
def heart_rate(age, goal):

    max_HR = 220 - age
    print(f"Your maximum heart rate is: {max_HR}")

    if goal == "S":
        print(f"Your target heart rate is between {max_HR * 0.8} and {max_HR}")
    else:
        print(f"Your target heart rate is between {max_HR * 0.6} and {max_HR * 0.8}")

user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")
heart_rate(user_age, user_goal)

