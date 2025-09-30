# import random
# while True:
#     user_input = input(
#         'Do you want to roll the Dice? (y/n) or (yes/no):').lower().strip()

#     if user_input in ['yes', 'y']:
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print(f'{dice1} and {dice2}')
#     elif user_input in ['no', 'n']:
#         print('Thank you')
#         break
#     else:
#         print('Invalid input, please enter y/n or yes/no')

# REVERSE A STRING
# user_input = input('Enter a string: ')
# reversed_string = user_input[::-1]
# print(f'Reversed string: {reversed_string}')

# user_input = input('Enter a sentence: ')
# reversed_sentence = user_input.split()[::-1]
# reversed_sentence = ' '.join(reversed_sentence)
# print(f'Reversed sentence: {reversed_sentence}')

# python -m venv venv
import qrcode
data = input('Enter data or link: ')
filename = input('Enter file name: ')
qr = qrcode.QRCode(box_size=15, border=5)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')
