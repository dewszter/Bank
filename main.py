from random import randint
from Classes import Kund, Konto #, Bank
import os


idGen = 0
kunder = []




def Meny():
    print("Vad vill du göra? \n \n")
    print("1. Skapa en ny kund")
    print("2. Skapa ett nytt konto")
    print("3. Ändra saldo på ett konto\n\n")
    val = input("Ditt val: ")
    return val



def KundNy():
    os.system('cls')
    idGen = randint(0,9999)
    namnNy = input("Ange kundens namn: ")
    pNumNy = input("Ange kundens personnummer (ÅÅÅÅMMDDXXXX): ")
    kunder.append(Kund(namnNy, pNumNy, idGen))
    
Meny()   
#if (val == "1"):
KundNy()

    
for i in kunder:
    print(i.namn, i.pNum, "\nkund ID: ", i.idKund)