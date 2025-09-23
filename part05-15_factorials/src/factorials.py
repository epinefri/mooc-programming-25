
def factorials(n: int):
    k = {}
    fact = 1
    for i in range(1, n+1):
        fact *= i
        k[i] = fact

    return k


if __name__ == "__main__":
    k = factorials(2)
    print(k)