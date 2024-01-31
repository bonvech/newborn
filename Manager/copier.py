import os
from datetime import datetime, date, timedelta


sourse_dir = "d:\\AA\\"
destin_dir = "d:\\DATA\\"
sep = "\\"

# timestamp = "2024_01"
timestamps = set()
timestamps.add("_".join(str(datetime.now()).split("-"))[:7])
# yesterday date
yesterday = datetime.now() - timedelta(days = 1)
timestamps.add("_".join(str(yesterday).split("-"))[:7])
# print(timestamps)


for timestamp in timestamps:
    ## "AE33-S09-01249"
    os.system(f"copy {sourse_dir}AE33-S09\\data\\table\\{timestamp}_AE33-S09-01249.csv  {destin_dir}AE33-S09-01249 ")
    os.system(f"copy {sourse_dir}AE33-S09\\data\\table\\{timestamp}_AE33-S09-01249.xlsx {destin_dir}AE33-S09-01249 ")
    os.system(f"copy {sourse_dir}AE33-S09\\data\\table\\{timestamp}_AE33-S09-01249.csv  {destin_dir}AE33-S09-01249\\table ")
    os.system(f"copy {sourse_dir}AE33-S09\\data\\table\\{timestamp}_AE33-S09-01249.xlsx {destin_dir}AE33-S09-01249\\table ")

    ## LVS
    os.system(f"copy {sourse_dir}LVS\\src\\data\\{timestamp}_lvs_data.csv  {destin_dir}LVS")
    os.system(f"copy {sourse_dir}LVS\\src\\data\\{timestamp}_lvs_log.txt   {destin_dir}LVS")

    ## PNS
    os.system(f"copy {sourse_dir}PNS\\src\\data\\{timestamp}_pns_data.csv  {destin_dir}PNS")
    os.system(f"copy {sourse_dir}PNS\\src\\data\\{timestamp}_pns_log.txt   {destin_dir}PNS")

    ## Web_MEM
    os.system(f"copy {sourse_dir}Web_MEM\\data\\{timestamp}_mav_mos_mgu.csv  {destin_dir}Web_MEM")
    os.system(f"copy {sourse_dir}Web_MEM\\data\\{timestamp}_mav_mos_mgu.xlsx  {destin_dir}Web_MEM")


    timestamp = "-".join(timestamp.split("_"))

    ## TCA
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
