# Part 1 goes here!
# Kelly Anne Williams (kellyannebyte)
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
        self.binary_string = self.binary_string[0] + self.binary_string[:-1]

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
        if encoding != 'utf-8' and encoding != 'us-ascii':
            raise ValueError('Encoding must be us-ascii or utf-8')
        else:
            binary = int(self.binary_string, 2)
            num_bytes = binary.bit_length() + 7 // 8
            arr_bytes = binary.to_bytes(num_bytes, "big")
            if encoding == 'utf-8':
                count = 0
                for i in range(8):
                    if self.binary_string[i] == '1':
                        count += 1
                    else:
                        break
                chunk_list = self.chunk(8)
                while len(chunk_list) != 0 & count != 0:
                    if len(chunk_list) == count:
                        break
                    for i in range(count):
                        if len(chunk_list) == 0:
                            raise DecodeError('Invalid leading byte')
                        chunk_list.pop(0)
                    count = 0
                    for i in range(8):
                        if chunk_list[0][i] == 1:
                            count += 1
                        else:
                            break
                try:
                    return arr_bytes.decode('utf-8').replace('\x00','')
                except UnicodeDecodeError:
                    raise DecodeError('Invalid leading byte')
            else:
                if (len(self.binary_string) > 8):
                    store = self.binary_string
                    div = (len(self.binary_string) // 8) + 1
                    string_array = []
                    chop_it = len(self.binary_string) // div
                    for i in range(div):
                        string_array.append(store[:chop_it])
                        store = store[chop_it:]
                    for i in range(len(string_array)):
                        while len(string_array[i]) % 8 != 0:
                            string_array[i] = '0' + string_array[i]
                    added = ''
                    for i in range(len(string_array)):
                        added += string_array[i]
                    output = ''
                    for i in range(div):
                        binary = int(string_array[i], 2)
                        num_bytes = binary.bit_length() + 7 // 8
                        arr_bytes = binary.to_bytes(num_bytes, "big")
                        output += arr_bytes.decode('us-ascii').replace('\x00','')
                    return output
                else: 
                    nums_by_odd = [x for x in range(1, 500) if x % 2 == 1]
                    print(nums_by_odd)

                    return arr_bytes.decode('us-ascii').replace('\x00','')


#import sys

#locate_python = sys.exec_prefix

#print(locate_python)


                    

