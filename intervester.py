
START_CAPITAL = 100000
MONTHLY_PAYMENT = 250
INTEREST_RATE = 0.12
PAYOUT_RATE = 12
SAVING_PERIOD = 10


    # Works for monthly and daily payout_rate - yearly needs extra method!
def calc_montly_or_daily():
    interest_rate = INTEREST_RATE / float(PAYOUT_RATE)
    print(interest_rate)
    total_capital = START_CAPITAL
    total_payments = 0

    for month in range(SAVING_PERIOD * 12):
        for payment in range(int(PAYOUT_RATE / 12)):
            total_capital += total_capital * interest_rate
        total_capital += MONTHLY_PAYMENT
        total_payments += MONTHLY_PAYMENT
        # print(f'month {month+1}: {total_capital}')

    print(f'\n\nEND: {total_capital}')
    print(f'TOTAL DEPOSITS: {total_payments + START_CAPITAL}')
    print(f'TOTAL INTEREST EARNED: {total_capital - START_CAPITAL - total_payments}')


def calc_yearly():
    total_capital = START_CAPITAL
    total_payments = 0

    for month in range(SAVING_PERIOD * 12):
        if ((month) % 12) == 0:
            total_capital += total_capital * INTEREST_RATE
        total_capital += MONTHLY_PAYMENT
        total_payments += MONTHLY_PAYMENT
    
    print(f'\n\nYEARLY END: {total_capital}')
    print(f'TOTAL DEPOSITS: {total_payments + START_CAPITAL}')
    print(f'TOTAL INTEREST EARNED: {total_capital - START_CAPITAL - total_payments}')


def calculate_interest():
    if PAYOUT_RATE < 12:
        calc_yearly()
    else:
        calc_montly_or_daily()

    
    
    


calculate_interest()