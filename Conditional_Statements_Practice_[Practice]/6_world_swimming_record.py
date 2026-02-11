world_swimming_record = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1m = float(input())

total_time = distance_in_meters * time_in_seconds_for_1m
water_resistance_in_seconds = (distance_in_meters // 15) * 12.5

final_time = total_time + water_resistance_in_seconds

if final_time < world_swimming_record:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(final_time - world_swimming_record):.2f} seconds slower.")