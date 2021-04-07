def duty_free(price, discount, holiday_cost):
    perc = price * (discount / 100.0)
    other = holiday_cost / perc

    return(other)

test = duty_free(12, 50, 1000)
print(test)
