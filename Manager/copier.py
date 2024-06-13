##  версия копировщика с проверкой существования целевой директории 
import os
from datetime import datetime, date, timedelta


##  check target dir before copying
def safecopy(source_file, target_dir):
    ## check path to copy to
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    res = os.system(f"xcopy {source_file}  {target_dir} /d /y")
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
    for station in ["MGU", "Suxarevskaya", "Ostankino"]:
        safecopy(f"{source_dir}Web_MEM\\Web_MEM_{station}\\figures\\web_{station.lower()}_{ftype}",  
                 f"{figure_dir}Web_MEM_{station}")
    #safecopy(f"{source_dir}Web_MEM\\Web_MEM_Suxarevskaya\\figures\\web_suxarevskaya_{ftype}", f"{figure_dir}Web_MEM_Suxarevskaya")
    
##  LVS, PNS
##  D:\AK\PNS\src\lvs\figures
for ftype in [".png", ".svg"]:
    safecopy(f"{source_dir}LVS\\src\\lvs\\figures\\lvs_week{ftype}",  f"{figure_dir}LVS")
    safecopy(f"{source_dir}PNS\\src\\lvs\\figures\\pns_week{ftype}",  f"{figure_dir}PNS")

##  TCA08
##  D:\AK\TCA08\figures
for ftype in [".png", ".svg"]:
    for period in ["day", "week"]:
        safecopy(f"{source_dir}TCA08\\figures\\tca_extdevicedata_{period}{ftype}",  f"{figure_dir}TCA08")
        safecopy(f"{source_dir}TCA08\\figures\\tca_onlineresult_{period}{ftype}",  f"{figure_dir}TCA08")



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
        for station in ["MGU", "Suxarevskaya", "Ostankino"]:
            safecopy(f"{source_dir}Web_MEM\\Web_MEM_{station}\\data\\{timestamp}_mem_{station.lower()}.{ftype}",  
                     f"{destin_dir}Web_MEM_{station}")
        #safecopy(f"{source_dir}Web_MEM_Suxarevskaya\\data\\{timestamp}_mav_mos_suxarevskaya.{ftype}",  f"{destin_dir}Web_MEM_Suxarevskaya")


    for ftype in ["data.csv", "log.txt"]:
        ## LVS
        safecopy(f"{source_dir}LVS\\src\\lvs\\data\\{timestamp}_lvs_{ftype}",  f"{destin_dir}LVS")

        ## PNS
        safecopy(f"{source_dir}PNS\\src\\lvs\\data\\{timestamp}_pns_{ftype}",  f"{destin_dir}PNS")


    ## AQ Guard Smart
    safecopy(f"{source_dir}AQGuard\\data\\raw\\{timestamp}_AQ_raw.txt",  f"{destin_dir}AQGuard")
    

    ## TCA
    timestamp = "-".join(timestamp.split("_"))
    tca_dir = f"{source_dir}TCA08"
    safecopy(f"{tca_dir}\\data\\Data\\{timestamp}_Data.csv",    f"{destin_dir}TCA08\\Data")
    safecopy(f"{tca_dir}\\data\\Logs\\{timestamp}_Logs.csv",    f"{destin_dir}TCA08\\Logs")
    safecopy(f"{tca_dir}\\data\\Setup\\{timestamp}_Setup.csv",  f"{destin_dir}TCA08\\Setup")
    safecopy(f"{tca_dir}\\data\\OffLineData\\{timestamp}_OffLineData.csv",     f"{destin_dir}TCA08\\OffLineData")
    safecopy(f"{tca_dir}\\data\\OnLineResult\\{timestamp}_OnLineResult.csv",   f"{destin_dir}TCA08\\OnLineResult")
    safecopy(f"{tca_dir}\\data\\OnLineResult\\{timestamp}_OnLineResult.xlsx",  f"{destin_dir}TCA08\\OnLineResult")
    safecopy(f"{tca_dir}\\data\\OnLineResult\\{timestamp}_OnLineResult.csv",   f"{destin_dir}TCA08")
    safecopy(f"{tca_dir}\\data\\OnLineResult\\{timestamp}_OnLineResult.xlsx",  f"{destin_dir}TCA08")
    safecopy(f"{tca_dir}\\data\\ExtDeviceData\\{timestamp}_ExtDeviceData.csv", f"{destin_dir}TCA08\\ExtDeviceData")
    safecopy(f"{tca_dir}\\data\\ExtDeviceData\\{timestamp}_ExtDeviceData.txt", f"{destin_dir}TCA08\\ExtDeviceData")



##  ===========================================================================
##  copy DATA to Yandex.Disk
##  ===========================================================================
print("\n====  copy DATA to Yandex.Disk")
AKdata_dir = "D:\\DATA"
yandex_dir = '"D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\DATA\\"'

##  Обновить старые файлы и добавить новые
##  /C - Продолжение копирования вне зависимости от наличия ошибок.
##  /E - Копирование каталогов с подкаталогами, включая пустые. Эквивалентен сочетанию ключей /S /E. Совместим с ключом /T.
##  /Y - Подавление запроса подтверждения на перезапись существующего целевого файла.
##  /D:m-d-y - Копирование файлов, измененных не ранее указанной даты. Если дата не указана, заменяются только конечные файлы, более старые, чем исходные.
command = f"xcopy {AKdata_dir}\\* {yandex_dir} /E /Y /D"
print(command)
os.system(command)

##  Обновить старые файлы
##  /R - Разрешение замены файлов, предназначенных только для чтения (среди прочих).
##  /S - Замена файлов во всех подкаталогах конечного каталога. Этот ключ несовместим с ключом /A.
##  /U - Замена только файлов, более старых, чем исходные. Этот ключ несовместим с ключом /A.
#command = f"replace {AKdata_dir}\\* {yandex_dir} /R /S /U "
#print(command)
#os.system(command)

##  Добавление новых файлов
##  REPLACE
##  /A - Добавление новых файлов в конечный каталог. Этот ключ несовместим с ключами /S и /U.
#command = f"replace {AKdata_dir}\\* {yandex_dir} /A"
#print(command)
#os.system(command)


##  ===========================================================================
##  copy AK to Yandex.Disk
##  ===========================================================================
print("\n====  copy AK to Yandex.Disk")
AKdata_dir =  "D:\\AK"
yandex_dir = '"D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\DATA\\AK\\"'

command = f"xcopy {AKdata_dir}\\* {yandex_dir} /E /Y /D"
print(command)
os.system(command)
