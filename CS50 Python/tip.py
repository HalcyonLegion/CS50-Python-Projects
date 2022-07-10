def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    no_dollar_sign = d.replace("$", "")
    return float(no_dollar_sign)


def percent_to_float(p):
    no_percentage_sign = p.replace ("%", "")
    percentage_conversion = float(no_percentage_sign) / 100
    return float(percentage_conversion)

main()