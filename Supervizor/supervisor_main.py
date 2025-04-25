from supervisor import *


yandex_disk = "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\_Instruments"
actual_devices = ["GRIMM", "OPS", "AE33"]  #, "Davis", "Optogaz"]
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
        "datadirname": f"{yandex_disk}\\_Davis\\2 ВНИИЖТ\\VNIIZT",
        "extention": "wlk"
        },
    "Optogaz": {
        "datadirname": f"{yandex_disk}\\_Optogaz\\VNIIZT",
        "extention": "log"
        },
    "GRIMM": {
        "datadirname": f"{yandex_disk}\\_Grimm5416\\_Today",
        "extention": "txt"
        },
    "OPS": {
        "datadirname": f"{yandex_disk}\\_OPS\\_Today",
        "extention": "O30"
        }        
}


############################################################################
############################################################################
if __name__ == "__main__":

    for device in actual_devices:
        alarm_time = 100 if device == "AE33" else 60 
        guard = Supervisor(device,
                           datadirname = devices[device]["datadirname"],
                           extention   = devices[device]["extention"],
                           alarm_time  = alarm_time
                           )

        print(f"=====\n{device}")
        try:
            guard.check_lastfile()              
            
        except Exception as error:
            guard.write_to_bot(f"{device} Supervisor: {error}")
