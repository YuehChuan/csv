import unittest


class MyTestCase(unittest.TestCase):
    def test_read_csv(self):
        import pandas as pd
        df = pd.read_csv('/home/villain/csv/data/New Session04.csv', usecols=['Fx', 'Fy','Fz'], header=3)
        print(df['Fx'].iloc[1])

    def test_read_F(self):
        import pandas as pd
        df = pd.read_csv('/home/villain/csv/data/New Session04.csv', usecols=['Fx', 'Fy', 'Fz'], header=3)
        index_to_keep = list(range(1, 10))
        print(df.loc[index_to_keep])

    def test_read_LFHD_XYZ(self):
        import pandas as pd
        df = pd.read_csv('/home/villain/csv/data/New Session04.csv', usecols=['Fx', 'Fy', 'Fz'], header=3)
        index_to_keep = list(range(11666, 12249))
        print(df.loc[index_to_keep])



if __name__ == '__main__':
    unittest.main()
