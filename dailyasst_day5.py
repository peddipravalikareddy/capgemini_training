#You have sales data for different regions and want to calculate the total sales for each region.

def sales_cal(a):
    total_sales=0
    for i in range(len(a)):
        total_sales+=a[i]["sales"]
    return total_sales
sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
]

#filtering each region
north=filter(lambda x:x["region"]=='North',sales_data)
south=filter(lambda x:x["region"]=='South',sales_data)
east=filter(lambda x:x["region"]=='East',sales_data)
west=filter(lambda x:x["region"]=='West',sales_data)

#converting class filter to list
north=list(north)
south=list(south)
east=list(east)
west=list(west)

updated_sales=[{"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},]

for i in sales_data:
    if i["region"]=="North":
        updated_sales[0]["sales"]=sales_cal(north)
    elif i["region"]=="South":
        updated_sales[1]["sales"]=sales_cal(south)
    elif i["region"]=="West":
        updated_sales[2]["sales"]=sales_cal(west)
    elif i["region"]=="East":
        updated_sales[3]["sales"]=sales_cal(east)
print(list(updated_sales))


# 2) Store management calculate the current stock and display current stock
   
initial_stock = {"apple": 50,"banana": 100,"orange": 75}
sold_item = {"apple": 10, "banana": 20, "orange": 15}
print(initial_stock.get('apple')-sold_item.get('apple'))
for i in initial_stock:
    initial_stock[i]=initial_stock.get(i)-sold_item.get(i)
print(initial_stock)



#phonenumber
phone_number={1:' one ',2:' two ',3:' three ',4:' four ',5:' five ',6:' six ',7:' seven ',8:' eight ',9:' nine ',0:' zero '}
n=input("Enter the phonenumber : ")
for i in n:
    print(phone_number.get(int(i)),end="")
