import copy

def create_site(product_name):
    return {
        'html': {
            'head': {
                'title': f'Куплю/продам {product_name} недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {product_name}',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }

def print_sites(products, sites):
    for product, site in zip(products, sites):
        print(f"Сайт для: {product}: \n{site}\n")

def main():
    num_sites = int(input("Сколько сайтов: "))
    sites = []
    products = []

    for _ in range(num_sites):
        product_name = input("Введите название продукта для нового сайта: ")
        products.append(product_name)
        new_site = create_site(product_name)
        sites.append(copy.deepcopy(new_site))
        print_sites(products, sites)

if __name__ == "__main__":
    main()
