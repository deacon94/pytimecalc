def add_time(start, duration):

# actual = add_time("3:30 PM", "2:12")
        #expected = "5:42 PM"
    # Determine starting hours and minutes
    print(start.find(':'))
    print(start[0:2])

    start_hrs = int(start[0:start.find(':')])
    start_secs = int(start[start.find(':')-1:])

    print(start_hrs)
    print(start_secs)

    # temp return
    new_time = start

    return new_time