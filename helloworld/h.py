# import urllib2
# url = 'http://aima.cs.berkeley.edu/data/iris.csv'
# u = urllib2.urlopen(url)
# localFile = open('iris.csv','w')
# localFile.write(u.read())
# localFile.close()

from numpy import genfromtxt, zeros
# read the first 4 columns
data = genfromtxt('iris.csv',delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt('iris.csv',delimiter=',',usecols=(4),dtype=str)
print data.shape
print target.shape

print set(target)

# from pylab import plot, show
# plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
# plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
# plot(data[target=='virginica',0],data[target=='virginica',2],'go')
# show()
#
# from pylab import figure, subplot, hist, xlim, show
# xmin = min(data[:,0])
# xmax = max(data[:,0])
# figure()
# subplot(411) # distribution of the setosa class (1st, on the top)
# hist(data[target=='setosa',0],color='b',alpha=.7)
# xlim(xmin,xmax)
# subplot(412) # distribution of the versicolor class (2nd)
# hist(data[target=='versicolor',0],color='r',alpha=.7)
# xlim(xmin,xmax)
# subplot(413) # distribution of the virginica class (3rd)
# hist(data[target=='virginica',0],color='g',alpha=.7)
# xlim(xmin,xmax)
# subplot(414) # global histogram (4th, on the bottom)
# hist(data[:,0],color='y',alpha=.7)
# xlim(xmin,xmax)
# show()


t = zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3

# from sklearn.naive_bayes import GaussianNB
# classifier = GaussianNB()
# classifier.fit(data,t) # training on the iris dataset
#
# from sklearn import cross_validation
# train, test, t_train, t_test = cross_validation.train_test_split(data, t,test_size=0.4, random_state=0)
#
# classifier.fit(train,t_train) # train
# print classifier.score(test,t_test) # test

