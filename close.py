import pandas as pd
import numpy as np
df = pd.read_csv('weather.csv', sep=",")

df1 = df.drop(['id'], axis=1).to_numpy()

init = []
for i in df1:
    for q in i:
        if (q not in init):
            init.append(q)

from collections import Counter
MinSup = 4


itemC = Counter()
for i in init:
    for d in df1:
        if(i in d):
            itemC[i] += 1    
print('les itemSets sont :')            
for k in itemC:
    print([k],": ",str(itemC[k]))
print()    

items = Counter() 
for i in itemC:
    if(itemC[i] >= MinSup): 
        items[frozenset([i])] += itemC[i]
Items_S = []


def my_function(x):
    var = list(x)
    global Items_S
    FI = None
    for count in range (2,11):
        Bool=True
        N_Items = set()
        temp = list(items)
        if count > 2:
            temp = list(Items_S)
            MyItem = FI
        else:
            MyItem = x
        for j in range(0, len(temp)):
            if temp[j] != MyItem:
                N_Items.add(MyItem.union(temp[j]))
        N_Items = list(N_Items) 

        items_A = Counter()                             
        for i in N_Items:                                 
            items_A[i] = 0                              
            for q in df1:                                
                temp = set(q)                                                                 
                if(i.issubset(temp)):                                      
                    items_A[i]+=1                                         
        #T = list(MyItem)[0]
        for i in items_A: 
            if (items_A[i] >= items[x]) and (i != FI):
                Bool = False
                var = list(i)
                FI = i

        Items_S += items_A
        if Bool:
            return (var)
        

print("les ItemSets fréquants et fermetures sonts : ")
x = 0
Fer = {}
ListF = []

for i in items:
    F_Item = my_function(i)
    if list(i) != F_Item:
        Fer[list(i)[0]] = F_Item
        ListF.append([list(i),F_Item])
    print(str(list(i)) + " - " + str(F_Item) +": "+str(items[i]))
    x += 1
print()    
        
print(Fer) 
print()



Item1 = items
Items_F = items
pos = 1

for count in range (2,1000):
    N_Items = set() # transform un tuple ou une list en un dictionaire
    temp = list(items)
    for i in range(0,len(temp)):
        for j in range(i+1, len(temp)):
            t = temp[i].union(temp[j])
            if(len(t) == count):
                N_Items.add(temp[i].union(temp[j]))
    N_Items = list(N_Items)
    items_A = Counter()   
    for i in N_Items:
        items_A[i] = 0
        for q in df1:
            temp = set(q)
            if(i.issubset(temp)):
                items_A[i]+=1
    #print("les "+str(count)+"-Itemsets:")
    
    #for i in items_A:
        #print(str(list(i))+": "+str(items_A[i]))
    #print()
    items = Counter()
    
    F = Fer.values()
    for i in items_A:
        if((items_A[i] >= MinSup) and (not (list(i) in F))):
            items[i]+=items_A[i]
    print("les "+str(count)+"-Itemsets fréquents et leur Fermetures")
    for i in items:
        F_Item = my_function(i)
        if list(i) != F_Item:
            Fer[str(list(i))] = F_Item 
            ListF.append([list(i),F_Item])
        print(str(list(i)) + " - " + str(F_Item) +": "+str(items[i]))
    print()  
    if(len(items) == 0):
        break
    Items_F = items
    pos = count
    
Item1 += Items_F    
print("Result: ")
print("Les items listes fréquents sont:")
for i in Items_F:
    print(str(list(i))+": "+str(Items_F[i]))
    
print()    
print(Fer)
print()

def Fonct_S(K, c):
    d = K.copy()
    for i in d:
        for j in c:
            d.remove(j)
    return d
     
print("les régles de confiance : ")    
for i in ListF:
    print("cofiance (",i[0], '->', Fonct_S(i[1], i[0]), ") est de 100%")  



# distance intra inter groupe , comparison kmenas
# clustering à base de click
