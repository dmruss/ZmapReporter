#!/bin/bash

#setup file
echo "Beginning Installation"
sudo apt-get update
sudo apt install python3-pip

#install python
echo "installing python3*****************"
sudo apt-get install python3

#install python dependencies
pip install -r requirements.txt

#also install zmap and zgrab
echo "installing nmap*********************"
sudo apt-get install nmap

echo "installing zmap**********************"
sudo apt-get install zmap

echo "installing go *************************"
pip install ip2geotools
sudo apt-get install -y golang-go && export GO111MODULE="auto"

echo "installing zgrab2 *******************"
sudo apt install golang-go make zmap -y && go get github.com/zmap/zgrab2 && export GOPATH=$(go env GOPATH)
cd $GOPATH/src/github.com/zmap/zgrab2 && make
echo "installation complete *******************"
