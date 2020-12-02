#!/usr/bin/env python3

import re

pat = re.compile(r"(\d+)-(\d+)\s(\w)")

passwords = open("2-input.txt").readlines()
passwords = [{"policy": a.split(":")[0], "pass":  a.split(":")[1].strip()} for a in passwords]

count = 0 
 
for a in passwords: 
    match = pat.match(a['policy']) 
    e, b, c = match.groups() 
    if int(e) <= a['pass'].count(c) <= int(b): 
        count += 1 
        print("YES!", a)
print(count)
        

count = 0 
 
for a in passwords: 
    match = pat.match(a['policy']) 
    e, b, c = match.groups() 
    if a['pass'][int(e)-1] == c and a['pass'][int(b)-1] != c: 
        count += 1 
        print("YES!", a) 
    elif a['pass'][int(e)-1] != c and a['pass'][int(b)-1] == c: 
        count += 1 
        print("YES!", a)
print(count)
