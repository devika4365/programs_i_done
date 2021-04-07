def highest_order_item(items_dict):
    food_item=max(items_dict, key=items_dict.get)
    return food_item
        
items=int(input("Enter items count"))
items_dict={}
for i in range(items):
    items_dict[input("item_name:")]=int(input("order_count:"))
    #items_dict[i].append(int(input("order count:")))
print(items_dict)
print(highest_order_item(items_dict))
