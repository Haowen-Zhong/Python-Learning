from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np


# 画圆
def circle(x, y, r, n):
	theta = np.linspace(0, 2 * np.pi, n)
	x = x + r * np.cos(theta)
	y = y + r * np.sin(theta)
	return x, y


def plotfunc():
	glClear(GL_COLOR_BUFFER_BIT)  # 清除之前缓存

	glPointSize(3.0)  # 设置点大小
	glColor3f(1.0, 0.0, 0.0)  # 设置点颜色
	glBegin(GL_POINTS)  # 此次开始，设置此次画的几何图形
	x, y = circle(0, 0, 1, 100)
	for x_, y_ in zip(x, y):
		glVertex2f(x_, y_)
	glEnd()  # 此次结束
glBegin(GL_LINE_STRIP)
glFlush()  # 刷新屏幕


if __name__ == '__main__':
	glutInit(sys.argv)  # 初始化
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # 设置显示模式
	glutInitWindowPosition(100, 100)  # 窗口打开的位置，左上角坐标在屏幕坐标
	glutInitWindowSize(900, 600)  # 窗口大小
	glutCreateWindow(b"Function Plotter")  # 窗口名字，二进制
	glutDisplayFunc(plotfunc)  # 设置当前窗口的显示回调
	glClearColor(1.0, 1.0, 1.0, 1.0)  # 设置背景颜色
	gluOrtho2D(-5.0, 5.0, -5.0, 5.0)  # 设置显示范围
	glutMainLoop()
