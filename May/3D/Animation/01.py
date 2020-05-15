import numpy as np
import matplotlib.pyplot as plt
'''
一共有三种Animation。
Animation:This class wraps the creation of an animation using matplotlib.
FuncAnimation:Makes an animation by repeatedly calling a function func.
ArtistAnimation:Animation using a fixed set of Artist objects.
'''
'''
保存方式：Animation.save or Animation.to_html5_video
'''
from matplotlib.animation import  Animation
from matplotlib.animation import  FuncAnimation
from matplotlib.animation import  ArtistAnimation
from mpl_toolkits.mplot3d import Axes3D

# x_data = []
# y_data = []
# z_data = []
#
# fig,ax = plt.subplots()
# ax.set_xlim(0,105)
# ax.set_ylim(0,12)
# line, = ax.plot(0, 0)
#
# def animation_frame(i):
# 	x_data.append(i * 10)
# 	y_data.append(i)
#
# 	line.set_xdata(x_data)
# 	line.set_ydata(y_data)
# 	return line,
#
# animation = FuncAnimation(fig,func = animation_frame, frames =np.arange(0,10,0.1)
# 						  ,interval=10)
# plt.show()
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'rx')
#
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0,10,5),
#                     init_func=init, blit=True)
# plt.show()
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()


def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for i in range(60):
    x += np.pi / 15.
    y += np.pi / 20.
    #每一个元素都是一张图！我们把图顺序播放自然就感觉是动图！
    im = plt.imshow(f(x, y), animated=True,cmap="rainbow")
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)
ani.save("movie.gif",fps=50,dpi=1000)
# writer = animation.FFMpegWriter(
# fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.gif", writer=writer)
#plt.show()