def add_time(start, duration, day=''):
    
    # Initialize
    new_days = 0
    new_hrs = 0
    new_mins = 0
    new_day_of_the_week_index = 0
    days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
    
    # Determine starting period, hours and minutes (convert to 24 hour set)
    start_period = start[len(start)-2:]

    if start_period == 'PM':
        start_hrs = int(start[0:start.find(':')]) + 12
    else:
        start_hrs = int(start[0:start.find(':')])
    
    start_mins = int(start[start.find(':')+1:start.find(':')+3])

    # Determine duration hours and minutes
    duration_hrs = int(duration[0:duration.find(':')])
    duration_mins = int(duration[duration.find(':')+1:duration.find(':')+3])

    # Compute new minutes
    new_mins = start_mins + duration_mins

    if new_mins >= 60:
        new_hrs = round(new_mins / 60)
        new_mins = new_mins % 60

    # Compute new hours, period 
    new_hrs = new_hrs + start_hrs + duration_hrs

    if new_hrs >= 24:
        new_days = round(new_hrs / 24)
        new_hrs = new_hrs % 24

    if new_hrs < 12:
        new_period = ' AM'
    else:
        new_period = ' PM'
        new_hrs = new_hrs - 12

    # Special check for the first hour of the day
    if new_hrs == 0:
        new_hrs = 12    

    # Compute Day of the week (if provided)
    if len(day) > 0:
        new_day_of_the_week = ', ' + days[((days.index(day.upper()) + new_days) % 7)].title()
    else:
        new_day_of_the_week = ''

    # Compute New Days (Timing)
    if new_days == 1:
        new_days = ' (next day)'
    elif new_days > 1:
        new_days = ' (' + str(new_days) + ' days later)'
    else:
        new_days = ''

    # Format new time
    new_time = str(new_hrs) + ':' + str(new_mins).rjust(2, '0') + new_period + new_day_of_the_week + new_days

    return new_time