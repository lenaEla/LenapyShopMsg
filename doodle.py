import os

initCell1 = "A2"
initCell2 = "C2"

minSherch = 2
maxSherch = 29

cmpt = minSherch
toReturn = "="
ite = 0

while cmpt <= maxSherch:
    toReturn += "SI(ET({0} = 'Poids Platre'!A${2}; {1} = 'Poids Platre'!C${2});'Poids Platre'!D${2}; ".format(initCell1, initCell2, cmpt)
    cmpt += 1
    ite += 1

toReturn += "SI ({0} <> \"\"; \"Not in table\"; \"\")".format(initCell1)+ ")"*ite

file = open("tmpFile.txt", "w")
file.write(toReturn)
file.close()