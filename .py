cart=[]
cost=0
items=[
    {
        "name":"pistol",
        "price":500,
        "department":"GUNS",
        "description":"very cool pew pew"
    },
    {
        "name":"ak47",
        "price":1000,
        "department":"GUNS",
        "description":"Fast fire rate pew pew"
    },
    {
        "name":"rocket launcher",
        "price":5000,
        "department":"explosive",
        "description":"boom boom boom"
    }
]

for index, item in enumerate(items):
        print(index, ":", item["name"], index,":", item["price"])
while True:
        x=input("choose da items type 3 to checkout")
        if x==3:
                print(cart)
                print(cost)
                break
        y=items[int(x)]
        print(f"you buy",{y["name"]})
        cart.append(y["name"])
        cost+= y["price"]
        

       
    
