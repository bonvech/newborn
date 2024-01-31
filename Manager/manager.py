import os
import fnmatch

sourse_dir = "d:\\AA"
destin_dir = "d:\\DATA"
sep = "\\"

devices = {
	"TCA": {
		"devicename": "",
		"datadir"   : "TCA/data",
		"dirs"      : ['Data',"ExtDeviceData", "Logs","OffLineData",'OnLineResult', 'Setup'],
		},
	"AE33-S09-01249": {
		"devicename": "_AE33-S09-01249",
		"datadir"   : "AE33-S09/data",
		"dirs"      : ['ddat','table'],
		},
	"Web_MEM": {
		"devicename": "_mav_mos_mgu",
		"datadir"   : "Web_MEM/data",
		},
	"PNS": {
		"devicename": "_pns",
		"datadir"   : "PNS/src/data",
		},
	"LVS": {
		"devicename": "_lvs",
		"datadir"   : "LVS/src/data",
		}
}


for device in devices:
    #print(devices[device])
    sourse_path = sourse_dir + sep + devices[device]["datadir"]
    print("\n", sourse_path)
    pattern = "2023_05" + devices[device]["devicename"] + "*"
    
    ## прочитать содержимое папки
    if "dirs" in devices[device]:
        for dirr in devices[device]["dirs"]:
            sourse_path = (sourse_dir + sep + devices[device]["datadir"] 
                           + sep + dirr)
            print(os.listdir(sourse_path))
            for filename in os.listdir(sourse_path):
                if fnmatch.fnmatch(filename, pattern):
                    print(filename)
    else:
        for filename in os.listdir(sourse_path):
            if fnmatch.fnmatch(filename, pattern):
                print(filename)