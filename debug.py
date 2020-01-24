from datetime import datetime
import inspect
import os

#pretty self explanitory
def get_line():
    return inspect.currentframe().f_back.f_lineno

#pretty self explanitory
def get_time():
    time   = datetime.now()
    hour   = time.hour
    minute = time.minute
    second = time.second
    current_time = "{}-{}.{}".format(hour,minute,second)
    return current_time

#pretty self explanitory
def make_directory(path):
    #only creates directory if it doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)


#appends to an array and returns it
def log(message, line, log_array):
    line = str(line).zfill(3) #adds 0's infront of string

    #Line | Time : Error Message
    string = "{} | {} : {}".format(line, get_time(), message)
    log_array.append(string)
    return log_array



def file_write(log_array, file_name):
    #gets time of writing the log
    time   = datetime.now()
    month  = time.month
    day    = time.day

    #stores log in cwd/logs/month:day/file name/
    date_directory = "logs/{}:{}".format(month, day)
    module_directory = "{}/{}".format(date_directory, file_name)


    #Creates new directories where needed
    make_directory(date_directory)
    make_directory(module_directory)

    #file name = "Log Hour-Minute.Second"
    file_name = "{}/Log {}.txt".format(module_directory, get_time())
    log_file = open(file_name, "w")
    #puts each item of the log on a seperate line
    for log in log_array:
        log_file.write(log + "\n")
    log_file.close()
