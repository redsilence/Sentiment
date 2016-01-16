import threading
from getSentiment import *
import re

tsk={}
t={}

for i,line in enumerate( open('Raw_Tweets.txt')):
    print(i)
    phrases=re.split('@|:|/|\.|;|', line)
    for j in range(len(phrases)):
        a = getSentiment(str(phrases[j]))
        print a

'''
for i,line in enumerate( open('Raw_Tweets.txt')):
    print(i)
    phrases=re.split('@|:|/|\.|;|', line)
    print("length=",len(phrases))
    for i in range(len(phrases)):
        def task(i):
            a = getSentiment(str(phrases[i]))
            print a
        tsk[i] = task

    print("Done definition")

    def tsks():
        for i in range(len(phrases)):
            #from IPython import embed
            #embed()
            t[i] = threading.Thread(target=tsk[i], args=[i])

        print("Done tasks definitions")
        for i in range(len(phrases)):
            print(phrases[i])
            t[i].start()
            #print("Started i")

        for i in range(len(phrases)):
            t[i].join()
            #print("Joined i")


    ca = threading.Thread(target=tsks)
    ca.start()
    ca.join()
    break



'''

'''
tt=['abc us hhj','hjkk iid fgh','i am happy','abc us hhj','hjkk iid fgh','i am happy','abc us hhj','hjkk iid fgh','i am happy','what is this','abc us hhj','hjkk iid fgh','i am happy','abc us hhj','hjkk iid fgh','i am happy','abc us hhj','hjkk iid fgh','i am happy','what is this']


for i in range(20):
    def task(i):
        #print i
        a = getSentiment(str(tt[i]))
        print a
    tsk[i] = task
    #print("i=",i)

#print("Done definition")
def tsks():
    for i in range(20):
        t[i] = threading.Thread(target=tsk[i],args=[i])



    for i in range(20):
        t[i].start()
        #print("Started i")

    for i in range(20):
        t[i].join()
        #print("Joined i")


ca = threading.Thread(target=tsks)
ca.start()
ca.join()


exit

'''


'''

def task1():
    print("1")
    a=getSentiment("he is happy"); print a
def task2():
    print("2")
    a=getSentiment("his is 45 years old"); print a
def task3():
    print("3")
    a=getSentiment("he is happy"); print a
def task4():
    print("4")
    a=getSentiment("his is 45 years old"); print a
def task5():
    print("5")
    a=getSentiment("he is happy"); print a
def task6():
    print("6")
    a=getSentiment("his is 45 years old"); print a
def task7():
    print("1")
    a=getSentiment("his is 45 years old"); print a
def task8():
    print("2")
    a=getSentiment("his is 45 years old"); print a
def task9():
    print("3")
    a=getSentiment("his is 45 years old"); print a
def task10():
    print("4")
    a=getSentiment("his is 45 years old"); print a
def task11():
    print("5")
    a=getSentiment("his is 45 years old"); print a
def task12():
    print("6")
    a=getSentiment("his is 45 years old"); print a

def dep1():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t3 = threading.Thread(target=task3)
    t4 = threading.Thread(target=task4)
    t5 = threading.Thread(target=task5)
    t6 = threading.Thread(target=task6)
    t7 = threading.Thread(target=task7)
    t8 = threading.Thread(target=task8)
    t9 = threading.Thread(target=task9)
    t10 = threading.Thread(target=task10)
    t11 = threading.Thread(target=task11)
    t12 = threading.Thread(target=task12)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()



d = threading.Thread(target=dep1)
d.start()
d.join()

'''