#根据之制定年月日打出日期
months=[
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'Agust',
    'September',
    'October',
    'November',
    'December',
    ]
#以1-31结尾
endings=['st','nd','ra']+17*['th']\
         ['st','nd','ra']+7*['th']\
         +['st']

year=raw_input('Year:')
month=raw_input('Month(1-12):')
day=raw_input('Day(1-31):')

month_number=int(month)
day_number=int(day)

month_name=months[month_number-1]
ordinal=day+endings[day_number-1]

print month_name+' '+ordinal+','+year
