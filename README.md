# usb_barcode_scanner

Support input from a USB scanner in python - such as this one: 

https://www.amazon.co.uk/gp/product/B0736NNZNV/

These scanners are often 'hand-held' but it should work on any USB keyboard emulating scanner.


Usage:
--

The library is very simple to use: just import it and in case, wait for input.

```
import logging

from usb_barcode_scanner.scanner import barcode_reader

if __name__ == '__main__':
    try:
        while True:
            upcnumber = barcode_reader()
            print(upcnumber)
    except KeyboardInterrupt:
        logging.debug('Keyboard interrupt')
    except Exception as err:
        logging.error(err)
```

Alternatively, you also could open the input from the barcode scanner in an extra step:

```
from usb_barcode_scanner.scanner import BarcodeReader

reader = BarcodeReader()

# Prepare something like sending a command to transport something near the scanning interface

upcnumber = reader.read_barcode()

```

Per default, the script opens a scanning device at `/dev/hidraw0`. If the device gets another address, 
you can simply set that adddress as an argument:

```
from usb_barcode_scanner.scanner import barcode_reader

upcnumber = barcode_reader("/dev/hidraw1")

# or

from usb_barcode_scanner.scanner import BarcodeReader

reader = BarcodeReader("/dev/hidraw1")
upcnumber = reader.read_barcode()
```

The project is really quite simple so if there's any difficulty with installing via pip, just copy the 
scanner.py into the root of your project and import from there: 
```
from scanner import barcode_reader
```

Installation
--
PyPI homepage: https://pypi.org/project/usb-barcode-scanner-julz/

GitHub: https://github.com/julzhk/usb_barcode_scanner

install with:
```
pip install usb-barcode-scanner-julz
```

Useful 
--
Generate barcodes : https://graphicore.github.io/librebarcode/
Alterative implementation (using evdev instead of the hidraw stream) : https://gist.github.com/michalfapso/1755e8a35bb83720c2559ce8ffde5f85


Compatibility
--

Tested and working in Linux and Raspberry Pi using Python 3.6+.
It won't work for windows.


License
--
The software is provided "As is", without warranty of any kind, express or implied. 
Please see the MIT license attached. 

Support & Contribution
--
Questions? Drop me a line : montane.gryphon_0m@icloud.com
 or add a support ticket here in github. 
 
 Suggestions and improvements welcome. I'm sorry I'm not very active answering questions, but I'll get to them eventually

