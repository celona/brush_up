#!/usr/bin/env python
# coding: utf-8

# In[97]:


import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# In[98]:


data = pd.read_csv('/home/celona/Documents/Learnings/brush_up/Untitled Folder 1/car.data')
data.head()


# In[99]:


x = data[['buying','maint','safety']].values
y = data[['class']]
x = np.array(x)
# x[:,1]


# In[100]:


# print(x.shape,y.shape)


# In[101]:


#coversion
le = LabelEncoder()
# print(len(x[0]))
for i in range(len(x[0])):
    x[:,i] = le.fit_transform(x[:,i])


# In[102]:


print(x)


# In[103]:


label_mapping = {
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
}
# y['class']


# In[104]:


y['class'] = y['class'].map(label_mapping)
y = np.array(y)


# In[105]:


# create model
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')


# In[106]:


X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2)
knn.fit(X_train,Y_train) 


# In[107]:


prediction = knn.predict(X_test)

accuracy = metrics.accuracy_score(Y_test,prediction)
print("prediction:", accuracy)


# In[ ]:




