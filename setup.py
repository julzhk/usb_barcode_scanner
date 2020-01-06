import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='usb barcode scanner',
     version='0.1',
     scripts=['scanner.py'] ,
     author="Julian Harley",
     author_email="usb_barcode_scanner_support.20.learningfuture@spamgourmet.com",
     description="Handheld USB Scanner package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/julzhk/usb_barcode_scanner",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: POSIX :: Linux",
     ],
 )
