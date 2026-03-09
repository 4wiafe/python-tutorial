def apply_discount(price, discount):
    if type(price) != int and type(price) != float:
        return 'The price should be a number'

    if type(discount) != int and type(discount) != float:
        return 'The discount should be a number'

    if price <= 0:
        return 'The price should be greater than 0'

    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'

    cal_discount = (discount / 100) * price
    final_price = price - cal_discount

    return final_price


print(apply_discount(74.5, 20.0))
