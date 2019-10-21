#!/usr/bin/env python3

def lookAndSay(num):
    """ 
    The function receives a string with digits in it
    then it returns the number of digits and the digit itself
    every time it discovers another digit
    and it is repeated until it reaches the end of the string
    """
    if(num == ""):
        return ""

    parts = []
    marker = 0
    for i in range(0, len(num)):
        if num[marker] != num[i]:
            part = num[marker:i]
            parts.append(str(len(part)))
            parts.append(num[marker])
            marker = i
    parts.append(str(len(num[marker:len(num)])))
    parts.append(str(num[len(num) - 1]))
    return "".join(parts)

def main():
    dummy = "1"
    for i in range(0,  10):
        print(dummy)
        dummy = lookAndSay(dummy)

if __name__ == "__main__":
    main()
