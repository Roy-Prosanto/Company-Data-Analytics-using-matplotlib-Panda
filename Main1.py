# ( Read Bathing soap facewash of all months )
df = pd.read_csv("G:\\Project\\Alaxe\\company_sales_data.csv")

monthList  = df ['month_number'].tolist()
bathingsoap   = df ['bathingsoap'].tolist()
faceWashSalesData   = df ['facewash'].tolist()
plt.figure(figsize=(12,7))
plt.subplot(2,1,1)
plt.title('Sales data of  a Bathingsoap')
plt.plot(monthList,bathingsoap, color="black",marker='o', linewidth=3)
plt.grid()
plt.xticks(monthList)

plt.subplot(2,1,2)
plt.title('Sales data of  a facewash')
plt.plot(monthList,bathingsoap, color="r",marker='o', linewidth=3)
plt.grid()

plt.xticks(monthList)
plt.xlabel("Month number")
plt.ylabel("sales units in numbers r")


# (all product sales   stack polt)
def1= pd.read_csv("G:\\Project\\Alaxe\\company_sales_data.csv")
faceCremSalesData   = def1 ['facecream'].tolist()
faceWashSalesData   = def1 ['facewash'].tolist()
toothPasteSalesData = def1 ['toothpaste'].tolist()
bathingsoapSalesData   = def1 ['bathingsoap'].tolist()
shampooSalesData   = def1 ['shampoo'].tolist()
moisturizerSalesData = def1 ['moisturizer'].tolist()
monthList  = def1 ['month_number'].tolist()

plt.plot([],[],color="m",label="faceCremSalesData",linewidth=5)
plt.plot([],[],color="c",label="faceWashSalesData",linewidth=5)
plt.plot([],[],color = "r",label="toothPasteSalesData",linewidth=5)
plt.plot([],[],color= "k",label="bathingsoapSalesData",linewidth=5)
plt.plot([],[],color="g",label="shampooSalesData",linewidth=5)
plt.plot([],[],color= "y",label="moisturizerSalesData",linewidth=5)


plt.stackplot(monthList,faceCremSalesData,faceWashSalesData,toothPasteSalesData,bathingsoapSalesData,shampooSalesData,moisturizerSalesData,  colors=['m','c','r','k','g','y'])

plt.legend()

plt.xlabel(monthList)
plt.ylabel("Seles units in NUmber")

plt.show()
