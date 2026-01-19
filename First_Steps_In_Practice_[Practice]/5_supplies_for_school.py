amount_of_packet_of_pens = int(input())
amount_of_packet_of_markers = int(input())
liters_of_detergent = int(input())
percent_of_discount = int(input())

price_of_packet_of_pens = 5.80
price_of_packet_of_markers = 7.20
price_of_detergent_per_liter = 1.20

total_price_of_pens = amount_of_packet_of_pens * price_of_packet_of_pens
total_price_of_markers = amount_of_packet_of_markers * price_of_packet_of_markers
total_price_of_detergent = liters_of_detergent * price_of_detergent_per_liter
total_price_without_discount = total_price_of_pens + total_price_of_markers + total_price_of_detergent
total_price = total_price_without_discount - (total_price_without_discount * (percent_of_discount / 100))

print(total_price)