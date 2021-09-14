for k in range(1, 1000):
    if 1 <= k < 10:
        digit = k % 10
        if digit ** 1 == k:
            print(f"Narcissistic__Number {k}")
    elif 10 <= k < 100:
        digit1 = k // 10
        digit2 = k % 10
        if digit1 ** 2 + digit2 ** 2 == k:
            print(f"Narcissistic__Number {k}")
    elif 100 <= k < 1000:
        digit3 = k % 10
        digit4 = k % 100 // 10
        digit5 = k // 100
        if digit5 ** 3 + digit4 ** 3 + digit3 ** 3 == k:
            print(f"Narcissistic__Number {k}")
