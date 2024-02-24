# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:24:03 2024

@author: bluet
"""

import json
def main():
    game = "None"
    keepGoing = True
    while keepGoing:
        choice = getMenuChoice()
        if choice == "0":
            keepGoing = False
        elif choice == "1":
            game = getDefaultGame()
            print("Default game loaded")
        elif choice == "2":
            game = loadGame()
            print("Game loaded")
        elif choice == "3":
            saveGame(game)
            print("Game saved")
        elif choice == "4":
            if game != "None":
                game = editNode()
            else:
                game = getDefaultGame()
                game = editNode(game)
        elif choice == "5":
            playGame(game)
    return game

def getMenuChoice():
    print("""
    0) exit
    1) load default game
    2) load a game file
    3) save the current game
    4) edit or add a node
    5) play the current game
    """)
    choice = input("select an option 0-5: ")
    return choice

def getDefaultGame():
    game = {
    "start": ["this is a default game", "quit", "quit", "try again", "start"]}
    return game

def playGame(game):
    keepGoing = True
    currentNode = "start"
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)
            
def playNode(game, currentNode):
    keepGoing = True
    (desc, menuA, nodeA, menuB, nodeB) = game[currentNode]
    while keepGoing:
        print(desc)
        print(f"1) {menuA}")
        print(f"2) {menuB}\n")
        menuChoice = input("select an option: ")
        if menuChoice == "1":
            currentNode = nodeA
            keepGoing = False
        elif menuChoice == "2":
            currentNode = nodeB
            keepGoing = False
        else:
            print("input should be 1 or 2")
    return currentNode

def saveGame(game):
    gameFile = input("Select the file you want to save to")
    with open(gameFile, "w") as outfile:
        json.dumps(game)
        json.dump(game, outfile)
        
def loadGame():
    gameFile = input("select the file you want to load")
    file = open(gameFile, "r")
    game = json.load(file)
    file.close()
    return game

def editFields(game, nodeToEdit):
    newDesc = input("Enter a description: ")
    newMenuA = input("Input a menu: ")
    newNodeA = input("Select a node this travels to: ")
    newMenuB = input("Create another menu: ")
    newNodeB = input("Select a node this travels to: ")
    nodeToEdit = (newDesc, newMenuA, newNodeA, newMenuB, newNodeB)
    return nodeToEdit

def editNode(game):
    print("Create or edit a node")
    print("Current nodes:\n")
    print("\n".join(game))
    print()
    nodeToEdit = input("Choose a node to create or edit: ")
    if nodeToEdit == ",".join(game):
        print("replacing node")
        game[nodeToEdit] = editFields(game, nodeToEdit)
    elif nodeToEdit != "":
        print("Creating new node")
        game[nodeToEdit] = editFields(game, nodeToEdit)
    return game

main()