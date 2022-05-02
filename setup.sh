#! /bin/sh

#setup file
sudo apt-get update

#install python
sudo apt-get install python3

#install python dependencies
pip install -r requirements.txt

##also install zmap and zgrab
sudo apt-get install zmap
sudo apt install golang-go
mkdir ZmapReporter
cd ZmapReporter
sudo go get github.com/zmap/zgrab2
cd
cd go/pkg/mod/github.com/zmap/zgrab2@v0.1.7
sudo go get github.com/stretchr/testify
