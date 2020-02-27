def change(n):
    t = [100, 50, 20, 5, 1]
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n


if __name__ == "__main__":
    print(change(376))
