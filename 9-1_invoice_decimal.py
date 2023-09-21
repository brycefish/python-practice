#!/usr/bin/env python3
# Bryce Fish
# Sep 20
# Lab 9

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    shipping_percent = Decimal(".085")
    shipping_cost = subtotal * shipping_percent
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + sales_tax + shipping_cost

    # set locale
    lc.setlocale(lc.LC_ALL, "en_US")
    invoice_total = lc.currency(invoice_total, grouping=True)
    order_total = lc.currency(order_total, grouping=True)

    #f-string alignment
    spec_left = 20
    spec_right = "10,"
    spec_right_currency_string = ">10"
    
    print(f"{'Order total:':{spec_left}}{order_total:{spec_right_currency_string}}")
    print(f"{'Discount amount:':{spec_left}}{discount:{spec_right}}")
    print(f"{'Subtotal:':{spec_left}}{subtotal:{spec_right}}")
    print(f"{'Sales tax:':{spec_left}}{sales_tax:{spec_right}}")
    print(f"{'Shipping cost:':{spec_left}}{shipping_cost:{spec_right}}")
    print(f"{'Invoice total:':{spec_left}}{invoice_total:{spec_right_currency_string}}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
