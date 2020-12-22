# usb_barcode_scanner

Support input from a hand-held USB scanner in python - such as this one: 

https://www.amazon.co.uk/gp/product/B0736NNZNV/


Usage:
--

The library is very simple to use: just import it and in case, wait for input.

```
from usb_scanner.scanner import barcode_reader
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

The project is really quite simple so if there's any difficulty with installing via pip, just copy the 
scanner.py into the root of your project and import from there: 
```
from scanner import barcode_reader
```

Installation
--
pypi homepage : https://pypi.org/project/usb-barcode-scanner-julz/0.2/
github : https://github.com/julzhk/usb_barcode_scanner

install with:
```
pip install usb-barcode-scanner-julz
```

Useful 
--
Generate barcodes : https://graphicore.github.io/librebarcode/

Compatibility
--

Tested and working in Linux and Raspberry Pi, using Python 3.6, but should work with Python 2.7 too.

License
--
The software is provided "As is", without warranty of any kind, express or implied. 
Please see the MIT license attached. 

Support & Contribution
--
Questions? Drop me a line : usb_barcode_scanner_support_2.20.learningfuture@spamgourmet.com
 or add a support ticket here in github.

Suggestions and improvements welcome.

