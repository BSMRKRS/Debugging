from datetime import datetime
import inspect

def get_line():
    return inspect.currentframe().f_back.f_lineno



def get_time():
    time   = datetime.now()
    hour   = time.hour
    minute = time.minute
    second = time.second
    current_time = "{}:{}.{}".format(hour,minute,second)
    return current_time



def log(message, line, file_name, log_array):
    string = "{} | {} on line {} in {}".format(get_time(), message, line, file_name)
    log_array.append(string)
    return log_array



def file_write(log_array, file_name):
    #gets time of writing the log
    time   = datetime.now()
    month  = time.month
    day    = time.day
    time_string = "{}:{} {}".format(month,day,get_time())

    #stores the log in logs/ directory
    #log name is the name of the file and the time it was written
    file_name = "logs/{} Log {}.txt".format(file_name, time_string)
    log_file = open(file_name, "w")
    #puts each item of the log on a seperate line
    for log in log_array:
        log_file.write(log)
        log_file.write("\n")
    log_file.close()
