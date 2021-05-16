# easy serial
provides convenient work with serial in python

## documentation

### importing
```python
import easy_serial
```

### working with easy serial
#### init
```python
import easy_serial

port = "COM3"

my_serial = easy_serial(port) # port, baudrate, timeout
```

#### sending messages
```python
import easy_serial

port = "COM3"

my_serial = easy_serial(port)
my_serial.write("Hello, world!")
```

#### reading messages
```python
import easy_serial

port = "COM3"

my_serial = easy_serial(port)
print(my_serial.read(10)) # reading 10 bytes from serial port
```

#### getting list of available serial ports
###### first method
```python
import easy_serial

print(easy_serial.com_ports()) # [COM1", "COM3"]
```
###### second method
```python
import easy_serial

easy_serial.print_com_ports()
```

#### advanced
##### encoding
```python
import easy_serial

port = "COM3"

my_serial = easy_serial(port)
my_serial.encoding = "ascii"
```

##### errors handling
```python
import easy_serial

port = "COM3"

my_serial = easy_serial(port)
my_serial.ignore_errors = True # False
```
