def get_mask_account(account_number: str) ->str:
    '''Функция, которая маскируют счет'''
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return "Номер счета введен неверно(стандартный номер счета содержит - 20 цифр)"


def get_mask_card_number(card_number: str) ->str:
    '''Функция, которая маскирует номер карты'''
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Номер карты введен неверно(стандартный номер карты содержит - 16 цифр)"