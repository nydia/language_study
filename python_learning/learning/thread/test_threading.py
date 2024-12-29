import threading

def count(i):
    print(i)
    
threads = []     
for i in range(1,10):
    t = threading.Thread(target=count, args=(i))
    threads.append(t)
    t.start()
for t in threads:
    t.join()