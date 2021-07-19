import datetime

datetime_format = "%Y-%m-%d %H:%M:%S.%f"

with open("profile.txt", "r+") as data:
    profile = data.readlines()
    last_login_str = profile[-2]
    last_claim_str = profile[-1]
    print(last_claim_str)
    print(last_login_str)
    last_login = datetime.datetime.strptime(last_login_str, datetime_format)
    last_claim = datetime.datetime.strptime(last_claim_str, datetime_format)
    uptime = last_claim - last_login
    if last_claim == "last primogems claim :" or last_login == "last login :":
        pass
    else:
        if uptime > 1:
            balance = profile[2]
            balance = balance.strip()
            balance = balance.replace('balance : ', '')
            balance = balance.replace('"', '')
            balance = int(balance) + 100
            new_balance = f'balance : "{balance}"'
            profile[2] = new_balance
            profile[-1] = last_login
    data.writelines(profile)
    data.close()

