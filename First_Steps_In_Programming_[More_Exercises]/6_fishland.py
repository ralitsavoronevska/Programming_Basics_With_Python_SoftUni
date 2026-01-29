mackerel_price = float(input())
sprinkle_price = float(input())
bonito_amount = float(input())
scad_amount = float(input())
mussels_amount = int(input())

# Скумрия (mackerel)
# Цаца (sprinkle)
# Паламуд (bonito) – 60% по-скъп от скумрията
# Сафрид (scad) – 80% по-скъп от цацата
# Миди (mussels) – 7.50 лв. за килограм

# Входни данни:
# 6.90
# 4.20
# 1.5
# 2.5
# 1

# Цена на паламуда = 6.90 + 6.90 * 0.60 = 11.04 лв. за килограм
# Сума паламуд = 1.5 * 11.04 = 16.56
# Цена на сафрид = 4.20 + 4.20 * 0.80 =  7.56 лв. за килограм
# Сума сафрид = 2.5 * 7.56 = 18.90
# Сума миди = 1 * 7.50 = 7.50
# Сметка = 16.56 + 18.90 + 7.50 = 42.96

bonito_price = mackerel_price + (mackerel_price * 0.60)
bonito_cost = bonito_price * bonito_amount
scad_price = sprinkle_price + (sprinkle_price * 0.80)
scad_cost = scad_price * scad_amount
mussels_cost = mussels_amount * 7.50
total_cost = bonito_cost + scad_cost + mussels_cost
print(f"{total_cost:.2f}")