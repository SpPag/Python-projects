def drop_first_last(grades_list):
    first, *middle, last = grades_list
    try:
        avg = sum(middle) / len(middle)
        print(avg)
    except ZeroDivisionError:
        print("Division by zero")
    print(f"""the middle grades are: {middle}""")


drop_first_last([12, 45, 70, 50, 80, 88, 93, 69, 10])
drop_first_last([1, 2])
