deposit_amount = float(input())
period = int(input())
interest_rate = float(input())

# total_amount = deposit_amount  + period * ((deposit_amount * (interest_rate / 100) ) / 12)
total_interest = deposit_amount * (interest_rate / 100)
monthly_interest = total_interest / 12
total_amount = deposit_amount + (period * monthly_interest)

print(total_amount)