#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'The movie is about to begin, we recommend '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your score?"))

# if between 90-100
if score >=90:
    message = ' you got an A, way to go! '

# if between 80-89
elif score >=80 and score <90:
    message = ' you got a B, nice going! '

# if between 70-79
elif score >=70 and score <79:
    message = 'you got a C, keep it up '

# if between 60-69
elif score >=60 and score <69:
    message = 'you got a B, a bit more time studing '

else:
    message = ' less time slacking around and more studing '

print(message)
