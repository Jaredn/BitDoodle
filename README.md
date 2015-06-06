<h3>BitDoodle</h3><br/>
Python Class for dealing with variable length bit doodles.<br/>
<br/>
Description:<br/>
    Bit Doodle is a class designed for working with variable length bit fields.  While the class can technically be
    used for anything, it is catered towards IPv4 and IPv6 addresses.  The main methods are join and disjoin, which
    will take a list of variable length fields and a list of values and join them together to a single value, or
    disjoin which will take a single value and a list of bit lengths, and break the original value into its multiple
    parts.

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
