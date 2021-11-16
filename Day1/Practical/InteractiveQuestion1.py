# -*- coding: utf-8 -*-
"""
Stiekeminleesfile
"""

{
    "tags": [
        "remove-input",
    ]
}

answ1 = widgets.Checkbox(
    value=False,
    description='You want to know whether you can predict blood glucose level from gene expression data, and have samples of gene expression data for patients with different blood glucose levels.',
    disabled=False,
    indent=False,
    layout = {'width': "max-content"}
)

answ2 = widgets.Checkbox(
    value=False,
    description='You\'ve measured the transcriptome of single cells in a certain tissue and want to find out how many different cell types there are.',
    disabled=False,
    indent=False,
    layout = {'width': "max-content"}
)

answ3 = widgets.Checkbox(
    value=False,
    description='You\'ve got data on formation of 3D DNA structures of interacting DNA and the chromatin marks along the DNA and want to predict 3D DNA structure formation.',
    disabled=False,
    indent=False,
    layout = {'width': "max-content"}
)

answ4 = widgets.Checkbox(
    value=False,
    description='You\'ve got labeled data of the number of seals in aerial pictures of sand banks and try to train a convolutional neural network to automatically count the number of seals',
    disabled=False,
    indent=False,
    layout = {'width': "max-content"}
)




widgets.Box(
    [
        answ1,
        answ2,
        answ3,
        answ4
    ]
)

def checkCorrect(answOne, answTwo, answThree, answFour):
    sumAnswers = sum([answOne, answTwo, answThree, answFour])
    if sumAnswers >= 2:
        print('You should only select one option!')
    if answTwo == True and not sum([answOne, answThree, answFour]) >= 1:
        print("Correct. Here you don't know the true cell types and want to cluster in the multidimensional gene expression space on some distance metric!")
    if sum([answOne, answTwo, answThree, answFour]) == 0:
        print("")
    if sumAnswers == 1 and not answTwo == True:
        print("Incorrect, this is a supervised learning approach!")


print("Which of the below best characterises an unsupervised learning problem?")
print()
widgets.interact(checkCorrect,
         answOne = answ1, answTwo = answ2, answThree = answ3, answFour = answ4)
print()