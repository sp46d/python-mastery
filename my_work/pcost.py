import os


dirname = os.path.dirname(os.path.dirname(__file__))
dat_path = os.path.join(dirname, "Data", "portfolio.dat")

with open(dat_path, "r") as f:
    data = f.read().splitlines()
    total_sum: float = 0.0
    for line in data:
        match line.split():
            case symbol, quantity, price:
                total_sum += int(quantity) * float(price)

print(total_sum)
