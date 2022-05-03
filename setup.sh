#!/bin/sh

#setup file
sudo apt-get update

#install python
neg = " no "
path = which python3
if neg in path:
  sudo apt-get install python3

#install python dependencies
pip install -r requirements.txt

##also install zmap and zgrab
path = which nmap
if neg in path:
  sudo apt-get install nmap
path = which zmap
if neg in path:
  sudo apt-get install zmap
path = which go
if neg in path:
  sudo apt-get install golang-go
cd || exit
mkdir ZmapReporter
cd ZmapReporter || exit
path = which zgrab2
if neg in path:
  sudo go get github.com/zmap/zgrab2
cd || exit
path = find ~ -type d -name "zgrab2@v0.1.7"
cd path || exit
sudo go get github.com/stretchr/testify
make
