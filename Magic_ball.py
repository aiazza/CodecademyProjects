
# We’ll be using the following 9 possible answers for our Magic 8-Ball:
# 
# Yes - definitely.
# It is decidedly so.
# Without a doubt.
# Reply hazy, try again.
# Ask again later.
# Better not tell you now.
# My sources say no.
# Outlook not so good.
# Very doubtful.
# The output of the program will have the following format:
# 
# [Name] asks: [Question]
# Magic 8-Ball’s answer: [Answer]
# For example:
# 
# Joe asks: Is this real life?
# Magic 8-Ball's answer: Better not tell you now

# https://www.codecademy.com/courses/learn-python-3/projects/python-magic-8-ball

import random

name = input("What is your name ?\n")
Question = input("What would you like to know ? \nAsk me a Yes or No Question.\n")
Answer = ""
random_number = random.randint(1, 9)



if random_number == 1:
    answer = "Magic 8-Ball's answer: Yes - definitely."
elif random_number == 2:
    answer = "Magic 8-Ball's answer: It is decidedly so."
elif random_number == 3:
    answer = "Magic 8-Ball's answer: Without a doubt."
elif random_number == 4:
    answer = "Magic 8-Ball's answer: Reply hazy, try again.."
elif random_number == 5:
    answer = "Magic 8-Ball's answer: Ask again later."
elif random_number == 6:
    answer = "Magic 8-Ball's answer: Better not tell you now."
elif random_number == 7:
    answer = "Magic 8-Ball's answer: My sources say no.."
elif random_number == 8:
    answer = "Magic 8-Ball's answer: Outlook not so good.."
elif random_number == 9:
    answer = "Magic 8-Ball's answer: Very doubtful."
else:
    answer = "Magic 8-Ball's answer: Error man, dont try to mess up the system"


if name == "":
    print("Question :", Question)
else:
    print(name, "asks : ", Question)
if Question =="":
    print("You have to provide a")
print(answer)


test change 