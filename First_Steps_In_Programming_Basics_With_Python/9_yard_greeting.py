# Input:
# От конзолата се прочита само един ред:
# 1. Кв. метри, които ще бъдат озеленени – реално число в интервала [0.00 … 10000.00]

# Output:
# На конзолата се отпечатват два реда:
# "The final price is: {final_service_price} lv."
# "The discount is: {service_discount} lv."

sqr_meters = float(input())
service_price = sqr_meters * 7.61
service_discount = service_price * 0.18
final_service_price = service_price - service_discount
print(f"The final price is: {final_service_price} lv."
      f"The discount is: {service_discount} lv.")