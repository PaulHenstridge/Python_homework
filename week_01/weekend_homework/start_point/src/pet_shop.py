def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, num_of_pets):
    pet_shop["admin"]["pets_sold"] += num_of_pets


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)
    return found_pets


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None


def remove_pet_by_name(pet_shop, name):
    for i in range(len(pet_shop["pets"])):
        if pet_shop["pets"][i]["name"] == name:
            del pet_shop["pets"][i]
            break


# ALT remove_pet_by_name
# def remove_pet_by_name(pet_shop, name):
# pet_to_delete = find_pet_by_name(pet_shop, name)
# pet_shop["pets"].remove(pet_to_delete)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    return customer["cash"] >= new_pet["price"]


def sell_pet_to_customer(pet_shop, pet, customer):
    if pet == None:
        return
    if customer_can_afford_pet(customer, pet):
        add_or_remove_cash(pet_shop, pet["price"])
        remove_customer_cash(customer, pet["price"])
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(pet_shop, pet["name"])
        increase_pets_sold(pet_shop, 1)
