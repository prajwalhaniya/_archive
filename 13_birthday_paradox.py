import datetime, random

def get_birthdays(number_of_birthdays):
    birthdays = []
    
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2000, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    
    return birthdays

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA

Months = (
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
)

while True:
    print('How many birthdays to generate? (Max: 100)')
    response = input('> ')

    if response.isdecimal() and (0 < int(response) <= 100):
        num_B_days = int(response)
        break
print()

print('Here are', num_B_days, 'Birtydays: ')

birthdays = get_birthdays(num_B_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(',',  end='')
    
    month_name = Months[birthday.month - 1]
    date_text = '{}{}'.format(month_name, birthday.day)
    print(date_text, end='')
print()
print()

match = get_match(birthdays)

print('In this simulation, ', end='')
if match != None:
    month_name = Months[match.month - 1]
    date_text = '{}{}'.format(month_name, match.day)
    print('Multiple people have birthday on', date_text)
else:
    print('There are not matching birthdays')
print()
