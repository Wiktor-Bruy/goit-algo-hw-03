from datetime import datetime
import re
import random

# First Task ----------------------------------------------------------
def get_days_from_today(date: str):
    if type(date) != str:
        return "Date must be string."

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        input_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        delta = today - input_date
        return delta.days
    else:
        return f"You input invalid string: {date}. Valid format: 'YYYY-MM-DD'."

# Second Task ---------------------------------------------------------
def get_numbers_ticket(min: int, max: int, quantity: int):
    if type(min) != int or type(max) != int or type(quantity) != int:
        return "Input data must be integer."

    if min < 1 or max > 1000 or min >= max or (max - min) < quantity:
        return []

    my_list = []
    for i in range(int(min), int(max +1)):
        my_list.append(i)

    result = random.sample(my_list, quantity)
    result.sort()
    return result


# Third Task ----------------------------------------------------------
def normalize_phone(phone_number: str):
    new_number = re.sub(r"[^0-9+]", "", phone_number)
    if new_number.startswith("+38") and len(new_number) == 13:
        return new_number
    elif new_number.startswith("380") and len(new_number) == 12:
        return f"+{new_number}"
    elif len(new_number) == 10:
        return f"+38{new_number}"
    else:
        return f"Invalid input number: {new_number}"