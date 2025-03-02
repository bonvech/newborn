from supervisor import *


############################################################################
############################################################################
if __name__ == "__main__":
    ##  AE33
    guard = Supervisor("AE33")
    #guard.datadirname = "D:\\AK\\AE33-S09\\data\\table"
    guard.datadirname = "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\DATA\\AE33-S09-01249"
    guard.extention = "csv"
    try:
        if guard.check_lastfile():
            #exit("Errors with last file")
            pass
    except Exception as error:
        guard.write_to_bot(f"{guard.device_name} Supervisor: {error}")


    ##  TCA08
    guard = Supervisor("TCA08")
    guard.datadirname = "D:\\AK\\TCA08\\data\\OnlineResult"
    guard.extention = "csv"
    try:
        if guard.check_lastfile():
            #exit("Errors with last file") 
            pass            
    except Exception as error:
        guard.write_to_bot(f"{guard.device_name} Supervisor: {error}")


    ### Davis
    guard = Supervisor("Davis")
    guard.datadirname = "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\_Instruments\\_Davis\\2 ВНИИЖТ\\VNIIZT"
    guard.extention = "wlk"
    try:
        if guard.check_lastfile():
            #exit("Errors with last file") 
            pass            
    except Exception as error:
        guard.write_to_bot(f"{guard.device_name} Supervisor: {error}")


    ### Optogaz
    guard = Supervisor("Davis")
    guard.datadirname = "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\_Instruments\\_Optogaz\\VNIIZT"
    guard.extention = "log"
    try:
        if guard.check_lastfile():
            #exit("Errors with last file") 
            pass            
    except Exception as error:
        guard.write_to_bot(f"{guard.device_name} Supervisor: {error}")

      
    ## D:\AK\Fidas\data\table    
