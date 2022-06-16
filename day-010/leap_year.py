""" leap year
"""
def is_leap(year) -> bool:
    """ Take a year, check if it is a leap year or not

    Args:
        year (int): the year to check

    Returns:
        bool: True if it is a leap year, False otherwise
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month) -> int:
    """Take a year and a month as inputs, work out the number of days in the month

    Args:
        year (_type_): _description_
        month (_type_): _description_

    Returns:
        int: _description_
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 2:
        return month_days[month-1]
    else:
        if is_leap(year):
            return 29
        else:
            return 28


if __name__ == "__main__":
    pass
