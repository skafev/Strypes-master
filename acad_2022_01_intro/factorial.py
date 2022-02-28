
def fact_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(__name__)

if __name__ == "__main__":
    for n in range(1, 10):
        print(f'{n}! = {fact_iter(n)}')
