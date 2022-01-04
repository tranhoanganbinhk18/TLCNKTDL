import socket
import time
import subprocess
import os

def main():
    while True:

        print('test')
        #os.system("stop-all.sh")
        #os.system("start-all.sh")
        os.system("./create_fs.sh")
        print('loadfs')
        os.system("hive -f test.hql")
        print('Success')
        time.sleep(86400)

if __name__ == '__main__':
    main()
