# this file is a fresh playground with more focus on visual representations of potential theories.
#
# after typing up the readme of this respository, it hit me how vague or unfleshed out ideas there are.
# that's what this playground is for, an in-depth look, without trying to keep it short.

"""
321,895,712,389,327,684,897 - number
321895712389327684897 - no commas




5/5 bit swapping

3 = 00011
2 = 00010
1 = 00001
8 = 01000
9 = 01001
5 = 00101
7 = 00111
1 = 00001
2 = 00010
3 = 00011
8 = 01000
9 = 01001

8 = 01000
^ = 01010
5 = 00101

4 = 00100
8 = 01000
9 = 01001
7 = 00111

Swaps used
8^5	= 32768


Double digit binary swap
00011 = 3
00010 = 2
00001 = 1
01000 = 8
01001 = 9
00101 = 5
00111 = 7
00001 = 1
00010 = 2
00011 = 3
01000 = 8
01001 = 9

01000 = 8
01010 = 10
00101 = 5

00100 = 4
01000 = 8
01001 = 9
00111 = 7


32189571238981054897 # New number
321895712389327684897 # Old Number

("lucky" swap, and only 1 digit gained...)

"""



"""

Number combinations of 6 values

To find maximum number of 4 digit possibilities, from 6 different numbers being combined.

Example:

a = 12
b = 15
c = 28
...

a*b*c (assumed multiplication) becomes abc = 5040 (but with 3 digits)


Testing from the fourDigit tab in the playground, leads me to start at:
Start = 3
gap size = 4 (between numbers)

values 2, 4 and 6 have +1 added (to have some even numbers in the mix)

which equals
a = 3
b = 12
c = 15
d = 20
e = 23
f = 28

"""

a = 3
b = 12
c = 15
d = 20
e = 23
f = 28


# start a dictionary with all possible swaps
dict_swaps = {
#    "aaa":"27"
}

possible_variables = [a,b,c,d,e,f]

# loop through aaa, aab, aac, aad, aae, aaf, aba, abb, abc abd... etc

variables_count = 0

i_index = 0
j_index = 0
k_index = 0
for i in possible_variables:
    for j in possible_variables:
        for k in possible_variables:
            dict_swaps[str(i_index) + str(j_index) + str(k_index)] = i*j*k
            variables_count = variables_count + 1

            k_index = k_index + 1
        k_index = 0
        j_index = j_index + 1
    j_index = 0
    i_index = i_index + 1


#print(dict_swaps)

print(variables_count)

































#
