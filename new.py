#!/usr/bin/python
#using spark with python:pyspark
#importing library 

from pyspark  import  SparkContext
from  operator import  add

#puttting x variable in list array 
x = []

#open file and split word then store in list

with open('student.txt','r') as f:
    for line in f:
        for word in line.split():
             
             x.append(word)
print x	

#make sparkcontext variable 
sc=SparkContext("local","App_first")

#transformation RDD
trans1=sc.parallelize(x)

#then action for count all words in list
action1=trans1.count()

#then action for collect word
action2=trans1.collect()

#searching character which is access in word
word_filter=trans1.filter(lambda y:'s' in y)
filtered = word_filter.collect()

#map word how many time 
words_map=trans1.map(lambda y:(y,1))
mapping=words_map.collect()




print "number of Element in RDD-> %i"%(action1)
print "number of Element in RDD-> %s"%(action2)
print "filtered RDD->%s"%(filtered)

#add number
number=[2,4,5,6,77]
trans3=sc.parallelize(number)
adding=trans3.reduce(add)
print "Adding elements RDD -> %i " % (adding)

#cache word true & false
trans1.cache()
caching=trans1.persist().is_cached
print "words got cached in   RDD -> %s " % (caching)

#join data
data1=[("Thanks",2),("welcome",90)]
data2=[("Thanks",9),("welcome",10)]

transform1=sc.parallelize(data1)
transform2=sc.parallelize(data2)

joined=transform1.join(transform2)
final=joined.collect()
print "Joined RDD -> %s " % (final)

print "Mapped  RDD -> %s " % (mapping)

