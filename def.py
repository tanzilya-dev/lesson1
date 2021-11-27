def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'


s = get_summ('Learn', 'python')
print(s.upper())


def format_price(price):
    return f'Цена: {int(price)} руб.'


print(format_price(56.24))
