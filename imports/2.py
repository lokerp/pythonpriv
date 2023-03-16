from random import randint, choice


def generate_random_int_number(min_num, max_num):
    if min_num < max_num:
        return randint(min_num, max_num)
    else:
        return min_num


def generate_random_letters(str_len=5):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_str = ''
    for _ in range(str_len):
        random_str += choice(letters)
    return random_str


def get_id():
    num = generate_random_int_number(100, 999)
    return generate_random_letters(str_len=2) + str(num) + generate_random_letters()


from random import seed

seed(a=42, version=2)
print(get_id())


def generate_random_int_number(min_num, max_num):
    if min_num < max_num:
        return randint(min_num, max_num)
    else:
        return min_num


def generate_random_letters(str_len=5):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_str = ''
    for _ in range(str_len):
        random_str += choice(letters)
    return random_str


def get_id():
    num = generate_random_int_number(100, 999)
    return generate_random_letters(str_len=2) + str(num) + generate_random_letters()


seed(a=42, version=2)
print(get_id())
