import pdb

def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    snacks = person["favourites"]["snacks"]
    likes_food = False
    for snack in snacks:
        if snack == food:
            likes_food = True
    return likes_food

def add_friend(person, new_friend):
    friend_list = person["friends"]
    friend_list.append(new_friend)
    print(friend_list)

def remove_friend(person, delete_friend):
    friend_list = person["friends"]
    on_list = False
    for friend in friend_list:
        if friend == delete_friend:
            on_list = True
    if on_list == True:
        entry_index = friend_list.index(delete_friend)
        del friend_list[entry_index]
    return len(friend_list)

def total_money(people):
    total_monies = 0
    for person in people:
        total_monies += person["monies"]
    return total_monies