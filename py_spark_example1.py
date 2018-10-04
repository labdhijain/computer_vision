#!/usr/bin/python

from pyspark  import  SparkContext
from  operator import  add


with open('no.txt') as f:
        fdata=f.read()
import re
reObj=re.compile('\d+')
mo=reObj.findall(fdata)
n=[]
for i in mo:n.append(int(i))
print(n)

sc=SparkContext("local","App_filter")

#number=[2,6,8,3,55]

transform=sc.parallelize(n)

adding=transform.reduce(add)


print "Adding elements RDD -> %s " % (adding)






