# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:31:36 2021

@author: ben
"""

def substring(string,first,end):
    count = 0
    for i in range(0,len(string)):
        if string[i] == first:
            for j in range(i+1,len(string)):
                if string[j] == end:
                    count = count +1 
    return count

print(substring("TXZXXJZWX","X","Z"))