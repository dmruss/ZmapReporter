#!/bin/sh

#setup file
echo "Beginning Installation"
#sudo apt-get update

#install python
echo "installing python3 *************************************************************"
sudo apt-get install python3

#install python dependencies
pip install -r requirements.txt

##also install zmap and zgrab
echo "installing nmap ****************************************************************"
sudo apt-get install nmap

echo "installing zmap ****************************************************************"
sudo apt-get install zmap

echo "installing go ******************************************************************"
cd $HOME || exit
sudo apt-get install -y golang-go
export GOROOT=/usr/lib/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
source .bashrc

pf=$(find $HOME/etc/ -type d -name "zmap")
cd $pf
echo "installing zgrab2 *************************************************************"
sudo go install github.com/zmap/zgrab2@latest
cd || exit
pF=$(find $HOME/etc/ -type d -name "zgrab2@v0.1.7")
echo "**************************** " + $pF + " ********************************"
cd $pF || exit
sudo go get $GOPATH github.com/stretchr/testify
sudo make 
