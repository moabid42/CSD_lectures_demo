# Chall is taking from somewhere
def filter(s):
    BLACKLIST = ["exec","input","eval"]
    for i in BLACKLIST:
        if i in s:
            print(f'Ban detected !')
            exit(0)

input_data = input("> ")
filter(input_data)
if len(input_data) > 13:
    print("Not so easy !")
    exit(0)
print('Answer: {}'.format(eval(input_data)))
