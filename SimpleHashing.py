# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 15:02:34 2022

@author: shaurya
"""
import numpy as np

Dict ={}
Dict['a'] =1
Dict['b'] =2
Dict['c'] =3
Dict['d'] =4

print(Dict)
for i in Dict.keys() :
    print(i)

for i in Dict.keys() :
    print(Dict[i])
    
values = [Dict[i] for i in Dict.keys()]
print(values) 
    
values = [i for i in Dict.keys()]
print(values)

values = [str(i) +':'+ str(Dict[i]) for i in Dict.keys()]
print(values)

keys = [i for i in Dict.keys()]
values = [Dict[i] for i in Dict.keys()]
di = {k:v for k,v in zip(keys,values)}
"""
['a:1', 'b:2', 'c:3', 'd:4']
"""

k=map(hash ,values)
"""
hash(1)
Out[28]: 1
"""

l=map(hash ,keys)
"""
hash('s')
Out[31]: 3597389277156182343
"""