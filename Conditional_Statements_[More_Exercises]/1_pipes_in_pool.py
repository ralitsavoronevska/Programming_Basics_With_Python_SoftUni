# Input:
# Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]

pool_volume_in_liters = int(input())
liters_of_water_per_hour_1st_pipe = int(input())
liters_of_water_per_hour_2nd_pipe = int(input())
absence_of_worker_in_hours = float(input())

pool_occupancy_1st_pipe = liters_of_water_per_hour_1st_pipe * absence_of_worker_in_hours
pool_occupancy_2nd_pipe = liters_of_water_per_hour_2nd_pipe * absence_of_worker_in_hours
pool_occupancy = pool_occupancy_1st_pipe + pool_occupancy_2nd_pipe

if pool_occupancy > pool_volume_in_liters:
    overflow_amount = pool_occupancy - pool_volume_in_liters
    print(f"For {absence_of_worker_in_hours:.2f} hours the pool overflows with {overflow_amount:.2f} liters.")
else:
    pool_occupancy_in_percentages = (pool_occupancy / pool_volume_in_liters) * 100
    pool_occupancy_1st_pipe_in_percentages = (pool_occupancy_1st_pipe / pool_occupancy) * 100
    pool_occupancy_2nd_pipe_in_percentages = (pool_occupancy_2nd_pipe / pool_occupancy) * 100
    print(f"The pool is {pool_occupancy_in_percentages:.2f}% full. Pipe 1: {pool_occupancy_1st_pipe_in_percentages:.2f}%. Pipe 2: {pool_occupancy_2nd_pipe_in_percentages:.2f}%.")