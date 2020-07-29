import math
daily_per_worker = int(input())
count_workers = int(input())
others_factory_amound = int(input())
daily_amound = daily_per_worker * count_workers
montly_amound = 0
for i in range(1, 31):
    if i % 3 == 0:
        new = daily_amound * 0.75
        montly_amound += math.floor(new)
    else:
        montly_amound += math.floor(daily_amound)
print(f"You have produced {montly_amound} biscuits for the past month.")
if montly_amound > others_factory_amound:
    diff = montly_amound - others_factory_amound
    percent = (diff / others_factory_amound) * 100
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    diff = others_factory_amound - montly_amound
    percent = (diff / others_factory_amound) * 100
    print(f"You produce {percent:.2f} percent less biscuits.")