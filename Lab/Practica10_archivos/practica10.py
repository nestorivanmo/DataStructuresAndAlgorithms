# -*- coding: utf-8 -*-
import locale
import pickle
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patheffects as path_effects

PATH = 'dataset.xml'
KEYS = ['user', 'email', 'password']
contador1 = 0
contador2 = 0

def getElements(bSequence, eSequence, offSet):
    listToUse = []
    try:
        file = open(PATH, "r", encoding='utf-8')
        for line in file:
            beginning = line.find(bSequence)
            end = line.find(eSequence)
            if beginning >= 0:
                listToUse.append(line[beginning+offSet:end])
    except:
        print('No fue posible abrir el archivo -> ' + str(PATH))
    finally:
        if file:
            file.close()
    return(listToUse)

def getListOfDictionaries(users,passwords,emails,keys):
    listOfDictionaries = []
    for i in range(len(users)):
        user = []
        user.append(users[i])
        user.append(passwords[i])
        user.append(emails[i])
        listOfDictionaries.append(dict(zip(keys, user)))
    return listOfDictionaries

def getDicOfEquals(element,ld):
    global contador1
    listOfElements = {}
    for u in ld:
        contador1 += 1
        obj = u[element]
        if listOfElements == {}:
            listOfElements.update({obj:1})
        else:
            if obj in listOfElements:
                current = listOfElements[obj]
                current += 1
                listOfElements.update({obj:current})
            else:
                listOfElements.update({obj:1})
    return listOfElements

def getMostRepeatedItem(listOfElements):
    global contador1
    repeatedElements = {}
    for e in listOfElements.keys():
        contador1 += 1
        if listOfElements[e] > 1:
            repeatedElements.update({e:listOfElements[e]})

    mostRepeatedKey = None
    numberOfItems = 0
    for r in repeatedElements.keys():
        contador1 += 1
        if repeatedElements[r] > numberOfItems:
            numberOfItems = repeatedElements[r]
            mostRepeatedKey = r
    return repeatedElements, mostRepeatedKey, numberOfItems

def printNicely(dictionary, title, repeatedElements, mrK, nI):
    print("\n" + str(title + 's'))
    print("Most repeated password: " + str(mrK) + "\nTimes: " + str(nI) + "\n")
    sortedDictionary = sorted((value, key) for (key,value) in repeatedElements.items())
    for x in sortedDictionary:
        print(" " + str(x))
    with open(title+".txt", "w") as file:
        file.write("Most repeated "+title+": " + str(mrK) + "\nTimes: " + str(nI) + "\n")
        file.write(str(sortedDictionary))
    print()


def getNumberCompanies():
    global contador2
    companies = []
    try:
        file = open(PATH, "r", encoding='utf-8')
        for line in file:
            contador2 += 1
            beginning = line.find('@')
            end = line.find('.')
            if beginning >= 0:
                company = line[beginning+1:end]
                if len(companies) == 0:
                    companies.append(company)
                if company not in companies:
                    companies.append(company)
    except:
        print('No fue posible abrir el archivo -> ' + str(path))
    finally:
        if file:
            file.close()
    repeatedCompanies = []
    with open("Compañías.txt", "w") as file:
        file.write(str(companies))
    return len(companies), companies

def printCompanies(companies):
    for c in companies:
        print(c)

def generatePieChart(listOfElements, title, element):
    impr = []
    vol = []
    for el in listOfElements.keys():
        impr.append(el)
        vol.append(listOfElements[el])
    fig1, ax1 = plt.subplots()
    ax1.pie(vol, labels=impr, autopct='%1.1f%%', shadow=True,startangle=90)
    plt.show()
    fig1.savefig(title + ".png")

def generateGraph(finalList):
    global contador1
    n = len(finalList)
    x = []
    yPassword = []
    yEmail = []
    for i in range(n):
        x.append(i)
        contador1 = 0
        for j in range(i):
            equalP= getDicOfEquals('password',finalList)
            repeatedElements,mostRepeatedKey,numberOfItems = getMostRepeatedItem(equalP)
        yPassword.append(contador1)
        contador1 = 0
        for j in range(i):
            equalP= getDicOfEquals('email',finalList)
            repeatedElements,mostRepeatedKey,numberOfItems = getMostRepeatedItem(equalP)
        yEmail.append(contador1)
    print(x)
    print(yPassword)
    print(yEmail)
    linearGraph('Passwords', x, yPassword)
    linearGraph('Emails', x, yEmail)

def linearGraph(title, x,y):
    fig,ax = plt.subplots()
    ax.plot(x,y)
    ax.set(xlabel="elementos", yLabel= "iteraciones", title= title)
    ax.grid()
    plt.show()


def generateGraphMail(finalList):
    global contador2
    n = len(finalList)
    x = []
    y = []
    for i in range(n):
        x.append(i)
        contador2 = 0
        for j in range(i):
            numberOfCompanies,companies = getNumberCompanies()
        y.append(contador2)
    print(x)
    print(y)

def companiesPieChart(companies, title):
    impr = []
    vol = []
    for el in companies:
        impr.append(el)
        vol.append(1)
    fig1, ax1 = plt.subplots()
    ax1.pie(vol, labels=impr, autopct='%1.1f%%', shadow=True,startangle=90)
    plt.show()
    fig1.savefig(title + ".png")


def generateStatistics(ld):
    print("\n---STATISTICS---\n")

    equalP= getDicOfEquals('password',ld)
    repeatedElements,mostRepeatedKey,numberOfItems = getMostRepeatedItem(equalP)
    generatePieChart(equalP, 'password', mostRepeatedKey)
    printNicely(equalP, 'Password', repeatedElements, mostRepeatedKey, numberOfItems)

    equalM = getDicOfEquals('email',ld)
    repeatedElements,mostRepeatedKey,numberOfItems = getMostRepeatedItem(equalM)
    generatePieChart(equalM, 'email', mostRepeatedKey)
    printNicely(equalM, 'Email', repeatedElements, mostRepeatedKey, numberOfItems)

    numberOfCompanies,companies = getNumberCompanies()
    print("Number of companies: \n" + str(numberOfCompanies) + "\n")
    companiesPieChart(companies, 'Companías')
    printCompanies(companies)


def main():
    users = getElements('<user>','</user>', 6)
    passwords = getElements('<password>','</password>', 10)
    emails = getElements('<email>','</email>', 7)

    finalList = getListOfDictionaries(users,emails,passwords, KEYS)

    print("\nList of dictionaries\n"+str(finalList))
    print("\nNumber of users\n" + str(len(finalList)))

    generateStatistics(finalList)
    generateGraph(finalList)
    generateGraphMail(finalList)

main()
