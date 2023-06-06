#import pandas as pd
import numpy as np
import pandas as pd

Z = np.zeros((4,))

print("Z", Z)

Z = np.zeros((4,))
Z[1] = 1.

print("Z", Z)

Z = np.zeros((4,))
Z[1:] = 1.

print("Z", Z)

#Z = np.zeros((4,))
Z = np.zeros((4, )) 
Z[:3] = 1.
#Z[:3] = 1.

print("Z", Z)


#X = np.twos((2, 2))

#X = 2 * np.ones((2, 2))

#X = np.ones((2, 2)) + np.ones((2, 2))

X = np.array([2.] * 4).reshape(2, 2)
#X = np.array([[2.,2.],[2.,2.]])

print("X:\n",X)

X = np.array([[1,2],[3,4]])
Y = X[0, :]
Y[1] = 10
print("X:\n", X)

X = np.array([[1,3],[11,10]])
print(np.mean(X[X > np.pi]))

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog','cat', 'snake','cat', 'dog', 'dog'],
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
'visits': [1,3,2,3,2,3,1,1,2,1],
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(data=data, index=labels)



print(df.sort_values(by='visits', ascending=False))

#print(df.sort_index(by='visits', ascending=False))

#print(df.sort_index(by='visits'))

print(df.sort_values(by='visits'))
#print(df.describe())

y_true = np.array([1.,2.,1.])
y_pred = np.array(-y_true)

print(y_true)
print(y_pred)

print(np.sqrt(((y_true-y_pred)**2).mean()))