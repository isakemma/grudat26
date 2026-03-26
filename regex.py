# coding: utf-8

# De här funktionerna ska returnera reguljära uttryck som löser uppgifterna på övningen.

def oktal():          # uppgift 1
    return ""

def ISIN():       # uppgift 2
    return ""

def MACaddress():     # uppgift 3
    return ""

def complex():     # uppgift 4
    return ""

def sorted():     # uppgift 5
    return ""

def sjorovare():
    return ""     #uppgift 6

# Här är lite kod som du kan använda för att provköra dina
# reguljära uttryck. Koden definierar en main-metod som läser
# rader från standard input och kollar vilka reguljära uttryck
# som matchar indata-raden. 
#
# För att provköra från terminalen, skriv:
# > python regex.py
# Skriv in teststrängar:
# [skriv här]
# ...

from sys import stdin
import re

def main():
    tasks = [oktal, isin, MACaddress, complex, sorted, sjorovare]
    print('Skriv in teststrängar:')
    while True:
        line = stdin.readline().rstrip('\r\n')
        if line == '': break
        for task in tasks:
            result = '' if re.search(task(), line) else 'INTE ' 
            print('%s(): "%s" matchar %suttrycket "%s"' % (task.__name__, line, result, task()))
    
if __name__ == '__main__': main()
