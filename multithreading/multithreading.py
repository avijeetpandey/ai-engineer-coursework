# multithreading example
import time
import threading


def download_file(file_id):
    print("Attempting to download file")
    time.sleep(2)
    print("Download complete")


# Simulation
startTime = time.time()

threads = []

for i in range(3):
    thread = threading.Thread(target=download_file, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("Total time taken, ", time.time() - startTime)
