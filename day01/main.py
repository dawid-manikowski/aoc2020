#!/usr/bin/env python3
expenses = open("1-input.txt").readlines()
expenses = [i.strip() for i in expenses]
expenses = [int(i) for i in expenses]

for a in expenses: 
    for b in expenses: 
        if a + b == 2020: 
            print(a, b, 2020, a*b) 
            
for a in expenses: 
    for b in expenses: 
        for c in expenses: 
            if a + b + c == 2020: 
                print(a, b, c, 2020, a*b*c)
