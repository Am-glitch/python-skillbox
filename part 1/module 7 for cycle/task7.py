missing_card = 0
known_cards = []
N = int(input('Введите количество карточек: '))
cards_left = N - 1

for card in range(cards_left):
    known_cards.append(int(input('Введите номер оставшейся карточки: ')))

for card_index in range(len(known_cards)):
    if (card_index + 1) != sorted(known_cards)[card_index]:
        missing_card = card_index + 1
        break

print(missing_card)
