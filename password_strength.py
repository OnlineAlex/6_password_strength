import re


def estimates_password_length(password):
    if len(password) > 7:
        return 1
    return 0


def evaluates_difference_chars(password):
    if re.search('[a-zA-Z]+\d|\d+[a-zA-Z]', password):
        return 1
    else:
        return 0


def evaluates_special_characters(password):
    if re.search('\W+', password):
        return 1
    return 0


def evaluation_register(password):
    if re.search('[a-z]+[A-Z]|[A-Z]+[a-z]', password):
        return 1
    else:
        return 0


def load_file(filepath):
    with open(filepath, 'r') as text_file:
        data_list = text_file.read().split()
        return data_list


def not_popular_passwords(password):
    popular_passwords = load_file('bad_passwords.txt')
    if password in popular_passwords:
        return False
    else:
        return True


def not_name_in_password(password):
    popular_names = load_file('foreign_names.txt')
    for popular_name in popular_names:
        if popular_name in password.lower():
            return False

    return True


def evaluation_uniqueness(password):
    if len(password) < 4:
        # Этот критерий не влияет на короткие пароли
        return 0
    if not_name_in_password(password) and not_popular_passwords(password):
        return 3
    elif not_name_in_password(password):
        return 1
    elif not_popular_passwords(password):
        return 2
    else:
        return 0


def evaluates_simplicity_number(password):
    years_birth = range(1940, 2018)
    for year in years_birth:
        if str(year) in password:
            return 0

    return 1


def evaluates_unique_character(password):
    for char in password:
        if password.find(char*3) != -1:
            return 0

    return 1


def get_password_strength(password):
    testing_list = [
        estimates_password_length,
        evaluates_difference_chars,
        evaluates_special_characters,
        evaluation_register,
        evaluation_uniqueness,
        evaluates_simplicity_number,
        evaluates_unique_character
    ]
    mark = 1

    for test in testing_list:
        mark += test(password)

    return mark


if __name__ == '__main__':
    user_password = input('Введите пароль: ')
    if user_password.find(' ') != -1:
        print('Введите пароль без пробелов')
    elif user_password:
        password_strength = get_password_strength(user_password)
        print('Надежность пароля {}'.format(password_strength))
    else:
        print('Вы не ввели пароль')
