##  версия копировщика с проверкой существования целевой директории 
import os
from datetime import datetime, date, timedelta


##  check target dir before copying
def safecopy(source_file, target_dir):
    ## check path to copy to
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    res = os.system(f"copy {source_file}  {target_dir}")
    if res:
        print("\r\r", source_file, target_dir)
    


###  config directories
source_dir = "d:\\AK\\"
destin_dir = "d:\\DATA\\"
figure_dir = "d:\\AK\\WWW\\figures\\"


## check path copy to
if not os.path.isdir(destin_dir):
    os.makedirs(destin_dir)


##  create timestamp for datafile names
timestamps = set()
##  add today timestamp
timestamps.add("_".join(str(datetime.now()).split("-"))[:7])
##  add yesterday timestamp
yesterday = datetime.now() - timedelta(days = 1)
timestamps.add("_".join(str(yesterday).split("-"))[:7])


##  ===========================================================================
##  copy figures
##  ===========================================================================
print("\n====  copy figures to WWW/figures")

##  Aethalometers
for ftype in ["day.png", "day.svg", "four_plots.png", "waves_day.png", "waves_day.svg", "waves_week.png", "week.png"]:
    ##  "AE33-S09-01249"
    safecopy(f"{source_dir}AE33-S09\\figures\\ae33_bc_{ftype}", f"{figure_dir}AE33-S09-01249")
    ##  AE43-S01-00125
    safecopy(f"{source_dir}AE43-S01\\figures\\ae33_bc_{ftype}", f"{figure_dir}AE43-S01-00125")

##  Web_MEM
for ftype in ["2_day.png", "2_day.svg", "2_week.png", "all_day.png", "all_day.svg", "all_week.png", "four_plots.png"]:
    safecopy(f"{source_dir}Web_MEM\\figures\\web_msu_{ftype}",  f"{figure_dir}Web_MEM")
    safecopy(f"{source_dir}Web_MEM_Suxarevskaya\\figures\\web_suxarevskaya_{ftype}",  f"{figure_dir}Web_MEM_Suxarevskaya")

##  LVS, PNS
## D:\AK\PNS\src\lvs\figures
for ftype in [".png", ".svg"]:
    safecopy(f"{source_dir}LVS\\src\\lvs\\figures\\lvs_week{ftype}",  f"{figure_dir}LVS")
    safecopy(f"{source_dir}PNS\\src\\lvs\\figures\\pns_week{ftype}",  f"{figure_dir}PNS")



##  ===========================================================================
##  copy datafiles
##  ===========================================================================
print("\n====  copy datafiles to DATA")
for timestamp in timestamps:
    for ftype in ["csv", "xlsx"]:
        ## "AE33-S09-01249"
        safecopy(f"{source_dir}AE33-S09\\data\\table\\{timestamp}_AE33-S09-01249.{ftype}",  f"{destin_dir}AE33-S09-01249 ")
        safecopy(f"{source_dir}AE33-S09\\data\\table\\{timestamp}_AE33-S09-01249.{ftype}",  f"{destin_dir}AE33-S09-01249\\table ")

        ## "AE43-S01-00125"
        safecopy(f"{source_dir}AE43-S01\\data\\table\\{timestamp}_AE43-S01-00125.{ftype}",  f"{destin_dir}AE43-S01-00125 ")
        safecopy(f"{source_dir}AE43-S01\\data\\table\\{timestamp}_AE43-S01-00125.{ftype}",  f"{destin_dir}AE43-S01-00125\\table ")

        ## Web_MEM
        safecopy(f"{source_dir}Web_MEM\\data\\{timestamp}_mav_mos_mgu.{ftype}",  f"{destin_dir}Web_MEM")
        safecopy(f"{source_dir}Web_MEM_Suxarevskaya\\data\\{timestamp}_mav_mos_suxarevskaya.{ftype}",  f"{destin_dir}Web_MEM_Suxarevskaya")


    for ftype in ["data.csv", "log.txt"]:
        ## LVS
        safecopy(f"{source_dir}LVS\\src\\lvs\\data\\{timestamp}_lvs_{ftype}",  f"{destin_dir}LVS")

        ## PNS
        safecopy(f"{source_dir}PNS\\src\\lvs\\data\\{timestamp}_pns_{ftype}",  f"{destin_dir}PNS")


    ## TCA
    timestamp = "-".join(timestamp.split("_"))
    safecopy(f"{source_dir}TCA\\data\\Data\\{timestamp}_Data.csv",    f"{destin_dir}TCA08\\Data")
    safecopy(f"{source_dir}TCA\\data\\Logs\\{timestamp}_Logs.csv",    f"{destin_dir}TCA08\\Logs")
    safecopy(f"{source_dir}TCA\\data\\Setup\\{timestamp}_Setup.csv",  f"{destin_dir}TCA08\\Setup")
    safecopy(f"{source_dir}TCA\\data\\OffLineData\\{timestamp}_OffLineData.csv",     f"{destin_dir}TCA08\\OffLineData")
    safecopy(f"{source_dir}TCA\\data\\OnLineResult\\{timestamp}_OnLineResult.csv",   f"{destin_dir}TCA08\\OnLineResult")
    safecopy(f"{source_dir}TCA\\data\\OnLineResult\\{timestamp}_OnLineResult.xlsx",  f"{destin_dir}TCA08\\OnLineResult")
    safecopy(f"{source_dir}TCA\\data\\OnLineResult\\{timestamp}_OnLineResult.csv",   f"{destin_dir}TCA08")
    safecopy(f"{source_dir}TCA\\data\\OnLineResult\\{timestamp}_OnLineResult.xlsx",  f"{destin_dir}TCA08")
    safecopy(f"{source_dir}TCA\\data\\ExtDeviceData\\{timestamp}_ExtDeviceData.csv", f"{destin_dir}TCA08\\ExtDeviceData")
    safecopy(f"{source_dir}TCA\\data\\ExtDeviceData\\{timestamp}_ExtDeviceData.txt", f"{destin_dir}TCA08\\ExtDeviceData")



##  ===========================================================================
##  copy DATA to Yandex.Disk
##  ===========================================================================
print("\n====  copy DATA to Yandex.Disk")
AKdata_dir = "D:\\DATA"
yandex_dir = '"D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\DATA\\"'

#command = f"xcopy {AKdata_dir} {yandex_dir} /e /y"
command = f"xcopy {AKdata_dir} {yandex_dir} /e /y"
print(command)
os.system(command)
