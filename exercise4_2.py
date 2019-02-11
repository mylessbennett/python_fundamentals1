my_age = 23
user_age = int(input("What is your age? "))


if user_age > 100:
    print("I'm not sure I believe you!")
elif user_age >= my_age:
    age_diff = user_age - my_age
    print("You are {} years older than me.".format(age_diff))
else:
    age_diff = my_age - user_age
    print("I am {} years older than you.".format(age_diff))
