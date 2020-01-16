from debug import file_write
#__name__ is the name of the current file, this is used if you import multiple libraries
file_name = name = __name__

log_array = ["Connection Established to server","Server requested size of image","sent server size of image","server requested image","Failed to send image data","lost connection to server"]
file_write(log_array, file_name)
