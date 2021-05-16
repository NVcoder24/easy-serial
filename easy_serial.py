# libraries
import os

try:
    import serial
    import serial.tools.list_ports
    import sys
    import glob
except ModuleNotFoundError:
    os.system("pip install PySerial")
    os.system("pip install glob")


# errors check
def errors_check(value):
    if value:
        return "ignore"
    else:
        return "replace"


def com_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform!')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def print_com_ports():
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
        print(f"{port}: {desc} [{hwid}]")


# main easy serial class
class EasySerial:
    # init
    def __init__(self, port, speed=9600, timeout=0.05):
        # serial
        self.serial = serial.Serial(port, speed, timeout=timeout)

        # default settings
        self.encoding = "ascii"
        self.ignore_errors = True

    # write
    def write(self, value=""):
        self.serial.write(value.encode())

    # read
    def read(self, read_bytes=0):
        output = self.serial.read(read_bytes)

        decoded = output.decode(errors=errors_check(self.ignore_errors), encoding=self.encoding)
        result = decoded.split("\n")[0].split("\r")[0]

        return result

    # get name
    def name(self):
        return self.serial.name