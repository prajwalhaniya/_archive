'''
In this problem, we’ll assume that phone numbers are four digits. A phone number belongs to a telemarketer if its four digits satisfy all three of the following properties:

• The first digit is 8 or 9.
• The fourth digit is 8 or 9.
• The second and third digits are the same.

For example, a phone number whose four digits are 8119 belongs to a telemarketer. Determine whether a phone number belongs to a telemarketer, and indicate whether we should answer the phone or ignore it.
'''

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if ((num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num4)):
    print('IGNORE')
else:
    print('answer')