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
        df = pd.read_csv('/home/villain/csv/data/New Session04.csv', usecols=['Fx', 'Fy', 'Fz'], header=3)
        index_to_keep = list(range(11666, 12249))
        #index_to_keep = list(range(11666, 11680))

        PFrame=df.loc[index_to_keep].astype(float)
        Positions=PFrame.to_numpy().T

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
        line, = ax.plot(x, y, z, label='XYZ Position curve')
        ax.legend()
        ax.autoscale()

        # second option - move the point position at every frame
        def update_point(n, x, y, z, point):
            point.set_data(np.array([x[n], y[n]]))
            point.set_3d_properties(z[n], 'z')
            return point

        ani = animation.FuncAnimation(fig, update_point, data_length, fargs=(x, y, z, point),interval=1)

        plt.show()


