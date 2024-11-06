#Refer https://colab.research.google.com/drive/1WfeiMUjgSnvxC9m5JtXEbQg5AcUlE53w?usp=sharing

#use colab



from google.colab import drive
drive.mount('/content/drive/')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris=pd.read_csv("/content/drive/MyDrive/Iris.csv")

iris.head(10)

sns.barplot(x='Species', y='SepalLengthCm', data=iris)

sns.countplot(x='Species', data=iris)

sns.boxplot(x='Species', y='SepalWidthCm', data=iris)

sns.swarmplot(x='Species', y='SepalWidthCm', data=iris)

sns.distplot(iris['SepalWidthCm'])

sns.jointplot(iris['SepalWidthCm'])

sns.pairplot(data=iris, hue='Species')