import ctypes as C
from ctypes.util import find_library
import csv
import numpy as np

class Orderbook(object):

    def __init__(self, price, volume):
        self.price = price
        self.volume = volume

    def getBestBid(self):
        pass

    def getBestAsk(self):
        pass

    def getNextBestBid(self):
        pass

    def getNExtBestAsk(self):
        pass




    def read_limit_order_book(self, lob_file):
        file = open(lob_file, "rU")
        reader = csv.reader(file, delimiter=",")
        row_num = 0
        a = []
        for row in reader:
            a += row
            row_num += 1
        file.close()
        libc = C.CDLL(find_library('c'))
        libc.malloc.restype = C.c_void_p
        # get a pointer to a block of data from malloc
        size = len(a)
        print(size)
        data_pointer = libc.malloc(size * C.sizeof(C.c_double))
        data_pointer = C.cast(data_pointer, C.POINTER(C.c_double))
        array = np.ctypeslib.as_array(data_pointer, shape=(size,))
        array[:] = np.array(a)
        MoneyEnv.pointer_array = data_pointer
        file.drop(['L6-BidPrice', 'L6-BidSize', 'L6-AskPrice', 'L6-AskSize', 'L7-BidPrice', 'L7-BidSize', 'L7-AskPrice',
                   'L7-AskSize', 'L8-BidPrice', 'L8-BidSize', 'L8-AskPrice', 'L8-AskSize', 'L9-BidPrice', 'L9-BidSize',
                   'L9-AskPrice', 'L9-AskSize', 'L10-BidPrice', 'L10-BidSize', 'L10-AskPrice', 'L10-AskSize'], axis=1,
                  inplace=True)

