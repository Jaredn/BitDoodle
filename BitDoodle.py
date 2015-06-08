
"""
Bit Doodle!

Description:
    Bit Doodle is a class designed for working with variable length bit fields.  While the class can technically be
    used for anything, it is catered towards IPv4 and IPv6 addresses.  The main methods are join and disjoin, which
    will take a list of variable length fields and a list of values and join them together to a single value, or
    disjoin which will take a single value and a list of bit lengths, and break the original value into its multiple
    parts.

join:
    Description:
        Given a list of bit lengths, and a list of values, join the values into a single number.  If the bit lengths
        are exactly 32 or 128 bits, an ipaddress object is returned instead.

    Inputs:
        format_ : list of integers, each representing a bit length
        values : list of integers, each representing a value
            NOTE: format_ and values must be the same length, or an exception will be thrown.
            NOTE: Each value must be between 0 and the max value of its corresponding bit-length or an exception
                  will be thrown.

    Outputs:      todo: allow user to specify output type
        A single value that can be of the following types:
        Int
        Long
        ipaddress object (of bit lengths were exactly 32 or 128)

disjoin:
    Description:
        Given a single value and a list of bit lengths, disjoin the value into its bit length values.

    Inputs:
        format_ : list of integers, each representing a bit length
        value : A single value to be broken down into multiple pieces defined by format_

    Outputs:
        An array of integers or longs
"""

import ipaddress


class BitDoodle:
    def __init__(self, format_):
        self.format_ = format_
        self.total_bit_length = sum(self.format_)

    def join(self, values):
        # validate lists
        self.validate_list_lengths(values)
        real_values = []
    
        for index, bit_length in enumerate(self.format_):
            # validate values
            self.validate_value(values[index], bit_length)
    
            shift_distance = self.get_bit_shift_distance(self.format_, index)
            real_value = values[index] << shift_distance
            real_values.append(real_value)
    
        if self.total_bit_length == 32 or self.total_bit_length == 128:
            return ipaddress.ip_address(sum(real_values))
        else:
            return sum(real_values)

    def disjoin(self, value):
        # value = bin(value)
        piece_values = []
        for index, bit_length in enumerate(self.format_):
            mask = (self.get_max_value(bit_length) << self.get_bit_shift_distance(self.format_, index)) #creates a mask of all 1's for only the relevant bits
            real_value = value & mask
            piece_value = real_value >> self.get_bit_shift_distance(self.format_, index)
            piece_values.append(piece_value)
        return piece_values

    def get_bit_shift_distance(self, format_, index):
        shift_distance = sum([x for x in format_[index+1::]])
        return shift_distance

    def validate_value(self, value, bit_length):
        if 0 <= value <= self.get_max_value(bit_length):
            return True
        raise Exception("%s out of range (0 -> %s)" % (value, self.get_max_value(bit_length)))

    def validate_list_lengths(self, values):
        if len(self.format_) != len(values):
            raise Exception("Format List Length (%s) is not equal to Values List Length (%s)" % (len(self.format_), len(values)))
        if len(self.format_) == 0:
            raise Exception("List length can not be 0")
        return True

    def get_max_value(self, bit_length):
        return (1 << bit_length) - 1

