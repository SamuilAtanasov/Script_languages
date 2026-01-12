class Compute:
    def __init__(self):
        pass
    def Factorial(self, n):
        if n < 0:
            return "Factorial does not exists for negative numbers."
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    def Sum(self, n):
        if n < 1:
            return "n must be positive full number"
        return n * (n + 1) // 2
    def tableMult(self, n):
        print(f"Table for multiplication of {n}:")
        for i in range(1, 10):
            print(f"{i} x {n} = {n * i}")
    def listDiv(self, n):
        if n == 0:
            return "Zero has endlessly many divisors."
        divisors = []
        for i in range(1, abs(n) + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors
Computation = Compute()
print(Computation.Factorial(5))
print(Computation.Sum(5))
print(Computation.tableMult(5))
print(Computation.listDiv(5))