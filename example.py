import debug
#__name__ is the name of the current file, this is used if you import multiple libraries
file_name = __name__
log_array = []

log_array = debug.log("Initializing Program", debug.get_line(), file_name, log_array)

try:
    RPL.servoWrite(0,1500)
    log_array = debug.log("stopping the motors", debug.get_line(), file_name, log_array)
except Exception as error:
    log_array = debug.log(error, debug.get_line(), file_name, log_array)

log_array = debug.log("Program Completed", debug.get_line(), file_name, log_array)
debug.file_write(log_array, file_name)
