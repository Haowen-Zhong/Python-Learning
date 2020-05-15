import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
frames 这是一个生成器
我们要的数据早就在这里了
通过yield 把t和位移扔出去给run
'''
def data_gen():
    for cnt in range(1000):
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/5.)

'''
初始化函数，设置画布大小，删掉所有数据
'''
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=3)
ax.grid()
xdata, ydata = [], []

'''
主要的变换函数！
data传进来给t和y
横坐标时间，纵坐标位移
通过ax.get_xlim()来得到目前横坐标的最大值和最小值
如果新来的横坐标超过了目前的最大值就改变图像的大小
'''

def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
                              repeat=False, init_func=init)
plt.show()