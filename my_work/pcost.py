import os


dirname = os.path.dirname(os.path.dirname(__file__))
dat_path = os.path.join(dirname, "Data", "portfolio.dat")


total_sum: float = 0.0
with open(dat_path, "r") as f:
    for line in f:
        match line.split():
            case [symbol, quantity, price]:
                total_sum += int(quantity) * float(price)

print(total_sum)
