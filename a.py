def d(n):
    return n + sum(int(n) for a in str(n))

self_numbers = set(range(1, 10001))

for i in range(1, 10001):
    generated_num = d(i)
    while generated_num <=10000:
        self_numbers.discard(generated_num)
        generated_num = d(generated_num)