import logging

from usb_scanner.scanner import barcode_reader

# simple usage  - in python 3
if __name__ == '__main__':
    try:
        while True:
            upcnumber = barcode_reader()
            print(upcnumber)
    except KeyboardInterrupt:
        logging.debug('Keyboard interrupt')
    except Exception as err:
        logging.error(err)
