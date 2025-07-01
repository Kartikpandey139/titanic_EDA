import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#open file dialog
Tk().withdraw() #Hide the root window
file_path = askopenfilename(title="titanic_train.csv")


train = pd.read_csv(r'C:\Users\Lenovo\Desktop\python practice\chapter 2\titanic_train.csv')
print(train.head())

print(train.isnull())

# manually checking for each of the elements whether they are null or not will take so much time 
# so will use countplot and set_style
sns.set_style('whitegrid')
sns.countplot(x="Survived",data=train)
sns.countplot(x="Survived",hue='Sex',data=train)

plt.show()