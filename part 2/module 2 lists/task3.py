amount = int(input('Количество видеокарт: '))
old_cards = []

for card in range(amount):
    cardNumber = int(input(f'Видеокарта {card + 1}: '))
    old_cards.append(cardNumber)

print('Старый список видеокарт:', old_cards)
print('Новый список видеокарт:', [card for card in old_cards if card != max(old_cards)])