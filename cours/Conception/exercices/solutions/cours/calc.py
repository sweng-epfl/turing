#!/usr/bin/env python3

def getInput():
    text = input("Calcul à faire ? (en notation polonaise inverse; ou 'sortir') ")
    if text == "sortir":
        return None
    return text

def parseInput(text):
    return text.split(" ")

def getInt(part):
    try:
        n = int(part)
        return n
    except ValueError:
        return None


def execute(op, a, b):
    if op == '+':
        return a + b
    if op == '-':
        return b - a
    if op == '*':
        return a * b
    if op == '/':
        return b / a
    return None

def compute(parts):
    lst = []
    for p in parts:
        if p == '':
            continue
        n = getInt(p)
        if n is None:
            n = execute(p, lst.pop(), lst.pop())
        if n is None:
            return None
        lst.append(n)
    if len(lst) == 1:
        return lst.pop()
    return None

def display(result):
    if result is None:
        print("Calcul invalide")
    else:
        print(result)


while True:
  text = getInput()
  if text is None: break
  tokens = parseInput(text)
  result = compute(tokens)
  display(result)
