YES = ['y', 'yes']
NO = ['n', 'no']


def create_store_table(stores):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|')
    print('-' * 50)
    for store in stores:
        id_spaces = 4 - len(str(store.id))
        name_spaces = 43 - len(store.name)
        print(f'|{store.id}{" " * id_spaces}|{store.name}{" " * name_spaces}|')
    print('-' * 50)


def create_customer_table(customers):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|BUDGET{" " * 8}|')
    print('-' * 50)
    for customer in customers:
        id_spaces = 4 - len(str(customer.id))
        name_spaces = 43 - len(customer.name)
        budget_spaces = 16 - len(str(customer.budget))
        print(f'|{customer.id}{" " * id_spaces}|{customer.name}{" " * name_spaces}|{customer.budget}{" " * budget_spaces}|')
    print('-' * 50)


def create_store_clothing_table(clothes):
    print('-' * 50)
    print(f'|ID  |BRAND{" " * 15}|TYPE{" " * 15}|PRICE{" " * 8}|')
    print('-' * 50)
    for cloth in clothes:
        id_spaces = 4 - len(str(cloth.id))
        brand_spaces = 20 - len(cloth.brand)
        type_spaces = 20 - len(cloth.clothing_type)
        price_spaces = 16 - len(str(cloth.price))
        print(f'|{cloth.id}{" " * id_spaces}|{cloth.brand}{" " * brand_spaces}|{cloth.clothing_type}{" " * type_spaces}|{cloth.price}{" " * price_spaces}|')
    print('-' * 50)


def create_customer_clothing_table(clothing):
    print('-' * 50)
    print(f'|ID  |BRAND{" " * 15}|TYPE{" " * 15}|')
    print('-' * 50)
    for cloth in clothing:
        id_spaces = 4 - len(str(cloth.id))
        brand_spaces = 20 - len(cloth.brand)
        type_spaces = 20 - len(cloth.clothing_type)
        print(f'|{cloth.id}{" " * id_spaces}|{cloth.brand}{" " * brand_spaces}|{cloth.clothing_type}{" " * type_spaces}|')
    print('-' * 50)


def payment():
    pass
