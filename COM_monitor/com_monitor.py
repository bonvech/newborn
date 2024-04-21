import serial
from datetime import datetime


class Comport:
    def __init__(self, port):
        ##  COM port properties
        self.portName = port
        self.BPS      = 1200
        self.PARITY   = serial.PARITY_NONE
        self.STOPBITS = serial.STOPBITS_ONE
        self.BYTESIZE = serial.EIGHTBITS
        self.TIMEX    = 1 
        self.ser      = None    


    ##  ----------------------------------------------------------------
    ##  Open COM port
    ##  ----------------------------------------------------------------
    def connect(self):
        #print(f"Connection to {self.portName} ...", end='')

        try:
            self.ser = serial.Serial(
                    port =     self.portName,
                    baudrate = self.BPS,       # 115200,
                    parity =   self.PARITY,    # serial.PARITY_NONE,
                    stopbits = self.STOPBITS,  # serial.STOPBITS_ONE,
                    bytesize = self.BYTESIZE,  # serial.EIGHTBITS
                    #timeout  = self.timeout
                    )
            print("Connected", end = '  ')
        except Exception as err:
            ##  напечатать строку ошибки
            #text = f"ERROR in {self.portName} connect(): {err}" 
            text = f"ERROR in connect(): {err}" 
            print(text)  ## write to log file
            return -1 ## Error in opening
        
        try:
            if (self.ser.isOpen()):
                text = f": {self.portName} port open success"
                print(text)  ## write to log file
                #self.write_bot(text)
        except Exception as err:
            ##  напечатать строку ошибки
            text = f": ERROR: {self.portName} port open failed: {err}" 
            print(text)  ## write to log file
            return -2  ## Error in checking
        
        return 0  ## OK          


    ##  ----------------------------------------------------------------
    ##  Close COM port
    ##  ----------------------------------------------------------------
    def unconnect(self):
        #print(f"Close COM port {self.portName} ... ", end='')
        self.ser.close() # Закройте порт    



for num in range(15):
    port = f"COM{num}"
    device = Comport(port)
    
    print(port, end='  ')
    if device.connect():
        pass
        #print(f"{port} does not respond")
    else:
        #print(f"{port} OK")
        device.unconnect()
        