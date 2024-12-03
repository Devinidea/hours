import pandas as pd

def generate_weekdays(year, month):
    all_dates = []
    
    start_date = f'{year}-{month:02d}-01'
    end_date = f'{year}-{month:02d}-{pd.Period(start_date).days_in_month}'  # 获取该月最后一天
    
    # 遍历该月的每一天
    for single_date in pd.date_range(start=start_date, end=end_date):
        # 判断是否是工作日（周一到周五）
        if single_date.weekday() < 5:  # 0=周一, 1=周二, ..., 4=周五
            all_dates.append(single_date)

    return all_dates

print(generate_weekdays(2024, 10))
