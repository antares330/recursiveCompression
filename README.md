# recursiveCompression
 [WIP] Infinite lossless compression


** This project is digital alchemy. A long shot that would have sweeping implications but that many think impossible. **</br>

Imagine zipping a 4 gb file to mere megabytes, without sacrificing any data once unzipped; that's the dream.

</br>
-- Long winded: TL;DR at the bottom --

This idea was sparked by Mersenne prime numbers (thanks NumberPhile). "2^82589933 − 1" is a formula that once solved, gives you the worlds largest prime number that is 24,862,048 digits long, but is losslessly represented by 14 digits / characters.

Current strategy:</br>
1a. Data file initialization (binary to actual number)

Recursive compression loop:</br>
1b. Remove as many digits as possible (without loss)


Single digit exponents - testing with 1 digit per side max</br>
3^7 = 2,187 (3 digits representing 4 digits) - compression of 1 digit</br>
3^8 = 6,561 (3 -> 4)</br>
3^9 = 19,683 (3 -> 5) - compression of 2 digits</br>
4^5 = 1,024 (3 -> 4)</br>
...</br>
9^8 = 43,046,721 (3 -> 8) - compression of 5 digits</br>
9^9 = 387,420,489 (3 -> 9) - compression of 6 digits</br>

We search through the whole number and replace any occurrences of the above the numbers (starting at the highest compression of digits, to maximize compression)

Future note: This is only the start, there will be additional compression formulas like:</br>
5! = 120 (2 -> 3) ... 9! = 362,880 (2 -> 6).

1c. Transform the compressed number in the following binary pattern

Original number: (although ineffective on small numbers, I cherry pick small numbers to demonstrate strategy)
4,565,619,531 (commas added only for readability)

--> Compressed number</br>
453^89531  -  (We assume any "^" takes a single digit from either side of itself)

--> 5 bit binary:</br>
4 = 00100</br>
5 = 00101</br>
3 = 00011</br>
^ = 01010 (10th value onwards can be used as function symbols to compress)</br>
8 = 01000</br>
9 = 01001</br>
5 = 00101</br>
3 = 00011</br>
1 = 00001</br>

==> 00100 00101 00011 01010 01000 01001 00101 00011 00001

2a. 5 bit binary --> 6 bit binary

==> 00100 00101 00011 01010 01000 01001 00101 00011 00001</br>
To: 001000 010100 011010 100100 001001 001010 001100 001XXX

X's represent 0's that are needed to fill out the rest of 6 bit pattern - this will need to be addressed later, and may need to be stored as an extra number at the end of the formula

2b. 6 bit binary --> actual number</br>
==> 001000 010100 011010 100100 001001 001010 001100 001000</br>
==>   8      20     26     38     9      10     12      8</br>
==> 8,202,638,910,128</br>

Future note: Likely, some mathematical formula will be entered here, so the numbers change (and won't get stuck between the 5/6 bit loop when no numbers are compressed)</br>
(i.e. x3 for 5 bit, x2 for 6 bit loop)

2c. Compress numbers (no numbers to compress due to small size of starting number)

Loop to 1 (1 is 5 bit, 2 is 6 bit).

==> 8,202,638,910,128

8 = 01000</br>
2 = 00010</br>
0 = 00000</br>
2 = 00010</br>
6 = 00110</br>
3 = 00011</br>
8 = 01000</br>
9 = 01001</br>
1 = 00001</br>
0 = 00000</br>
1 = 00001</br>
2 = 00010</br>
8 = 01000</br>

==> 01000 00010 00000 00010 00110 00011 01000 01001 00001 00000 00001 00010 01000</br>
==>   8     2     0     2     6     3     8     9     1      0    1     2     8</br>
==> 8,202,638,910,128 (in this case no digits changed in the bit transfer/swap because no compression happened)</br>

Also worth noting, the swap process currently gains digits, so will need to be refined significantly (or the compression needs to compensate for it)


TL;DR</br>
Data -> Binary -> Number</br>
Compress Number: Replace subsets with compressed version (i.e. 6,561 into 3^8)</br>
Turn the whole thing into a pure number again (i.e. "^" becomes a number, but in a reversible way to decompress later)</br>
Repeat</br>
