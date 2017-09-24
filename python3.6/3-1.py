width = int(input('Please enter width:'))
price_width = 10
iten_width = width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'
print('=' * width)
print(format % (iten_width, 'Apples',price_width,0.4))
print(format % (iten_width, 'Pears',price_width,0.45))
print(format % (iten_width, 'Apples',price_width,0.4))
print(format % (iten_width, 'Apples',price_width,0.4))
print('=' * width)