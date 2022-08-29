def read_hour() :
    hour = int(input("Enter hour: "))
    return hour

def read_minute() :
    minute = int(input("Enter minute: "))
    return minute

def read_second() :
    sec = int(input("Enter second: "))
    return sec

def to_seconds(h, m, s) :
    second = h*3600 + m*60 + s
    return second

def time_elapsed(start, finish) :
    hour = (finish - start) // 3600
    minute = ((finish - start) - hour*3600) // 60
    sec = ((finish - start) - hour*3600) % 60
    elapse = "{} hours {} minutes {} seconds.".format(hour,minute,sec)
    return elapse

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))