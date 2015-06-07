<h1>BitDoodle!</h1>
<h2>Python Class for dealing with variable length bit doodles.</h2>
<br/>
<h3>Description:</h3>
    Bit Doodle is a class designed for working with variable length bit fields.  While the class can technically be
    used for anything, it is catered towards IPv4 and IPv6 addresses.  The main methods are join and disjoin, which
    will take a list of variable length fields and a list of values and join them together to a single value, or
    disjoin which will take a single value and a list of bit lengths, and break the original value into its multiple
    parts.

<h2>EXAMPLES:</h2><br/>

<h3>Basic useage simple example</h2>
&gt;&gt;&gt; from BitDoodle import BitDoodle<br/>
&gt;&gt;&gt; format_ = [8, 8, 8, 8]<br/>
&gt;&gt;&gt; dood = BitDoodle(format_)<br/>
&gt;&gt;&gt; dood.join([10, 20, 30, 40])<br/>
<b>IPv4Address(u'10.20.30.40')</b><br/>
&gt;&gt;&gt; <br/>
&gt;&gt;&gt; dood.total_bit_length<br/>
<b>32</b><br/>
<h3>Not so obvious IPv4 example</h3>
Imagine if a standard IP address was broken up into meaningful pieces.  For example the first 8 bits are a static 10, but the next 5 bits represent your datacenter, and the next 4 bits might represent the security zone, and the next 4 bits might represent the pod number, and so on.  Given a format and values to put into the fields, you can generate a meaningful IP address.<br/>
&gt;&gt;&gt; format_ = [8, 5, 4, 5, 4, 6]<br/>
&gt;&gt;&gt; dood = BitDoodle(format_)<br/>
&gt;&gt;&gt; dood.join([10, 4, 0, 1, 4, 30])<br/>
<b>IPv4Address(u'10.32.5.30')</b><br/>
<br/>
<h3>Not so obvious IPv6 example</h3>
This is the same as above, but for IPv6.  If ARIN (or your RIR) gave you a /40, the first 40 bits would be static, then the next 24 bits could mean something specific to your use case, split up however you want.  Finally the last 64 are the host, which you could also break down further if you wanted.  This is more to show BitDoodle working fine with very large numbers.<br/>
&gt;&gt;&gt; format_ = [40, 6, 4, 6, 4, 4, 64]<br/>
&gt;&gt;&gt; dood = BitDoodle(format_)<br/>
&gt;&gt;&gt; dood.join([0x200199aa00, 4, 0, 1, 4, 10, 255])<br/>
<b>IPv6Address(u'2001:99aa:10:14a::ff')</b><br/>
<br/>

<h3>Disjoin example</h3>
Disjoin does the opposite of join.  Given a format and an integer (in this case, represented as a binary number / IP address), return the values of each section.  So just like above, if you knew the IP address you could find out the data center, security zone, pod, etc, of each field.<br/>
&gt;&gt;&gt; format_ = [8, 5, 4, 5, 4, 6]<br/>
&gt;&gt;&gt; dood = BitDoodle(format_)<br/>
&gt;&gt;&gt; dood.disjoin(0b00001010000011111111111100101101)<br/>
[10L, 1, 15, 31, 12, 45]
