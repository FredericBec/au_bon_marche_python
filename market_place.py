import time
from typing import Optional

import unicodedata

from Cart import Cart
from Customer import Customer
from Fruit import Fruit
from Item import Item
from Stock import Stock
from Vegetable import Vegetable

# --------------------------Constant-------------------------------------

fruits = list()
vegetables = list()
cart: Cart
carts = list()
HEADER = ["Fruit", "Stock", "Prix (au kg ou à l'unité)", "Légume"]
TABLE_LEFT_HEADER = "---------------+---------+---------------------------+"
TABLE_RIGHT_HEADER = "----------------------+----------+---------------------------+"
COL_FRUIT_HEADER = f"|    {HEADER[0]}      |  {HEADER[1]}  | {HEADER[2]} "
COL_VEGETABLE_HEADER = f"|       {HEADER[3]}         |  {HEADER[1]}   | {HEADER[2]} |"
BALANCE_HEADER = "+-------------------------------------+"
PIECE = "pièce"
KILO = "kg"
USER_MENU = {1: "arrivée du client", 2: "Bilan de la journée"}

# --------------------------Datas-------------------------------------


def init_fruits() -> None:
    """
    Initialize fruits datas
    """
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


def init_vegetables() -> None:
    """
    Initialize vegetables datas
    """
    carrot = Vegetable("Carotte", Stock(7, KILO), 1.30)
    brussels_sprouts = Vegetable("Choux de Bruxelles", Stock(4, KILO), 4.00)
    green_cabbage = Vegetable("Choux vert", Stock(12, PIECE), 2.50)
    butternut = Vegetable("Courge butternut", Stock(6, PIECE), 2.50)
    chicory = Vegetable("Endive", Stock(5, KILO), 2.50)
    spinach = Vegetable("Épinard", Stock(4, KILO), 2.60)
    leek = Vegetable("Poireau", Stock(5, KILO), 1.20)
    pumpkin = Vegetable("Potiron", Stock(6, PIECE), 2.50)
    black_radish = Vegetable("Radis noir", Stock(10, PIECE), 5.00)
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


def display_fruits_menu(fruit) -> str:
    """
    display all fruits and formatting them
    :param fruit: each fruit in fruits list
    :return: formatting str
    """
    return (f"| {fruit.name.ljust(13)} | {fruit.stock.unite} {fruit.stock.type.ljust(5)} " +
            f"| {str(fruit.price).rjust(8)} €/{fruit.stock.type.ljust(15)}")


def display_vegetables_menu(vege) -> str:
    """
    display all vegetables and formatting them
    :param vege: vegetable in vegetables list
    :return: formatting str
    """
    return (f"| {vege.name.ljust(20)} | {str(vege.stock.unite).rjust(2)} {vege.stock.type.ljust(5)} " +
            f"| {str(vege.price).rjust(8)} €/{vege.stock.type.ljust(15)}")


def display_menu(index) -> None:
    """
    Display the table of articles
    :param index: integer
    """
    row_fruits = display_fruits_menu(fruits[index])
    row_vegetables = display_vegetables_menu(vegetables[index])

    print(row_fruits + row_vegetables, end="|\n")
    print("+" + TABLE_LEFT_HEADER + TABLE_RIGHT_HEADER)


def init_table_menu() -> None:
    """
    Initialize the table of articles for the menu
    """
    init_fruits()
    init_vegetables()
    print("+" + TABLE_LEFT_HEADER + TABLE_RIGHT_HEADER)
    print(COL_FRUIT_HEADER + COL_VEGETABLE_HEADER)
    print("+" + TABLE_LEFT_HEADER + TABLE_RIGHT_HEADER)
    for i in range(10):
        display_menu(i)


def display_customer_menu() -> None:
    """
    Display table of articles
    :return: function which initialize the table
    """
    return init_table_menu()


def display_balance(cart_list: list) -> None:
    """
    Display the balance of the day and calculate the total of the day
    :param cart_list: list with all information of clients
    """
    total_day_balance = total_balance(cart_list)
    print(BALANCE_HEADER)
    print(" Liste des clients: ")
    print(BALANCE_HEADER)
    print(" Client     | Achats     | Total")
    print(BALANCE_HEADER)
    for cart_cust in cart_list:
        cust_str = repr(cart_cust.customer)
        purchases_str = "-".join([f"{item.name} x{item.quantity} : {item.total_cost}€" for item in cart_cust.purchases])
        total_str = f"{cart_cust.total:.2f}"
        print(" " + cust_str + " | " + purchases_str + " | " + total_str + "€\n")
    print(BALANCE_HEADER)
    print("            Total de la journée: ")
    print(f"                    {total_day_balance:.2f}€")
    print(BALANCE_HEADER)
    back_to_menu()


def display_start_menu() -> None:
    """
    Display the first menu of application
    """
    print("+-------------------------+")
    print(f"| [1]-{USER_MENU[1]}   |")
    print(f"| [2]-{USER_MENU[2]} |")
    print("+-------------------------+")


