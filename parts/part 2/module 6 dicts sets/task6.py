clients = dict()

amount = int(input('Введите количество заказов: '))

for i_client in range(amount):
    order = input(f'{i_client + 1}-й заказ: ')

    firstname = order.split()[0]
    pizza = order.split()[1]
    quantity = int(order.split()[2])

    if (firstname in clients.keys()):
        for i_row in range(len(clients[firstname])):
            if (clients[firstname][i_row]['pizza'] == pizza):
                clients[firstname][i_row]['quantity'] += quantity
            else:
                clients[firstname].append({
                'pizza': pizza,
                'quantity': quantity
            }) 
    else:
        clients[firstname] = [{
            'pizza': pizza,
            'quantity': quantity
        }]

for client in clients:
    print(f'{client}:')
    for i_order in range(len(clients[client])):
        print(f'{clients[client][i_order]["pizza"]}: {clients[client][i_order]["quantity"]}')
