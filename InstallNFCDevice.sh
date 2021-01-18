# Install all software updates
apt update
apt upgrade
# Install software which requires to install libnfc
apt install pcsc-tools pcscd libpcsclite-dev libpcsclite1 libusb-dev
apt install git binutils make csh g++ sed gawk autoconf automake autotools-dev libglib2.0-dev liblzma-dev libtool 
# Install software to read the card on NFC reader
# Download libnfc and unzip the tar file
git clone https://github.com/jpwidera/libnfc.git
cd libnfc/
#Configure and install libnfc
autoreconf -is
./configure --prefix=/usr --sysconfdir=/etc
make 
make install
ldconfig
# Return to the original path and remove the files necessary for the installation
cd ..
rm -Rf libnfc
# Install the python library with pip
pip3 install --upgrade pip
pip3 install pygame
pip3 install urllib3
pip3 install -U nfcpy