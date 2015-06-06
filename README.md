# BitDoodle
Python Class for dealing with variable length bit doodles.

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
        
        

EXAMPLES:

-from BitDoodle import BitDoodle
-format_ = [8, 8, 8, 8]
-dood = BitDoodle(format_)
-dood.join([10, 20, 30, 40])
IPv4Address(u'10.20.30.40')

-format_ = [8, 5, 4, 5, 4, 6]
-dood = BitDoodle(format_)
-dood.join([10, 4, 0, 1, 4, 30])
IPv4Address(u'10.32.5.30')

-format_ = [40, 6, 4, 6, 4, 4, 64]
-dood = BitDoodle(format_)
-dood.join([0x200199aa00, 4, 0, 1, 4, 10, 255])
IPv6Address(u'2001:99aa:10:14a::ff')
