#!/usr/bin/python

import sys
import signal

from PyQt4.QtCore import QCoreApplication

from threadedserver import Server

def exit(signal, frame):
    print 'Exiting!'
    sys.exit(0)

def main():
    app = QCoreApplication(sys.argv)
    server = Server()
    
    signal.signal(signal.SIGINT, exit)
    return app.exec_()
    
if __name__ == '__main__':
    main()
