def return_10():
    return 10


def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def multiply(number_1, number_2):
    return number_1 * number_2


def divide(number_1, number_2):
    return number_1 / number_2


def length_of_string(string):
    return len(string)


def join_string(string1, string2):
    return string1 + string2


def add_string_as_number(num_1, num_2):
    return int(num_1) + int(num_2)


def number_to_full_month_name(index):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "July",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]

    return months[index - 1]


def number_to_full_month_name(index):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "July",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]
    return months[index - 1]


def number_to_short_month_name(index):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "July",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]
    return months[index - 1]


def volume_of_cube(side):
    return side**3


def reverse_string(string):
    return string[::-1]


def fahrenheit_to_celsius(fah):
    return (fah - 32) * (5 / 9)
