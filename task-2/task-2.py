text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def sum_profit(text: str):
    total_income = sum([float(num) for num in text.split() if num.replace('.', '', 1).isdigit()])
    print(f"Загальний дохід: {total_income}")

sum_profit(text)