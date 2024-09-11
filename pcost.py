from pathlib import Path


def portfolio_cost(filename: Path):
    total_sum: float = 0.0
    with open(filename, "r") as f:
        for line in f:
            try:
                match line.split():
                    case [_, quantity, price]:
                        total_sum += int(quantity) * float(price)
            except ValueError as e:
                print("Couldn't parse:", line)
                print("Reason:", e)
            finally:
                continue

    return total_sum


if __name__ == "__main__":
    print(portfolio_cost(Path("Data/portfolio.dat")))
