# https://www.codewars.com/kata/539de388a540db7fec000642/train/python
import dateparser

'''
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".
'''


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # Code here!
    first_date = dateparser.parse(current_date)
    last_date = dateparser.parse(expiration_date)
    
    if (entered_code == correct_code and first_date >= last_date):
        return True
    else:
        return False
