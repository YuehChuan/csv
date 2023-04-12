import unittest




class MyTestCase(unittest.TestCase):


    def test_plot(self):
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        df = pd.read_csv('/home/villain/csv/data/New Session04.csv', usecols=['Fx', 'Fy', 'Fz'], header=3)
        index_to_keep = list(range(11666, 12249))
        #index_to_keep = list(range(11666, 11670))

        PFrame=df.loc[index_to_keep].astype(float)
        Positions=PFrame.to_numpy().T


        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(Positions[0], Positions[1], Positions[2], marker='x')
        plt.show()

    def test_animation_origin(self):
        ##https://stackoverflow.com/questions/36721861/matplotlib-plot-movements-in-3d
        from matplotlib import pyplot as plt
        import numpy as np
        from matplotlib import animation

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # create the parametric curve
        t = np.arange(0, 2 * np.pi, 2 * np.pi / 100)
        x = np.cos(t)
        y = np.sin(t)
        z = t / (2. * np.pi)

        # create the first plot
        point, = ax.plot([x[0]], [y[0]], [z[0]], 'o')
        line, = ax.plot(x, y, z, label='parametric curve')
        ax.legend()
        ax.set_xlim([-1.5, 1.5])
        ax.set_ylim([-1.5, 1.5])
        ax.set_zlim([-1.5, 1.5])
        # second option - move the point position at every frame
        def update_point(n, x, y, z, point):
            point.set_data(np.array([x[n], y[n]]))
            point.set_3d_properties(z[n], 'z')
            return point
        ani = animation.FuncAnimation(fig, update_point, 99, fargs=(x, y, z, point))
        plt.show()

    def test_animation(self):
        "load data"
        import pandas as pd
        df = pd.read_csv('/home/villain/csv/data/New Session04.csv', usecols=['GYROY3', 'GYROZ3', 'MAGX3'], header=3)
        index_to_keep = list(range(11666, 12249))
        #index_to_keep = list(range(11666, 11680))

        PFrame=df.loc[index_to_keep].astype(float)
        Positions=PFrame.to_numpy().T

        "plot animation"

        from matplotlib import pyplot as plt
        import numpy as np
        from matplotlib import animation

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # create the parametric curve
        data_length=len(index_to_keep)

        frame = np.arange(data_length)
        x = Positions[0]
        y = Positions[1]
        z = Positions[2]

        # create the first plot
        point, = ax.plot([x[0]], [y[0]], [z[0]], 'o')
        line, = ax.plot(x, y, z, label='Glove XYZ Position curve')
        ax.legend()
        ax.autoscale()

        # second option - move the point position at every frame
        def update_point(n, x, y, z, point):
            point.set_data(np.array([x[n], y[n]]))
            point.set_3d_properties(z[n], 'z')
            return point

        ani = animation.FuncAnimation(fig, update_point, data_length, fargs=(x, y, z, point),interval=1)

        plt.show()

    #https://pythonqwt.readthedocs.io/en/latest/

    def test_plot_line(self):
        from matplotlib import pyplot as plt
        import numpy as np


        import pandas as pd
        df = pd.read_csv('/home/villain/csv/data/New Session04.csv', usecols=['ACCY3', 'ACCZ3', 'GYROX3','GYROY3','GYROZ3','MAGX3'], header=3)
        index_to_keep = list(range(11666, 12249))
        #index_to_keep = list(range(11666, 11680))

        PFrame=df.loc[index_to_keep].astype(float)
        Positions=PFrame.to_numpy().T

        "plot animation"

        from matplotlib import pyplot as plt
        import numpy as np
        from matplotlib import animation

        # create the parametric curve
        data_length=len(index_to_keep)

        frame = np.arange(data_length)
        x = Positions[0]
        y = Positions[1]
        z = Positions[2]
        glovex = Positions[3]
        glovey = Positions[4]
        glovez = Positions[5]

        plt.figure()
        plt.subplot(311)
        plt.plot(frame, x, 'bo')

        plt.subplot(312)
        plt.plot(frame, y, 'r--')

        plt.subplot(313)
        plt.plot(frame, z, 'k')

        "glove"
        plt.figure()
        plt.subplot(311)
        plt.plot(frame, glovex, 'bo')

        plt.subplot(312)
        plt.plot(frame, glovey, 'r--')

        plt.subplot(313)
        plt.plot(frame, glovez, 'k')

        plt.show()

    def test_multi_plot(self):
        #https: // hackmd.io / @ yizhewang / Bkd0EMyCm?type = view

        import pandas as pd
        df = pd.read_csv('/home/villain/csv/data/New Session04.csv', usecols=['ACCY3', 'ACCZ3', 'GYROX3','GYROY3','GYROZ3','MAGX3'], header=3)
        index_to_keep = list(range(11666, 12249))

        PFrame=df.loc[index_to_keep].astype(float)
        Positions=PFrame.to_numpy().T

        "plot animation"

        from matplotlib import pyplot as plt
        import numpy as np
        from matplotlib import animation

        # create the parametric curve
        data_length=len(index_to_keep)

        frame = np.arange(data_length)
        bandx = Positions[0]
        bandy = Positions[1]
        bandz = Positions[2]
        glovex = Positions[3]
        glovey = Positions[4]
        glovez = Positions[5]



        plt.figure(figsize=(6, 4.5), dpi=100)  # 設定圖片尺寸
        plt.xlabel('r (m)', fontsize=16)  # 設定坐標軸標籤
        plt.xticks(fontsize=12)  # 設定坐標軸數字格式
        plt.yticks(fontsize=12)
        plt.grid(color='red', linestyle='--', linewidth=1)  # 設定格線顏色、種類、寬度
        plt.ylim(0, 1800)  # 設定y軸繪圖範圍
        # 繪圖並設定線條顏色、寬度、圖例
        line1, = plt.plot(frame, bandx, color='red', linewidth=3, label='bandx')
        line2, = plt.plot(frame, bandy, color='blue', linewidth=3, label='bandy')
        line3, = plt.plot(frame, bandz, color='green', linewidth=3, label='bandz')
        line4, = plt.plot(frame, glovex,'r--', color='red', linewidth=3, label='glovex')
        line5, = plt.plot(frame, glovey,'r--', color='blue', linewidth=3, label='glovey')
        line6, = plt.plot(frame, glovez,'r--', color='green', linewidth=3, label='glovez')
        plt.legend(handles=[line1, line2,line3,line4,line5,line6], loc='upper right')
        plt.savefig('Fe_r_plot.svg')  # 儲存圖片
        plt.savefig('Fe_r_plot.png')
        plt.show()




