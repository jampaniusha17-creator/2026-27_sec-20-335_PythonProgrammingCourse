def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Calling function with default rate (5%)
p = 10000
t = 2
si1 = simple_interest(p, t)
print("Simple Interest with default rate (5%):", si1)

# Calling function with explicit rate
si2 = simple_interest(p, t, 8)
print("Simple Interest with explicit rate (8%):", si2)