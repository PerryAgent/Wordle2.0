import json
from logging import exception
import random
from colorama import Fore, Style


data  = json.load(open("Oxford-Dictionary-Json/dicts.json"))
words = []

for word in data:
    if len(word['word'])>= 3 and len(word['word'])<=6 :
        words.append(word['word'].upper())

number = len(words)


class Game:
    n = 0
    w = ""

    def __init__(self):
        print("       ",end="")
        print ("WELCOME TO WORDLE!\n")
        self.n = random.randint(0,number)
        self.w = words[self.n]

    def start(self):
        l = len(self.w)
        tries = 7
        
        print("         ",end="")
        for i in range(l):
            print(Fore.BLACK +"_",end=" ")
        
        print("\n")

        print(Style.RESET_ALL)
        while(tries):
            tries -= 1
            print("Next Guess?\n")

            g = input()
            if len(g)!=l:
                raise exception("Invalid Input!")

            g = g.upper()

            g_copy = g

            print("         ",end="")
            count = l
            for i in range(l):
                if g[i] in self.w:

                    if g[i] == self.w[i]:
                        print(Fore.GREEN +g[i],end=" ")
                        count -= 1
                    else:
                        print(Fore.LIGHTYELLOW_EX +g[i],end=" ")
                else:
                    print(Fore.BLACK +g[i],end=" ")

            print("\n         ",end="")
            for i in range(l):
                print(Fore.BLACK +"_",end=" ")
            print(Style.RESET_ALL)


            g = g_copy
            print("\n")
            if count == 0:
                print("And you get 'Ghanta' for winning!!")
                return
        
        print("\n         ",end="")
        for i in self.w:
            print(Fore.RED +i,end=" ")

        print(Style.RESET_ALL)
        print("Loser!!!")

n = Game()
n.start()
