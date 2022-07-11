"""
try_exc_else_finally.py

Example of try-except-else-finally block for error handling

"""


def division(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"{numerator} / {denominator} = {result}")
    except ZeroDivisionError:
        print(f"Cannot divide by {denominator}!")
    else:
        # else block only executes if the try block succeeded. Won't execute if exception triggered.
        # else block is optional in most cases--anything that would go in the else statement can
        # just go within the try block.
        print(f"This is the else block executing; denominator was {denominator}.")
    finally:
        # finally executes regardless of whether try succeeded or not.
        print(f"This is the finally block executing.")

num_pairs = [[1,2], [1,0]]

for pair in num_pairs:
    print(f"\nDividing {pair[0]} / {pair[1]}")
    division(pair[0], pair[1])
    