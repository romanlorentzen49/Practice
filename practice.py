restaurants=["In N Out", "McDonads","Chick Fil A", "Jack in the Box", "Taco Bell"]

new_res = input("What restaurant would you like to rank into your list?")

def rank_restaurant(new_res, restaurants):
    
    for i in range(len(restaurants)):

        rank = input("Do you like A)" + new_res + " more or B)"+restaurants[i]+"more? A/B")

        if rank=="A":
            restaurants.insert(i, new_res)
            break
        elif rank== "B":
            continue
    return restaurants

print("Your new resturants is ", rank_restaurant(new_res,restaurants))