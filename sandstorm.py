import numpy as np
import matplotlib.pyplot as plt
from vector import Vector

def generate_sand(N=256):
    cells = np.random.randint(0,256,(N,N))
    return cells

def draw_rec(cells, startPos, length):
    for i in range(startPos.x, startPos.x+length.x):
        for j in range(startPos.y, startPos.y+length.y):
            cells[j][i] = 255
    return cells

def plot_cells(cells):
    #plt.axis("off") # 目盛りを非表示
    #plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.imshow(cells, cmap=plt.cm.gray_r, vmin=0, vmax=255)
    plt.show()

def main():
    cells = generate_sand()
    startPos = Vector(20,60) # 長方形の左上の座標
    length = Vector(30,100) # 長方形の長さ
    cells = draw_rec(cells, startPos, length)
    startPos = Vector(55,135)
    length = Vector(100,30)
    cells = draw_rec(cells, startPos, length)
    plot_cells(cells)

if __name__ == "__main__":
    main()
