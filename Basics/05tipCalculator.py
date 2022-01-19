bill = input('enter the total bill: ')
tip = input('what is the tip percentage: ')
split = input('how many people want to split the bill: ')

perhead = round((float(bill) / int(split)) * (1 + float(tip)/100))

print('each person should pay: ', perhead)