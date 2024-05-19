from supervisor import *


############################################################################
############################################################################
if __name__ == "__main__":
    guard = Supervisor("Guard")
    guard.datadirname = "C:\\AK\\AQGuard\\data\\raw"
    guard.extention = "txt"
    try:
        if guard.check_lastfile():
            #exit("Errors with last file") 
            pass            
    except Exception as error:
        guard.write_to_bot(f"{guard.device_name} Supervisor: {error}")
        
        
    guard = Supervisor("AE43")
    guard.datadirname = "C:\\AK\\AE43-S01\\data\\table"
    guard.extention = "csv"
    try:
        if guard.check_lastfile():
            #exit("Errors with last file")
            pass
    except Exception as error:
        guard.write_to_bot(f"{guard.device_name} Supervisor: {error}")
        