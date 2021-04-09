def add_time(start, duration, day=''):
    
    # Initialize
    new_hrs = 0
    new_mins = 0

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
        new_hrs = new_hrs - 24

    if new_hrs <= 12:
        new_period = 'AM'
    else:
        new_period = 'PM'
        new_hrs = new_hrs - 12

    # Format new time
    new_time = str(new_hrs) + ':' + str(new_mins).rjust(2, '0') + ' ' + new_period

    return new_time