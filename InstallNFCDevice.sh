# Install all software updates
apt update
apt upgrade
# Install software which requires to install libnfc
apt install pcsc-tools pcscd libpcsclite-dev libpcsclite1 libusb-dev
# Install software to read the card on NFC reader
# Download libnfc and unzip the tar file
wget http://dl.bintray.com/nfc-tools/sources/libnfc-1.7.1.tar.bz2
tar xjf libnfc-1.7.1.tar.bz2
cd libnfc-1.7.1/
#Configure and install libnfc
./configure
make
make install
ldconfig
# Return to the original path and remove the files necessary for the installation
cd ..
rm libnfc-1.7.1.tar.bz2
rm -Rf libnfc-1.7.1
# Install the python library with pip
pip3 install --upgrade pip
pip3 install pygame
pip3 install urllib3