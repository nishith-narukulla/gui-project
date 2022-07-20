import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [0,10,20,30,40]
z = [.1,.2,.3,.4,.5]
plt.title("sample data")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.axis([0,50,0,100])
plt.plot(x,y,color='r',label='plot1')
plt.plot(x,z,color='orange',label='plot2')
plt.legend()
plt.show()