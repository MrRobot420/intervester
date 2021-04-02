
START_CAPITAL = 5000
MONTHLY_PAYMENT = 100
INTEREST_RATE = 0.05
PAYOUT_RATE = 12
SAVING_PERIOD = 10


def ask_capital():
    value = input(f'Your Start Capital (ENTER for: {START_CAPITAL} €): ')
    if (value == ''):
        return START_CAPITAL
    return float(value)

def ask_payment():
    value = input(f'Your monthly payment (ENTER for: {MONTHLY_PAYMENT} €): ')
    if (value == ''):
        return MONTHLY_PAYMENT
    return float(value)

def ask_interest():
    value = input(f'The interest rate (p.a.) (ENTER for: {INTEREST_RATE * 100} %): ')
    if (value == ''):
        return INTEREST_RATE
    return float(value) / 100.0

def ask_payout_rate():
    value = input(f'The payout rate: (ENTER for {PAYOUT_RATE} - yearly = 1, monthly = 12, daily = 365): ')
    if (value == ''):
        return PAYOUT_RATE
    return int(value)

def ask_period():
    value = input(f'The saving period: (ENTER for {SAVING_PERIOD} years): ')
    if (value == ''):
        return SAVING_PERIOD
    return int(value)

def ask_values():
    global START_CAPITAL
    global MONTHLY_PAYMENT
    global INTEREST_RATE
    global PAYOUT_RATE
    global SAVING_PERIOD

    START_CAPITAL = ask_capital()
    MONTHLY_PAYMENT = ask_payment()
    INTEREST_RATE = ask_interest()
    PAYOUT_RATE = ask_payout_rate()
    SAVING_PERIOD = ask_period()

# Works for monthly and daily payout_rate - yearly needs extra method!
def calc_montly_or_daily():
    interest_rate = INTEREST_RATE / float(PAYOUT_RATE)
    total_capital = START_CAPITAL
    total_payments = 0

    for month in range(SAVING_PERIOD * 12):
        for payment in range(int(PAYOUT_RATE / 12)):
            total_capital += total_capital * interest_rate
        total_capital += MONTHLY_PAYMENT
        total_payments += MONTHLY_PAYMENT
        # print(f'month {month+1}: {total_capital}')

    print(f'\n\nEND: {"{:.2f}".format(total_capital)} €')
    print(f'TOTAL DEPOSITS: {"{:.2f}".format(total_payments + START_CAPITAL)} €')
    print(f'TOTAL INTEREST EARNED: {"{:.2f}".format(total_capital - START_CAPITAL - total_payments)} €')


def calc_yearly():
    total_capital = START_CAPITAL
    total_payments = 0

    for month in range(SAVING_PERIOD * 12):
        if (month % 12) == 0:
            total_capital += total_capital * INTEREST_RATE
        total_capital += MONTHLY_PAYMENT
        total_payments += MONTHLY_PAYMENT
    
    print(f'\n\nYEARLY END: {total_capital} €')
    print(f'TOTAL DEPOSITS: {total_payments + START_CAPITAL} €')
    print(f'TOTAL INTEREST EARNED: {total_capital - START_CAPITAL - total_payments} €')


def calculate_interest():
    ask_values()

    if PAYOUT_RATE < 12:
        calc_yearly()
    else:
        calc_montly_or_daily()

    
    
    


calculate_interest()