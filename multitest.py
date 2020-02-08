import multiprocessing

def p(i):
    print(i)

if __name__ == "__main__":
    for i in range(2000):
        multiprocessing.Process(target=p, args=(i,)).start()