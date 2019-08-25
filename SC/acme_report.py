import random
from random import randint, sample, uniform
from acme import Product
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(n=30):
    product_list = []
    for i in range(0,n):
        product_name = random.choice(ADJECTIVES) + "" + random.choice(NOUNS)
        weight = random.randint(5,101)
        price = random.randint(5,101)
        flammability = random.uniform(0,2.5)
        product = Product(product_name, weight=weight, price=price, flammability=flammability)
        product_list.append(product)
    return product_list

def inventory_report(product_list):
    unique_product_list = []
    weight_list = []
    price_list = []
    flam_list = []

    for i in product_list:
        if i.name not in unique_product_list:
            unique_product_list.append(i.name)
        
        weight_list.append(i.weight)
        price_list.append(i.price)
        flam_list.append(i.flammability)

    def mean(num_list):
        return round(sum(num_list)/float(len(num_list)),2)

    print('# unique products:', len(unique_product_list))
    print('avg products price', mean(price_list))
    print('avg products weight', mean(weight_list))
    print('avg products flammability', mean(flam_list))

if __name__ == '__main__':
    inventory_report(generate_products())
