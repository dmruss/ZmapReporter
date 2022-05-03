#!/bin/sh

#setup file
sudo apt-get update

#install python
notInst=" no "
path=which python3
if [[ $path == *"$notInst"* ]]
  sudo apt-get install python3

#install python dependencies
pip install -r requirements.txt

##also install zmap and zgrab
path = which nmap
if [[ $path == *"$notInst"* ]]
  sudo apt-get install nmap
path = which zmap
if [[ $path == *"$notInst"* ]]
  sudo apt-get install zmap
path = which go
if [[ $path == *"$notInst"* ]]
  sudo apt-get install golang-go
cd || exit
mkdir ZmapReporter
cd ZmapReporter || exit
#path = which zgrab2
if [[ $path == *"$notInst"* ]]
  sudo go get github.com/zmap/zgrab2
cd || exit
path = find ~ -type d -name "zgrab2@v0.1.7"
cd $path || exit
sudo go get github.com/stretchr/testify
make
