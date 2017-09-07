#使用给定宽度答应格式化的价格列表
width=input('Please enter width:')
price_width=10
item_width=width-price_width
header_format='%-*s%*s'
format='%-*s%*.2f'
print '=' *width
print format%(item_width,'Apple',price_width,0.4)
print format%(item_width,'Pears',price_width,0.5)
print format%(item_width,'Cantalouples',price_width,1.92)
print format%(item_width,'Dried Apricots(16 oz.)',price_width,8)
print format%(item_width,'prunes',price_width,12)
print'='*width