def display_receipt(cart_customer: Cart) -> None:
    """
    Display customer receipt
    :param cart_customer: cart of the customer
    """
    print("+-------------------+")
    print(" Nom: " + f"{cart_customer.customer.name}")
    print(" Prénom: " + f"{cart_customer.customer.first_name}")
    print(" Listes des achats: ")
    print(" " + " |".join(repr(purchase).replace(",", " -") for purchase in cart_customer.purchases), end="\n")
    print("\n Total à payer: ")
    print(f" {cart_customer.total}€ ")
    print("+-------------------+")
    print()


def back_to_menu():
    """
    Allow user to return to the main menu and reset carts list
    """
    reset_carts()
    time.sleep(2)
    init()


# --------------------------Validate-------------------------------------


def normalize_string(s: str) -> str:
    """
    Method for ignoring accent in choice
    :param s: entry to verify
    :return: normalizing str
    """
    return unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('utf-8').casefold()


def valid_choice(guess: str) -> int | None:
    """
    Method for verify if the user choose the right number
    :param guess: question to the user
    :return: cast number
    """
    valid_number: bool = False
    number: Optional[int] = None

    print(guess)
    while not valid_number:
        number_str = input().strip()
        if number_str.isdigit():
            number = int(number_str)
            valid_number = number == 1 or number == 2
        else:
            print("Merci de saisir le bon index de menu!")

    return number


def valid_str(prompt) -> str | None:
    """
    Method for verify the right entry
    :param prompt: question to the user
    :return: verifying str
    """
    validate_str: bool = False
    string = None

    print(prompt + "\n")
    while not validate_str:
        string = input().strip()
        if string.isalpha():
            validate_str = True
        else:
            print("Merci de saisir que des lettres!")

    return string


def valid_quantity(prompt, item) -> int:
    """
    Verify if the quantity is not higher than the stock
    :param prompt: question to the customer
    :param item: article
    :return: quantity
    """
    validate_quantity: bool = False
    quantity = None
    print(prompt)

    while not validate_quantity:
        quantity = int(input().strip())
        if item.stock.unite > quantity > 0:
            validate_quantity = True
        else:
            print("Merci de saisir une quantité valide!")

    return quantity


# --------------------------Functions-------------------------------------


def fill_customer(name: str, firstname: str) -> Customer:
    """
    Method to fill customer information
    :param name: customer name
    :param firstname: customer firstname
    :return: customer
    """
    customer: Customer = Customer(name, firstname)

    return customer


def update_stock(item, quantity: int) -> None:
    """
    Update the stock
    :param item: article
    :param quantity: quantity of article
    """
    if item in fruits or item in vegetables:
        item.stock.unite -= quantity


def total_price(quantity: int, price: float) -> float:
    """
    Calculate the total of each article
    :param quantity: quantity of article
    :param price: price of article
    :return: total
    """
    return quantity * price


def total_balance(cart_list: list) -> float:
    """
    Calculate the total of day balance
    :param cart_list: list of cart
    :return: sum of total
    """
    return sum(cart_cust.total for cart_cust in cart_list)


def add_purchases() -> Item:
    """
    Allow customer to choose article
    :return: Item or message
    """
    while True:
        display_customer_menu()
        purchase_list: list = fruits + vegetables

        choice: str = input("Que souhaitez-vous acheter?")
        normalize_choice = normalize_string(choice.casefold())

        available_items = [normalize_string(item.name) for item in purchase_list]
        item_index = available_items.index(choice)
        item = purchase_list[item_index]
        if item.stock.unite == 0:
            print("Cet article n'est plus disponible")
            time.sleep(2)
        else:
            if normalize_choice in available_items:
                quantity: int = valid_quantity("Veuillez saisir la quantité:", item)
                total_cost = total_price(quantity, item.price)
                update_stock(item, quantity)
                return Item(choice, quantity, total_cost)
            else:
                print("Veuillez choisir un article de la liste !")


def add_to_cart(customer: Customer) -> None:
    """
    Allow customer to add article to cart
    :param customer: customer
    """
    global cart
    purchases: list = list()
    total: float = 0.0
    is_finished: bool = False

    while not is_finished:
        purchase: Item = add_purchases()
        total = total + purchase.total_cost
        purchases.append(purchase)
        cart = Cart(purchases, total, customer)
        add_article: str = valid_str("Voulez-vous acheter un autre article? [Y/N]")
        if add_article.casefold() == "n":
            carts.append(cart)
            is_finished = True
            display_receipt(cart)
            time.sleep(2)
            init()


def customer_arrival() -> None:
    """
    Method for ask user information
    """
    customer_name: str | None = valid_str("Veuillez saisir votre nom")
    customer_firstname: str | None = valid_str("Veuillez saisir votre prénom")

    customer = fill_customer(customer_name, customer_firstname)
    guess = input("Voulez faire des achats? [Y/N]")
    if guess.casefold() == "y":
        add_to_cart(customer)
    else:
        init()


def reset_carts() -> None:
    """
    Clear all elements of carts list
    :return:
    """
    return carts.clear()


def init() -> None:
    """
    Method for display the main menu and ask user to choose an action
    """
    display_start_menu()
    user_choice: int | None = valid_choice("Que souhaitez vous faire?")

    match user_choice:
        case 1:
            customer_arrival()
        case 2:
            display_balance(carts)


# --------------------------Main-------------------------------------


if __name__ == '__main__':
    reset_carts()
    init()
