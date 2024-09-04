import random
from collections import defaultdict
import json

date_constrain_map = {}
weekday_map = set()
holiday_map = {17}
sun = 1
sat = 7
month_days = 30

for i in range(1, month_days+1):

    if i == sun and i <= month_days:
        holiday_map.add(i)
        sun += 7
    elif i == sat and i <= month_days:
        holiday_map.add(i)
        sat += 7
    elif i not in holiday_map:
        weekday_map.add(i)
    
    no_day = {i, i+1, i+2}
    date_constrain_map[i] = no_day


doctors_num = 22
area_num = 5
big_schedule = [(6,1,4)]
small_schedule = [(5,1,4),(4,2,4)]
big_schedule_doctors_num = month_days * area_num % doctors_num

doctor_list = [f'd{i}' for i in range(1,doctors_num + 1)]
poor_doctors = random.sample(doctor_list, big_schedule_doctors_num)
schedule = {doctor: random.choice(big_schedule) for doctor in poor_doctors}
for doctor in doctor_list:
    if doctor not in schedule:
        schedule.update({doctor: random.choice(small_schedule)})



calendar = {i: {'worker': [], 'rest': []} for i in range(1, month_days + 1)}

def set_schedule(weekday_num: int, holiday_num: int, noday_num: int, doctor: str, calendar: dict, weekday_map: set, holiday_map: set):
    curr_weekday_map = weekday_map.copy()
    curr_holiday_map = holiday_map.copy()
    available_list = list(curr_weekday_map.union(curr_holiday_map))
    
    noday_list = random.sample(available_list, noday_num)
    curr_weekday_map.difference_update(set(noday_list))
    curr_holiday_map.difference_update(set(noday_list))
    for noday in noday_list:
        calendar[noday]['rest'].append(doctor)
   
 
    while weekday_num > 0:
        if len(curr_weekday_map) == 0:
            raise Exception('no available weekday')
        selected_day = random.choice(list(curr_weekday_map))
        if len(calendar[selected_day]['worker']) == area_num+2:
            curr_weekday_map.difference_update({selected_day})
            continue
        else:
            curr_weekday_map.difference_update(date_constrain_map[selected_day])
            curr_holiday_map.difference_update(date_constrain_map[selected_day])
            calendar[selected_day]['worker'].append(doctor)
            weekday_num -= 1
    
    while holiday_num > 0:
        if len(curr_holiday_map) == 0:
            raise Exception('no available holiday')
        selected_day = random.choice(list(curr_holiday_map))
        if len(calendar[selected_day]['worker']) == area_num+2:
            curr_holiday_map.difference_update({selected_day})
            continue
        else:
            curr_weekday_map.difference_update(date_constrain_map[selected_day])
            curr_holiday_map.difference_update(date_constrain_map[selected_day])
            calendar[selected_day]['worker'].append(doctor)
            holiday_num -= 1
    
    
    
for d, way in schedule.items():
    try:
        set_schedule(weekday_num=way[0], 
                        holiday_num=way[1], 
                        noday_num=way[2], 
                        doctor=d, 
                        calendar=calendar, 
                        weekday_map=weekday_map, 
                        holiday_map=holiday_map)
    except Exception as err:
        print(err)



total = 0
overload_worker_days = []
available_worker_days = []
for day, schedule in calendar.items():
    if len(schedule['worker']) > area_num:
        overload_worker_days.append(day)
    else:
        available_worker_days.append(day)
    total += len(schedule['worker']) 
print(total)
print('overload', overload_worker_days)
print('available', available_worker_days)

print(json.dumps(calendar, indent=4))
