sentence = input('Sentence:')
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print(' ' * left_margin + '+' + '_' *(box_width -2) + '+')
print(' ' * left_margin + ' '* 2  + '|' + ' '* text_width + '|')
print(' ' * left_margin +' '*2+'|' + sentence + '|')
print(' ' * left_margin + ' ' * 2 + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '+' + '_' *(box_width -2) + '+')
