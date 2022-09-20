in_s = input('enter your string: ')


while True:
    if len(in_s) > 5 or in_s == '':
        in_s = input('Your string must be 1 to 5 characters. Re-enter your string: ')
        continue
    else:
        break


print(f"Great! Thanks for entering the string '{in_s}'")


def check_input(input_val, condition, err_msg=''):
    while True:
        if not condition:
            input_val = input(f'{err_msg}: ')
            continue
        else:
            break
            return input_val