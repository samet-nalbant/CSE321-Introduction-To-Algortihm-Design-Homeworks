# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def algorithm(P,n):
    result = 0
    for i in range(len(P)-1,0,-1):
        mult = 1
        for j in range(1,i):
            mult = mult*n
        result = result + P[i]*mult

    return result

print(algorithm([4,3,2,1,0],1))