#!/usr/bin/python

import sys
import signal

from PySide.QtCore import QCoreApplication

from threadedserver import Server

def exit_handler(signal, frame):
    print 'Exiting!'
    sys.exit(0)

def main():
    app = QCoreApplication(sys.argv)
    server = Server()
    
    signal.signal(signal.SIGINT, exit_handler)
    return app.exec_()
    
if __name__ == '__main__':
    main()
