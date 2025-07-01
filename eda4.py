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

 
# to find the Survived age group as histogram we can do :

sns.histplot(train['Age'].dropna(),kde=False,color='red',bins=40)


plt.show()