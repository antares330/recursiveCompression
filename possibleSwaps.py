"""
available swaps


3^7 = 2187
3^8 = 6561
3^9 = 19683

4^5 = 1024
4^6 = 4096
4^7 = 16384
4^8 = 65536
4^9 = 262144

5^5 = 3125
5^6 = 15625
5^7 = 78125
5^8 = 390625
5^9 = 1953125

6^4 = 1296
6^5 = 7776
6^6 = 46656
6^7 = 279936
6^8 = 1679616
6^9 = 10077696

7^4 = 2401
7^5 = 16807
7^6 = 117649
7^7 = 823543
7^8 = 5764801
7^9 = 40353607


8^4 = 4096
8^5 = 32768
8^6 = 262144
8^7 = 2097152
8^8 = 16777216
8^9 = 134217728

9^4 = 6561
9^5 = 59049
9^6 = 531441
9^7 = 4782969
9^8 = 43046721
9^9 = 387420489


Future swaps (these get left out, until some of the other ideas are futher developed)
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880

"""



# sorted to manually CMD + F search
""" (highest compression ratio at the top)
9^9	=	387420489
8^9	=	134217728
9^8	=	43046721
7^9	=	40353607
8^8	=	16777216
6^9	=	10077696
7^8	=	5764801
9^7	=	4782969
8^7	=	2097152
5^9	=	1953125
6^8	=	1679616
7^7	=	823543
9^6	=	531441
5^8	=	390625
6^7	=	279936
4^9	=	262144
8^6	=	262144
7^6	=	117649
5^7	=	78125
4^8	=	65536
9^5	=	59049
6^6	=	46656
8^5	=	32768
3^9	=	19683
7^5	=	16807
4^7	=	16384
5^6	=	15625
6^5	=	7776
3^8	=	6561
9^4	=	6561
4^6	=	4096
8^4	=	4096
5^5	=	3125
7^4	=	2401
3^7	=	2187
6^4	=	1296
4^5	=	1024



The biggest problem is that number of consecutive digits needed before compressing per cycle.
i.e.
5^9	= 1953125           # isn't great
4^5	=	1024          # is great



We might be taking the wrong approach. Let's flip the script.

With a total of 3 characters, how many of the possible 9,999 possiblities of a 4 digit number could we cover?
(what average percentage could we compress by one digit).

This act, plus a proper cycle (such as the proposed 5/5) would make recursive compression a given.

(Moved back to playground.py)















"""
