days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

weekday_dict = {i+1: day for i, day in enumerate(days)}

reverrs_weekday_dict = {day: i+1 for i, day in enumerate(days)}

print("Day dict:", weekday_dict)
print("Revers weekday dict:", reverrs_weekday_dict)