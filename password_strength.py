import re
import getpass


def is_password_long(password):
    len_good_psw = 8
    return bool(len(password) >= len_good_psw)


def in_password_char_and_num(password):
    return bool(re.search(
        '[a-zA-Z].*\d|\d.*[a-zA-Z]',
        password
    ))


def in_password_special_char(password):
    return bool(re.search('\W+', password))


def are_char_different_register(password):
    return bool(re.search(
        '[A-Z].*[a-z]|[a-z].*[A-Z]',
        password
    ))


def load_data_list(filepath):
    with open(filepath, 'r') as text_file:
        data_list = text_file.read().split('\n')
        return data_list


def is_in_blacklist(password, blacklist):
    return bool(password in blacklist)


def is_in_names_list(password, name_list):
    for popular_name in name_list:
        if popular_name in password.lower():
            return True

    return False


def evaluation_uniqueness(in_blacklist, name_include):
    if not in_blacklist and not name_include:
        return 3
    elif not in_blacklist:
        return 2
    elif not name_include:
        return 1
    else:
        return 0


def are_dates_include(password):
    return not bool(re.search('\d{4,}', password))


def are_duplicate_char(password):
    return not bool(re.search('(\S)\1\1', password))


def get_password_strength(password, rating_uniq):
    len_norm_psw = 5
    if len(password) < len_norm_psw:
        return 1

    testing_list = [
        is_password_long,
        in_password_char_and_num,
        in_password_special_char,
        are_char_different_register,
        are_dates_include,
        are_duplicate_char
    ]

    strength_rating = 1 + rating_uniq
    for test in testing_list:
        if test(password):
            strength_rating += 1

    return strength_rating


if __name__ == '__main__':
    user_password = getpass.getpass(prompt='Введите пароль: ')
    if user_password:
        blacklist_passwords = load_data_list('10-million-password-list-top-100000.txt')
        blacklist_names = load_data_list('names.txt')
        rating_uniqueness = evaluation_uniqueness(
            is_in_blacklist(user_password, blacklist_passwords),
            is_in_names_list(user_password, blacklist_names)
        )
        password_strength = get_password_strength(user_password, rating_uniqueness)

        print('Надежность пароля {}'.format(password_strength))
    else:
        print('Вы не ввели пароль')
