import time
import psutil


def find_usage_30sec():                                            #for 30 seconds
    threading.Timer(30.0, find_usage_30sec).start()
    print "Usage in last 30 seconds"
    print psutil.cpu_percent()                                      # for cpu usage
    print psutil.virtual_memory()                                   # for virtual memory 
    print psutil.disk_usage('/')                                    # for disk usage
 
def find_usage():                                                    #for  5 seconds
    threading.Timer(5.0, find_usage).start()
    print "Current Usage"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')


def find_usage_5min():                                               #for 5 minutes
    threading.Timer(300.0, find_usage_5min).start()
    print "Usage in last 5 minutes"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')
    
def find_usage_1min():
    threading.Timer(60.0, find_usage_1min).start()                    #for 1 minutes
    print "Usage in last 1 minute"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')

find_usage()
find_usage_30sec()
find_usage_1min()
find_usage_5min()

import thread


thread.start_new_thread(find_usage,())
thread.start_new_thread(find_usage_30sec,())
thread.start_new_thread(find_usage_1min,())
thread.start_new_thread(find_usage_5min,())
