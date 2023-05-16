def divisors(n):
    divisors_list = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n // i:  # Avoid duplicate divisors for perfect squares
                divisors_list.append(n // i)
    if len(divisors_list) == 0:
        return f"{n} is prime"
    else:
        return sorted(divisors_list)
