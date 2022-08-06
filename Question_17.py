import pandas as pd
import numpy as np
sal=pd.read_csv("D:\\imp docs and courses\\data.csv")
print(sal)
salman=np.array(sal)[: : -1]
print("array of the dataset is ",salman)

faizi=np.array(sal)[:,-1]
print("final results row is ",faizi)

def fun(c,faizi):
    for i,val in enumerate(faizi):
        if val=="yes":
            specific_hypothesis=c[i].copy()
            break
    for i, val in enumerate(c):
        if faizi[i]=='yes':
            for x in range(len(specific_hypothesis)):
                if val[x]!=specific_hypothesis[x]:
                    specific_hypothesis[x]="?"
                else:
                    pass
    return specific_hypothesis
print("the final hypothesis is:",fun(salman,faizi))