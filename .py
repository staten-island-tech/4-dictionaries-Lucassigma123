cart=[]
cost=(0)
item= {
    "name":"pistol",
    "price":"$500",
    "department":"GUNS",
    "description":"very cool pew pew"
}
item1={
    "name":"ak47",
    "price":"$1000",
    "department":"GUNS",
    "description":"Fast fire rate pew pew"
}
item2={
    "name":"rocket launcher",
    "price":"$5000",
    "department":"explosive",
    "description":"boom boom boom"
}
print(item)
print(item1)
print(item2)
while True:
    x= input("choose a gun to buy type no to stop buy and checkout")
    if x== "pistol":
        print("you purchased item pistol ")
        cart.append("pistol")
        cost+=500
    if x=="ak47":
            print("your purchased ak47")
            cart.append("ak47")
            cost+=1000
    if x=="rocket launcher":
                print("you purchased rocket launcher")
                cart.append("rocket launcher")
                cost+=5000
    if x=="no":
        print (cart)
        print ("$" ,cost)
        break


