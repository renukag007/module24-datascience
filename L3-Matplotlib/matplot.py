# Refer https://colab.research.google.com/drive/1THcuKuoAAuPco6vV-N-uGzMEawtt3nlR?usp=sharing

# use the colab file



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive/')

train=pd.read_csv("/content/company_sales_data.csv")

train

**Read Total profit of all months and show it using a line plot**

profitList = train ['total_profit'].tolist()
monthList  = train ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

Get total profit of all months and show line plot with the following Style properties

Generated line plot must include following Style properties: –

    Line Style dotted and Line-color should be red
    Show legend at the lower right location.
    X label name = Month Number
    Y label name = Sold units number
    Add a circle marker.
    Line marker color as read
    Line width should be 3 **bold text** **bold text**

profitList = train ['total_profit'].tolist()
monthList  = train ['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Profit data of last year',
      color='r', marker='o', markerfacecolor='k',
      linestyle='--', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

**Read all product sales data and show it  using a multiline plot**

monthList  = train ['month_number'].tolist()
faceCremSalesData   = train ['facecream'].tolist()
faceWashSalesData   = train ['facewash'].tolist()
toothPasteSalesData = train ['toothpaste'].tolist()
bathingsoapSalesData   = train ['bathingsoap'].tolist()
shampooSalesData   = train ['shampoo'].tolist()
moisturizerSalesData = train ['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()

**Read face cream and facewash product sales data and show it using the bar chart**

monthList  = train['month_number'].tolist()
faceCremSalesData   = train ['facecream'].tolist()
faceWashSalesData   = train['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()