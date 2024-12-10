
item_dict = {}
f = open("D:\\Grocery shop.txt","r")
while True:
    item = f.readline()
    if item == "\n":
        break
    quant = f.readline()
    uprice = f.readline()
    item = item[:len(item)-1]
    quant = int(quant[:len(quant)-1])
    uprice = float(uprice[:len(uprice)-1])
    item_dict[item]=[quant,uprice]
f.close()

"""
item_dict = {"milk":[5000,2.25],
             "oil":[1500,3.50],
             "biscuit":[4000,4.45],
             "chips":[3000,1.50],
             "tissues":[2500,5.00],
             "toothpaste":[3500,8.50],
             "lotion":[5500,7.75],
             "bread":[2000,4.50]}
"""
def present_data():
  print(29*"=")
  print("** Grocery Item List **".center(29))
  print(29*"=")
  for x in item_dict:
     print(x,(20-len(x))*" ",(6-len(str(item_dict[x][0])))*" ", item_dict[x][0])
  print(30*"-")
present_data()

def decrease_quantity(item,amount):
  item_dict[item][0]-= amount
  
def increase_quantity(item,amount):
  item_dict[item][0]+= amount
  
def receive_order():
   while True:
     item = input("Item (type 'x' to stop):")
     if item == 'x':
         break
     amount = int(input("Amount: "))
     if  item not in item_dict:
           print("New item fount!")
           uprice = float(input("Enter the unit price: "))
           item_dict[item] = [amount,uprice]
           continue
     increase_quantity (item,amount)
   present_data()
   
def process_demand():
    demand_list = []
    while True:
       item =  input("Item (type 'x' to stop):")
       if item == 'x':
          break
       if  item not in item_dict:
           print("Sorry! Item is not available")
           continue
       amount = int(input("Amount: "))
       if amount>item_dict[item][0]:
          print("Total{item_dict[item][0]} pcs available!")
          continue
       decrease_quantity(item,amount)
       demand_list+=[item,amount,item_dict[item][1],amount*item_dict[item][1]],
    print(40*"=")
    print("** Payment Receipt **".center(40))
    print(40*"=")
    print("Item,s Name",3*" ","Quant.","U.price"," ","S.Total")
    print(40*"-")
    tprice = 0
    for x in demand_list:
        tprice+=x[3]
        print(x[0].title(),(14-len(x[0]))*" ",(5-len(str(x[1])))*" ",x[1],(6-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],(8-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print(40*"-")
    tprice = "%.2f"%tprice
    print("Total Price:", (26-len(str(tprice)))*" ",tprice)
    print(40*"-")
   # process_demand()



while True:
    present_data()
    print("Pick an option: ")
    print("Type '1': To process demand")
    print("Type '2': To receive order")
    print("Type '3': To exit the program")
    pick = input("Pick:")
    if pick =='1':
        process_demand()
    elif pick =='2':
        receive_order()
    elif pick =='3':
        break
    else:
        continue
f = open("D:\\Grocery shop.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write(str(item_dict[x][0])+"\n")
    f.write(str(item_dict[x][1])+"\n")
f.write("\n")
f.close()
present_data()
            



        
        



    
    
    
