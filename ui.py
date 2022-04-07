import count
# from count import *

# count.in
def get_user_input():
    value = input("enter action number\n \
    1 for increment\n \
    2 for decrement\n \
    3 for reset\n \
    4 for display\n \
    5 exit\n"
    )
    return int(value)


def main():
    counter = 0
    isWorking = True
    while isWorking:
        user_input = get_user_input()
        if user_input == 1:
            counter = count.increment(counter)
        elif user_input == 2:
            counter = count.decrement(counter)
        elif user_input == 3:
            counter = count.reset()
        elif user_input == 4:
            print("count ==> ", counter)
        elif user_input == 5:
            isWorking = False

    print("user input ==> ", user_input)
    # increment(user_input)

main()