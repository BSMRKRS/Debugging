import debug
file_name = "example.py"
#file_name = __name__ ###USE THIS if working with libraries
log_array = []

log_array = debug.log("Initializing Program", debug.get_line(), log_array)

try:
    RPL.servoWrite(0,1500)
    log_array = debug.log("stopping the motors", debug.get_line(), log_array)
except Exception as error:
    log_array = debug.log(error, debug.get_line(), log_array)

log_array = debug.log("Program Completed", debug.get_line(), log_array)
debug.file_write(log_array, file_name)
