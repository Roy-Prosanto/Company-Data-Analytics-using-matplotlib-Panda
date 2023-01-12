bars =pd.read_csv("G:\\Project\\Alaxe\\company_sales_data.csv")
wight=float(0.2)
month=bars['month_number'].tolist()
face_cream  = bars["facecream"].tolist()
facewashdata =bars["facewash"].tolist()
plt.bar([a-0.25 for a in month],face_cream,width=.25,label="face_cream",align='edge')
plt.bar([a+0.25 for a in month], facewashdata ,width=-.25,label="facewashdata",align='edge')

plt.xticks(month)

plt.legend(loc='upper left')
plt.grid(linestyle="--",color= "r")
plt.show()