import os
from datetime import datetime, date, timedelta


sourse_dir = "d:\\AK\\"
destin_dir = "d:\\DATA\\"
figure_dir = "d:\\AK\\WWW\\figures\\"
#sep = "\\"

# timestamp = "2024_01"
timestamps = set()
timestamps.add("_".join(str(datetime.now()).split("-"))[:7])
# yesterday date
yesterday = datetime.now() - timedelta(days = 1)
timestamps.add("_".join(str(yesterday).split("-"))[:7])
# print(timestamps)


##  ===========================================================================
##  copy figures
##  ===========================================================================

## "AE33-S09-01249"
for ftype in ["day.png", "day.svg", "four_plots.png", "waves_day.png", "waves_day.svg", "waves_week.png", "week.png"]:
    os.system(f"copy {sourse_dir}AE33-S09\\figures\\ae33_bc_{ftype}  {figure_dir}AE33-S09-01249")

## Web_MEM
for ftype in ["2_day.png", "2_day.svg", "2_week.png", "all_day.png", "all_day.svg", "all_week.png", "four_plots.png"]:
    os.system(f"copy {sourse_dir}Web_MEM\\figures\\web_msu_{ftype}  {figure_dir}Web_MEM")



##  ===========================================================================
##  copy datafiles
##  ===========================================================================
for timestamp in timestamps:
    for ftype in ["csv", "xlsx"]:
        ## "AE33-S09-01249"
        os.system(f"copy {sourse_dir}AE33-S09\\data\\table\\{timestamp}_AE33-S09-01249.{ftype}  {destin_dir}AE33-S09-01249 ")
        os.system(f"copy {sourse_dir}AE33-S09\\data\\table\\{timestamp}_AE33-S09-01249.{ftype}  {destin_dir}AE33-S09-01249\\table ")

        ## Web_MEM
        os.system(f"copy {sourse_dir}Web_MEM\\data\\{timestamp}_mav_mos_mgu.{ftype}  {destin_dir}Web_MEM")

    for ftype in ["data.csv", "log.txt"]:
        ## LVS
        os.system(f"copy {sourse_dir}LVS\\src\\data\\{timestamp}_lvs_{ftype}  {destin_dir}LVS")

        ## PNS
        os.system(f"copy {sourse_dir}PNS\\src\\data\\{timestamp}_pns_{ftype}  {destin_dir}PNS")


    ## TCA
    timestamp = "-".join(timestamp.split("_"))
    os.system(f"copy {sourse_dir}TCA\\data\\Data\\{timestamp}_Data.csv    {destin_dir}TCA08\\Data")
    os.system(f"copy {sourse_dir}TCA\\data\\Logs\\{timestamp}_Logs.csv    {destin_dir}TCA08\\Logs")
    os.system(f"copy {sourse_dir}TCA\\data\\Setup\\{timestamp}_Setup.csv  {destin_dir}TCA08\\Setup")
    os.system(f"copy {sourse_dir}TCA\\data\\OffLineData\\{timestamp}_OffLineData.csv      {destin_dir}TCA08\\OffLineData")
    os.system(f"copy {sourse_dir}TCA\\data\\OnLineResult\\{timestamp}_OnLineResult.csv    {destin_dir}TCA08\\OnLineResult")
    os.system(f"copy {sourse_dir}TCA\\data\\OnLineResult\\{timestamp}_OnLineResult.xlsx   {destin_dir}TCA08\\OnLineResult")
    os.system(f"copy {sourse_dir}TCA\\data\\OnLineResult\\{timestamp}_OnLineResult.csv    {destin_dir}TCA08")
    os.system(f"copy {sourse_dir}TCA\\data\\OnLineResult\\{timestamp}_OnLineResult.xlsx   {destin_dir}TCA08")
    os.system(f"copy {sourse_dir}TCA\\data\\ExtDeviceData\\{timestamp}_ExtDeviceData.csv  {destin_dir}TCA08\\ExtDeviceData")
    os.system(f"copy {sourse_dir}TCA\\data\\ExtDeviceData\\{timestamp}_ExtDeviceData.txt  {destin_dir}TCA08\\ExtDeviceData")


##  ===========================================================================
##  copy DATA to Yandex.Disk
##  ===========================================================================
print("copy DATA to Yandex.Disk")
#AKdata_dir = "D:\\DATA"
AKdata_dir = "D:\\DATA"
yandex_dir = '"D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\DATA\\"'
#yandex_dir = "D:\\AerosolComplex\\YandexDisk\\DATA\\"
command = f"xcopy {AKdata_dir} {yandex_dir} /e /y"
print(command)
os.system(command)
