git clone https://github.com/donno2048/restricted-functions
pip3 install PyInstaller==4.5.1
mkdir -p usr/bin
python3 -m PyInstaller --distpath usr/bin refcon.spec
rm -rf restricted-functions build