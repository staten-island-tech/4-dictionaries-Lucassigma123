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
        x=input("choose da items ")
        y=items[int(x)]
        print(f"you buy",{y["name"]})
        cart.append(y["name"])
        cost+= y["price"]
        z=input("yes to checkout type anything else to continue")
        if z.lower=="yes":
                print(cart)
                print(cost)

       
    
