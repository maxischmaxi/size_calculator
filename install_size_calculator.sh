#!/bin/sh

# check if sudo rights
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "Installing size_calculator..."
pip install pyinstaller
pyinstaller main.py --onefile --name size_calculator
cp dist/size_calculator /usr/local/bin
rm -rf build dist size_calculator.spec
echo "Done!"