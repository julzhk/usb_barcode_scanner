#!/usr/bin/python

# Inspired by https://www.piddlerintheroot.com/barcode-scanner/
# https://www.raspberrypi.org/forums/viewtopic.php?f=45&t=55100
# from 'brechmos' - thank-you!

CHARMAP_LOWERCASE = {4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k',
                     15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v',
                     26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7',
                     37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';',
                     52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}
CHARMAP_UPPERCASE = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K',
                     15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V',
                     26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&',
                     37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':', 52: '"',
                     53: '~', 54: '<', 55: '>', 56: '?'}
CR_CHAR = 40
SHIFT_CHAR = 2
ERROR_CHARACTER = '?'


class BarcodeReader:
    def __init__(self, device_path="/dev/hidraw0"):
        self.device_path = device_path
        self.f = open(self.device_path, "rb")

    def read_barcode(self):
        barcode_string_output = ''
        # barcode can have a 'shift' character; this switches the character set
        # from the lower to upper case variant for the next character only.
        CHARMAP = CHARMAP_LOWERCASE
        while True:
            # step through returned character codes, ignore zeroes
            for char_code in [element for element in self.f.read(8) if element > 0]:
                if char_code == CR_CHAR:
                    # all barcodes end with a carriage return
                    self.f.close()
                    return barcode_string_output
                if char_code == SHIFT_CHAR:
                    # use uppercase character set next time
                    CHARMAP = CHARMAP_UPPERCASE
                else:
                    # if the charcode isn't recognized, use ?
                    barcode_string_output += CHARMAP.get(char_code, ERROR_CHARACTER)
                    # reset to lowercase character map
                    CHARMAP = CHARMAP_LOWERCASE



def barcode_reader(device_path="/dev/hidraw0"):
    reader = BarcodeReader(device_path)
    return reader.read_barcode()
