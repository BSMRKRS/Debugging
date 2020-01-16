from datetime import datetime

def file_write(log_array, file_name):
    #gets time of writing the log
    time   = datetime.now()
    month  = time.month
    day    = time.day
    hour   = time.hour
    minute = time.minute
    second = time.second
    time_string = "{}:{} {}|{}.{}".format(month,day,hour,minute,second)

    #stores the log in logs/ directory
    #log name is the name of the file and the time it was written
    file_name = "logs/{} Log {}.txt".format(file_name, time_string)
    log_file = open(file_name, "w")
    #puts each item of the log on a seperate line
    for log in log_array:
        log_file.write(log)
        log_file.write("\n")
    log_file.close()
