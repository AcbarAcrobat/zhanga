for i in range(1000):
    if i % 3 == 0 and i % 5 != 0:
        digit_sum = 0
        temp_i = 0
        while temp_i > 10:
            digit_sum += temp_i % 10
            temp_i //=10
        digit_sum += temp_i % 10
        if digit_sum < 10:
            print(i)
