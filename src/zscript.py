#import to zmapReporter
#run zmap/zgrab
import os


def runZmap(a, b):
    os.system("cd")
    os.system("sudo zmap -p " + str(a) + " -N " + str(b) + "| ztee maybeSSH.csv | ~/go/pkg/mod/github.com/zmap/zgrab2@v0.1.7/zgrab2 ssh -o banners.json")
