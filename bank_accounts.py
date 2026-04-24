from decimal import Decimal

def is_account_invalid(account_id, accounts_length):
    return account_id < 0 or account_id >= accounts_length

def is_balance_invalid(balance, amount):
    return balance < amount

def process_account_requests(balances, requests):
    accounts_length = len(balances)
    mutable_balances = list(balances)

    for i, req in enumerate(requests, 1):
        parts = req.split()
        request_type = parts[0]
        primary_account = int(parts[1]) - 1
        amount = Decimal(parts[2]) if len(parts) == 3 else Decimal(parts[3])

        if request_type == "deposit":
            if is_account_invalid(primary_account, accounts_length):
                return [Decimal(-i)]
            mutable_balances[primary_account] += amount

        elif request_type == "withdraw":
            if is_account_invalid(primary_account, accounts_length) or is_balance_invalid(balances[primary_account], amount):
                return [Decimal(-i)]
            mutable_balances[primary_account] -= amount

        elif request_type == "transfer":
            recipient_account = int(parts[2]) - 1
            amount = Decimal(parts[3])
            if (is_account_invalid(primary_account, accounts_length) or
                    is_account_invalid(recipient_account, accounts_length) or
                    is_balance_invalid(balances[primary_account], amount)):
                return [Decimal(-i)]
            mutable_balances[primary_account] -= amount
            mutable_balances[recipient_account] += amount

        else:
            return [Decimal(-i)]

    return mutable_balances

print(process_account_requests([Decimal(100001.0), Decimal(999.23), Decimal(2222.22)],
                               ["deposit 12 20", "transfer 1 2 1000001.322"]))