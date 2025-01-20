import time

from Cart import Cart
from Customer import Customer
from Fruit import Fruit
from Item import Item
from Stock import Stock
from Vegetable import Vegetable

fruits = list()
vegetables = list()
cart: Cart
carts = list()
HEADER = ["Fruit", "Stock", "Prix (au kg ou à l'unité)", "Légume"]
TABLE_COL = 2
TABLE_HEADER = "+-------" * TABLE_COL + "+---------------------------"
PIECE = "pièce"
KILO = "kg"
USER_MENU = {1: "arrivée du client", 2: "Bilan de la journée"}

# --------------------------Datas-------------------------------------


def init_fruits():
    clementine = Fruit("Clémentine", Stock(6, KILO), 2.90)
    date = Fruit("Datte", Stock(4, KILO), 7.00)
    pomegranate = Fruit("Grenade", Stock(3, KILO), 3.50)
    kaki = Fruit("Kaki", Stock(3, KILO), 4.50)
    kiwi = Fruit("Kiwi", Stock(5, KILO), 3.50)
    mandarin = Fruit("Mandarine", Stock(6, KILO), 2.80)
    orange = Fruit("Orange", Stock(8, KILO), 1.50)
    grapefruit = Fruit("Pamplemousse", Stock(8, PIECE), 2.00)
    pear = Fruit("Poire", Stock(5, KILO), 2.50)
    apple = Fruit("Pomme", Stock(8, KILO), 1.50)
    fruits.append(clementine)
    fruits.append(date)
    fruits.append(pomegranate)
    fruits.append(kaki)
    fruits.append(kiwi)
    fruits.append(mandarin)
    fruits.append(orange)
    fruits.append(grapefruit)
    fruits.append(pear)
    fruits.append(apple)


def init_vegetables():
    carrot = Vegetable("Carotte", Stock(7, KILO), 1.30)
    brussels_sprouts = Vegetable("Choux de Bruxelles", Stock(4, KILO), 4.00)
    green_cabbage = Vegetable("Choux vert", Stock(12, PIECE), 2.50)
    butternut = Vegetable("Courge butternut", Stock(6, PIECE), 2.50)
    chicory = Vegetable("Endive", Stock(5, KILO), 2.50)
    spinach = Vegetable("Épinard", Stock(4, KILO), 2.60)
    leek = Vegetable("Poireau", Stock(5, KILO), 1.20)
    pumpkin = Vegetable("Potiron", Stock(6, PIECE), 2.50)
    black_radish = Vegetable("Carotte", Stock(10, PIECE), 5.00)
    salsify = Vegetable("Salsifis", Stock(7, KILO), 2.50)
    vegetables.append(carrot)
    vegetables.append(brussels_sprouts)
    vegetables.append(green_cabbage)
    vegetables.append(butternut)
    vegetables.append(chicory)
    vegetables.append(spinach)
    vegetables.append(leek)
    vegetables.append(pumpkin)
    vegetables.append(black_radish)
    vegetables.append(salsify)


# --------------------------Menus-------------------------------------


def display_fruits_menu(fruit):
    return f"| {fruit.name} | {fruit.stock.unite} {fruit.stock.type} | {fruit.price} €/{fruit.stock.type}"


def display_vegetables_menu(vege):
    return f"| {vege.name} | {vege.stock.unite} {vege.stock.type} | {vege.price} €/{vege.stock.type}"


def display_menu(index):
    row_fruits = display_fruits_menu(fruits[index])
    row_vegetables = display_vegetables_menu(vegetables[index])

    print(row_fruits + row_vegetables, end="|\n")
    print(TABLE_HEADER + TABLE_HEADER + "+")


def init_table_menu():
    init_fruits()
    init_vegetables()
    print(TABLE_HEADER + TABLE_HEADER + "+")
    print("| " + " | ".join(x for x in HEADER) + f" | {HEADER[1]} | {HEADER[2]} |")
    print(TABLE_HEADER + TABLE_HEADER + "+")
    for i in range(10):
        display_menu(i)


def display_customer_menu():
    return init_table_menu()


def display_balance(carts):

    return


def display_start_menu():
    print("+-------------------------+")
    print(f"| [1]-{USER_MENU[1]}   |")
    print(f"| [2]-{USER_MENU[2]} |")
    print("+-------------------------+")


def display_receipt(cart):
    print("+--------------+")
    print(f"| {cart.customer.name} |")
    print(f"| {cart.customer.first_name} |")
    print("| Listes des achats: |")
    for purchase in cart.purchases:
        print(f"| {purchase} |")
    print("| Total à payer:\n")
    print(f"| {cart.total} |")


# --------------------------Datas-------------------------------------


def valid_choice(guess):
    valid_number = False
    number = None

    print(guess)
    while not valid_number:
        number_str = input().strip()
        if number_str.isdigit():
            number = int(number_str)
            valid_number = number == 1 or number == 2
        else:
            print("Merci de saisir le bon index de menu!")

    return number


def fill_customer(name, firstname):
    customer = Customer(name, firstname)

    return customer


def valid_str(prompt):
    validate_str = False
    name_firstname = None

    print(prompt)
    while not validate_str:
        name_firstname = input().strip()
        if name_firstname.isalpha():
            validate_str = True
        else:
            print("Merci de saisir que des lettres!")

    return name_firstname


def update_stock(item, quantity):
    if item in fruits or item in vegetables:
        item.stock.unite -= quantity


def total_price(quantity, price):
    return quantity * price


def add_purchases():
    display_customer_menu()
    purchase_list: list = fruits + vegetables

    choice = input("Que souhaitez-vous acheter?")

    available_items = [item.name.casefold() for item in purchase_list]
    if choice in available_items:
        quantity = input("Veuillez saisir la quantité:\n")
        item_index = available_items.index(choice)
        item = purchase_list[item_index]
        total_cost = total_price(int(quantity), item.price)
        update_stock(item, int(quantity))
        return Item(choice, int(quantity), total_cost)
    else:
        print("Veuillez choisir un article de la liste !")


def add_to_cart(customer):
    global cart
    purchases: list = list()
    total: float = 0.0
    is_finished = False

    while not is_finished:
        purchase = add_purchases()
        total = total + purchase.total_cost
        purchases.append(purchase)
        cart = Cart(purchases, total, customer)
        carts.append(cart)
        add_article = input("Voulez-vous acheter un autre article? [Y/N]")
        if add_article.casefold() == "n":
            is_finished = True
            display_receipt(cart)
            time.sleep(2)
            init()


def customer_arrival():
    customer_name = valid_str("Veuillez saisir votre nom")
    customer_firstname = valid_str("Veuillez saisir votre prénom")

    customer = fill_customer(customer_name, customer_firstname)
    guess = input("Voulez faire des achats? [Y/N]")
    if guess.casefold() == "y":
        add_to_cart(customer)
    else:
        init()


def init():
    display_start_menu()
    user_choice = valid_choice("Que souhaitez vous faire?")

    match user_choice:
        case 1:
            customer_arrival()
        case 2:
            display_balance(carts)


if __name__ == '__main__':
    init()
