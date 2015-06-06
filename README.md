# BitDoodle<br/>
Python Class for dealing with variable length bit doodles.<br/>
<br/>
Bit Doodle!<br/>
Description:<br/>
    Bit Doodle is a class designed for working with variable length bit fields.  While the class can technically be<br/>
    used for anything, it is catered towards IPv4 and IPv6 addresses.  The main methods are join and disjoin, which<br/>
    will take a list of variable length fields and a list of values and join them together to a single value, or<br/>
    disjoin which will take a single value and a list of bit lengths, and break the original value into its multiple<br/>
    parts.<br/>
join:<br/>
    Description:<br/>
        Given a list of bit lengths, and a list of values, join the values into a single number.  If the bit lengths<br/>
        are exactly 32 or 128 bits, an ipaddress object is returned instead.<br/>
    Inputs:<br/>
        format_ : list of integers, each representing a bit length<br/>
        values : list of integers, each representing a value<br/>
            NOTE: format_ and values must be the same length, or an exception will be thrown.<br/>
            NOTE: Each value must be between 0 and the max value of its corresponding bit-length or an exception<br/>
                  will be thrown.<br/>
    Outputs:      todo: allow user to specify output type<br/>
        A single value that can be of the following types:<br/>
        Int<br/>
        Long<br/>
        ipaddress object (of bit lengths were exactly 32 or 128)<br/>
disjoin:<br/>
    Description:<br/>
        Given a single value and a list of bit lengths, disjoin the value into its bit length values.<br/>
    Inputs:<br/>
        format_ : list of integers, each representing a bit length<br/>
        value : A single value to be broken down into multiple pieces defined by format_<br/>
    Outputs:<br/>
        An array of integers or longs<br/>
        
        

EXAMPLES:

-from BitDoodle import BitDoodle<br/>
-format_ = [8, 8, 8, 8]<br/>
-dood = BitDoodle(format_)<br/>
-dood.join([10, 20, 30, 40])<br/>
IPv4Address(u'10.20.30.40')<br/>
<br/>
-format_ = [8, 5, 4, 5, 4, 6]<br/>
-dood = BitDoodle(format_)<br/>
-dood.join([10, 4, 0, 1, 4, 30])<br/>
IPv4Address(u'10.32.5.30')<br/>
<br/>
-format_ = [40, 6, 4, 6, 4, 4, 64]<br/>
-dood = BitDoodle(format_)<br/>
-dood.join([0x200199aa00, 4, 0, 1, 4, 10, 255])<br/>
IPv6Address(u'2001:99aa:10:14a::ff')<br/>
<br/>
