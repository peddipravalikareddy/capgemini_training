# CITIES:

cities = [
    {"name": "New York", "population": 8419600},
    {"name": "Los Angeles", "population": 3980400},
    {"name": "Chicago", "population": 2716000},
    {"name": "Houston", "population": 2328000}
]
result=sorted(cities,key=lambda x:-x['population'])
print(list(result))


#CONVERTING PRICES
PricesList_inr =[3000,56000,45000,2300]
euro_convert=map(lambda x:x/90,PricesList_inr)
USD_convert=map(lambda x:x/86,PricesList_inr)
print(list(euro_convert))
print()
print(list(USD_convert))


#EMAILS
user_emails=[
    {"email":"alice@example.com","verified":True},
    {"email":"bob@example.com","verified":False},
    {"email":"alice@example.com","verified":True},
    {"email":"alice@example.com","verified":False},
]
user=filter(lambda x:x["verified"]==True,user_emails)
print(list(user))


#FILTER_ODD & DOUBLE_EVEN
numbers=[11,12,13,4,5]
odd=filter(lambda x:x%2!=0,numbers)
print(list(odd)) 
even=filter(lambda x:x%2==0,numbers)
result=map(lambda x:x*2,even)
evenlist=list(result)
print(evenlist)
evenlist.sort()
print(evenlist)
# sorted_result=sorted(result,key=lambda x:x)
# print(list(sorted_result))

#PRODUCT_SORT
products = [
    {"name": "Laptop", "price": 92000},
    {"name": "Smartphone", "price": 48000},
    {"name": "Tablet", "price": 20000},
    {"name": "Monitor", "price": 8000}
    ]
result=sorted(products,key=lambda x:x["price"])
print(list(result))


#PRODUCTS_DISCOUNT
products = [
     {"name": "Laptop", "price": 1200},
     {"name": "Headphones", "price": 80},
     {"name": "Smartphone", "price": 700},
     {"name": "Monitor", "price": 150}
]
products=map(lambda x: {'name':x['name'],'price':x['price']*0.8}, filter(lambda x: x['price']>100 , products))
print(list(products))


#REMOVE_DUPLICATES
numbers3=[2,2,4,6,3,4,6,1]
print(list(set(numbers3)))



#SORTWORDS_LENGTH
words = ["apple", "banana", "cherry", "date", "fig"]
sorted_words=list(sorted(words,key=lambda x: len(x)))
print(sorted_words)


#STUDENT_NAMELIST
student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
loan_names=[]
for item in student_name_list:
    if len(item)>6:
        loan_names.append(item)
print(list(loan_names))

