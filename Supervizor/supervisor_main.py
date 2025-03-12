from supervisor import *


actual_devices = ["AE33", "Davis", "Optogaz", "GRIMM", "OPS"]
devices = {
    "AE33": { ##  AE33
        "datadirname": "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\DATA\\AE33-S09-01249",
        "extention": "csv"
        },
    "TCA08": {
        "datadirname": "D:\\AK\\TCA08\\data\\OnlineResult",
        "extention": "csv"
        },
    "Davis": {
        "datadirname": "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\_Instruments\\_Davis\\2 ВНИИЖТ\\VNIIZT",
        "extention": "wlk"
        },
    "Optogaz": {
        "datadirname": "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\_Instruments\\_Optogaz\\VNIIZT",
        "extention": "log"
        },
    "GRIMM": {
        "datadirname": "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\_Instruments\\_Grimm5416\\_Today",
        "extention": "txt"
        },
    "OPS": {
        "datadirname": "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\_Instruments\\_OPS\\_Today",
        "extention": "O30"
        }        
}


############################################################################
############################################################################
if __name__ == "__main__":
    for device in actual_devices:
        guard = Supervisor(device,
                           datadirname = devices[device]["datadirname"],
                           extention   = devices[device]["extention"]
                           )

        print(f"=====\n{device}")
        try:
            guard.check_lastfile():                
            
        except Exception as error:
            guard.write_to_bot(f"{device} Supervisor: {error}")
