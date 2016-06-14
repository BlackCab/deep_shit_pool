import threading
import sys
from Queue import Queue

q=Queue()

def find_capital(i, q):
    while True:
        strng = q.get()
        if str(strng)[0].isupper():
            print strng
            f_res.write(strng)
        q.task_done()

if __name__=="__main__":

    f_res = open('D://shit/cap-result.txt', 'w')

    if len(sys.argv)>1:		
        for i in range(int(sys.argv[1])):
            trd = threading.Thread(target=find_capital, args=(i, q))
            trd.setDaemon(True)
            trd.start()

        with open('D://shit/cap-file.txt','r') as f:
            for line in f:
                q.put(line)

        print "Waiting..."
        q.join()
        print 'Done'
        f_res.close()
    else:
        print "Please set number of threads!"
	
