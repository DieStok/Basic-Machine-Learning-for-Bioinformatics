# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:30:15 2021

@author: dieter
"""

{
    "tags": [
        "remove-input",
    ]
}

answ5 = widgets.Checkbox(
    value=False,
    description='On the right, as on the left, gradient descent will converge on a very good fit. It just takes more iterations.',
    disabled=False,
    indent=False,
    layout = {'width': "max-content"}
)

answ6 = widgets.Checkbox(
    value=False,
    description='You will need a higher alpha value on the right partial derivative landscape than on the left one, due to local minima on the right.',
    disabled=False,
    indent=False,
    layout = {'width': "max-content"}
)

answ7 = widgets.Checkbox(
    value=False,
    description='Gradient descent cannot find good values for the parameters on the right landscape.',
    disabled=False,
    indent=False,
    layout = {'width': "max-content"}
)

answ8 = widgets.Checkbox(
    value=False,
    description='Gradient descent can find a good set of parameters, but only if you run it multiple times, each with a different random initialisation and compare performance. This is computationally costly.',
    disabled=False,
    indent=False,
    layout = {'width': "max-content"}
)




widgets.Box(
    [
        answ5,
        answ6,
        answ7,
        answ8
    ]
)

def checkCorrect(answOne, answTwo, answThree, answFour):
    sumAnswers = sum([answOne, answTwo, answThree, answFour])
    if sumAnswers >= 2:
        print('You should only select one option!')
    if answFour == True and not sum([answOne, answTwo, answThree]) >= 1:
        print("Correct. Gradient descent is blind to the landscape, and normally we don't even know how the landscape looks (and it is highly multidimensional). However, given multiple random initialisations, gradient descent will find a rather good fit, although we won't know if it is the globally optimal fit.")
    if sumAnswers == 0:
        print("")
    if sumAnswers == 1 and not answFour == True:
        print("Incorrect, think again!")

print("What do you think would happen if you tried gradient descent in the picture on the right above?")
print()
widgets.interact(checkCorrect,
         answOne = answ5, answTwo = answ6, answThree = answ7, answFour = answ8)
print()