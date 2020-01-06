# usb_barcode_scanner

Support input from a hand-held USB scanner in python - such as this one: 

https://www.amazon.co.uk/gp/product/B0736NNZNV/

Usage:
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