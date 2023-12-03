import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
one_touch1=list()
one_touch2=list()
j=0
for i in lst:
    if i=='robot':
        one_touch1.append(1)
        one_touch2.append(0)
    else:
        one_touch1.append(0)
        one_touch2.append(1)
    j=+1
data = pd.DataFrame({'robot':one_touch1, 'human':one_touch2})
print(data.head())
