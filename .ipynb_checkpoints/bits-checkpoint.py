# Part 1 goes here!
# Kelly Anne Williams (kellyannebyte)
# Homework #01
# 2/1/2023

class DecodeError(Exception):
    pass
class ChunkError(Exception):
    pass

class BitList:
    def __init__(self, binary_string):
        checker = True
        for i in binary_string:
            if i != '0' and i != '1':
                checker = False
                break
        if checker == False:
            raise ValueError("Format is invalid; does not consist of only 0 and 1")
        else:
            self.binary_string = binary_string

    def __eq__(self, other):
        return self.binary_string == other.binary_string

    def __str__(self):
        return self.binary_string

    @staticmethod
    def from_ints(*args):
        binary_string = ""
        checker = True
        for i in args:
            if i != 0 and i != 1:
                checker = False
                break
            else:
                binary_string += str(i)
        if checker == False:
            raise ValueError("Format is invalid; does not consist of only 0 and 1")
        else:
            return BitList(binary_string)

    def arithmetic_shift_left(self):
        self.binary_string = self.binary_string[1:] + '0'

    def arithmetic_shift_right(self):
        self.binary_string = '0' + self.binary_string[:-1]

    def bitwise_and(self, otherBitList):
        new_string = ""
        for i in range(len(self.binary_string)):
            if self.binary_string[i] == '1' and otherBitList.binary_string[i] == '1':
                new_string += '1'
            else:
                new_string += '0'
        return BitList(new_string)
    
    def chunk(self, chunk_length):
        if len(self.binary_string) % chunk_length != 0:
            raise ChunkError("Length of string is not divisible by chunk length")
        else:
            chunk_list = []
            for i in range(0, len(self.binary_string), chunk_length):
                chunk_list.append(BitList(self.binary_string[i:i+chunk_length]))
            return chunk_list
    
    def decode(self, encoding="utf-8"):
        if encoding != 'us-ascii' and encoding != 'utf-8':
            raise ValueError("Encoding must be either 'us-ascii' or 'utf-8'")
        else:
            bin = int(self.binary_string, 2)
            num_bytes = bin.bit_length() + 7 // 8
            arr_bytes = bin.to_bytes(num_bytes, 'big')
            if encoding == 'utf-8':
                ones = 0
                for i in range(len(arr_bytes)):
                    if arr_bytes[i] == 1:
                        ones += 1
                    else:
                        break
                chunk_list = self.chunk(ones)
                while len(chunk_list) != 0 & ones != 0:
                    if len(chunk_list) == ones:
                        break
                    for i in range(ones):
                        if len(chunk_list) == 0:
                            raise DecodeError("Invalid UTF-8 encoding")
                        chunk_list.pop(0)
                    ones = 0
                    for i in range(len(arr_bytes)):
                        if arr_bytes[i] == 1:
                            ones += 1
                        else:
                            break
                    try:
                        return arr_bytes.decode('utf-8').replace('\x00','')
                    except:
                        raise DecodeError("Invalid UTF-8 encoding")
            else:
                if (len(self.binary_string) > 8):
                    store = self.binary_string
                    div = (len(self.binary_string) // 8) + 1
                    arr = []
                    chop = len(self.string) // div
                    for i in range(div):
                        arr.append(store[:chop])
                        store = store[chop:]
                        for i in range(len(arr)):
                            while len(arr[i]) % 8 != 0:
                                arr[i] += '0' + arr[i]
                            new_string = ''
                            for i in range(len(arr)):
                                new_string += arr[i]
                            return_string = ''
                            for i in range(div):
                                bin = int(arr[i], 2)
                                num_bytes = bin.bit_length() + 7 // 8
                                arr_bytes = bin.to_bytes(num_bytes, 'big')
                                return_string += arr_bytes.decode('utf-8').replace('\x00','')
                            return return_string
                    else:
                        odds = [x for x in range(1, 500) if x % 2 == 1]
                        print(odds)
                        return arr_bytes.decode('utf-8').replace('\x00','')


import sys

locate_python = sys.exec_prefix

print(locate_python)


                    

