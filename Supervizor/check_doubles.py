from supervisor import *


############################################################################
############################################################################
datadir = "D:\\AerosolComplex\\YandexDisk\\ИКМО org.msu\\DATA\\"
device = Supervisor("TCA08")

for dirname in os.listdir(datadir):
    ## проверить папка ли это
    if not os.path.isdir(datadir + dirname):
        continue
    print(dirname)
    device.check_doubles(datadir + dirname, "csv")
        
