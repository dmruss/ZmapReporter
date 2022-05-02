#! /bin/sh

#setup file
sudo apt-get update

#install python
sudo apt-get install python3

#install python dependencies
pip install -r requirements.txt

##also install zmap and zgrab
sudo apt-get install zmap
sudo apt-get install golang-go
cd || exit
echo "Moved to Base Directory ***************************************************************************************"
mkdir ZmapReporter
echo "Created Zmap Reporter Directory********************************************************************************"
cd ZmapReporter || exit
echo "Entered Zmap Reporter Directory *******************************************************************************"
sudo go get github.com/zmap/zgrab2
echo "Retrieved Zgrab2 Repository ***********************************************************************************"
cd || exit
cd go/pkg/mod/github.com/zmap/zgrab2@v0.1.7 || exit
sudo go get github.com/stretchr/testify
make
