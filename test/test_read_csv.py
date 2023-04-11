import unittest


class MyTestCase(unittest.TestCase):
    def test_read_csv(self):
        import csv
        with open('/home/villain/csv/data/New Session04.csv', 'r') as f:  # Read lines separately
            reader = csv.reader(f, delimiter='t')
            for i, row in enumerate(reader):
                print(i, row)

    def test_process_row(self):
        import csv
        with open('/home/villain/csv/data/New Session04.csv', 'r') as f:  # Read lines separately
            reader = csv.reader(f, delimiter='t')
            for i, row in enumerate(reader):
                if i == 3:
                    print(row)

    def test_process_row(self):
        import csv
        with open('/home/villain/csv/data/New Session04.csv', 'r') as f:  # Read lines separately
            reader = csv.reader(f, delimiter='t')
            for i, row in enumerate(reader):
                if i == 5: #first data row
                    print(row)

    def test_process_frame(self):
        import csv
        from itertools import islice

        with open('/home/villain/csv/data/New Session04.csv', 'r') as f:
            for row in islice(csv.reader(f), 5, 25):
                print(row)

    def test_process_frame_float(self):
        import csv
        from itertools import islice
        with open('/home/villain/csv/data/New Session04.csv', 'r') as f:
            for row in islice(csv.reader(f), 5, 25):
                value = [ round ( float(elenment), 3) for elenment in row][2:] # string ->float->小數點3位
                print(value)


    def test_plot_frame(self):
        import csv
        from itertools import islice
        with open('/home/villain/csv/data/New Session04.csv', 'r') as f:
            fx=[]
            fy=[]
            fz=[]
            for row in islice(csv.reader(f), 5, 25):
                value = [ round ( float(elenment), 3) for elenment in row][2:] # string ->float->小數點3位
                fx.append(value[0])
                fy.append(value[1])
                fz.append(value[2])
                print(value)




if __name__ == '__main__':
    unittest.main()
