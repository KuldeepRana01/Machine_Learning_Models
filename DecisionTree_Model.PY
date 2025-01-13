import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import sys
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
df=pd.read_csv('d:/data/DecisionTree.csv',sep=',',header=0)
print(df)
value=['Outlook','Temp','Humidity','Wind']
string_to_int=preprocessing.LabelEncoder()
df=df.apply(string_to_int.fit_transform)
print(df)
feature_cols=['Outlook','Temp','Humidity','Wind']
X=df[feature_cols]
y=df.PlayTennis
test=pd.DataFrame({'Outlook':[1],'Temp':[1],'Humidity':[1],'Wind':[1]})
print(test)
dtree = DecisionTreeClassifier(criterion='entropy',random_state=100)
dtree=dtree.fit(X,y)
tree.plot_tree(dtree, feature_names=feature_cols)
y_pred=dtree.predict(test)
print(y_pred)
plt.show()
#plt.savefig("F:/dt.png")