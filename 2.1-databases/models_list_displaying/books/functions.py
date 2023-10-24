def get_adjacent_dates(date: str, dates: list) -> tuple:
    previous_date = 0
    next_date = 0

    if date == dates[0]:
        next_date = dates[1]
    elif date == dates[-1]:
        previous_date = dates[-2]
    else:
        date_index = dates.index(date)
        previous_date = dates[date_index-1]
        next_date = dates[date_index+1]

    return (previous_date, next_date)
