# this file is a fresh playground with more focus on visual representations of potential theories.
#
# after typing up the readme of this respository, it hit me how vague or unfleshed out ideas there are.
# that's what this playground is for, an in-depth look, without trying to keep it short.

import pandas as pd
import random

#import an excel for storage and testing between runs
import_export_excel = "storage/storage.xlsx"

storageFile = pd.read_excel(import_export_excel)
#print(storageFile)

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


a = 1
b = 3
c = 7
d = 15
e = 17
f = 23

fourDigitCoverage = []
fiveDigitCoverage = []

def runTest():
    global fourDigitCoverage
    global fiveDigitCoverage
    fourDigitCoverage = []
    fiveDigitCoverage = []


    # add all numbers to the following lists here
    four_loopCount = 9999
    five_loopCount = 99999

    # add all numbers under 9,999 to "fourDigitCoverage", then we'll remove them as we add them to possible swaps
    i = 1
    while (i <= four_loopCount):
        fourDigitCoverage.append(i)
        i += 1

    # same as fourDigitCoverage, but now with 5 digits
    i = 1
    while (i <= five_loopCount):
        fiveDigitCoverage.append(i)
        i += 1




    # start a dictionary with all possible swaps
    dict_swaps = {
    #    "aaa":"27"
    }

    possible_variables = [a,b,c,d,e,f]
    #print(possible_variables)
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

                # check if the value is still in the fourDigitCoverage list, if so, remove it
                if(i*j*k in fourDigitCoverage):
                    fourDigitCoverage.remove(i*j*k)

                # same as fourDigitCoverage version above, but for the fiveDigitCoverage List
                if(i*j*k in fiveDigitCoverage):
                    fiveDigitCoverage.remove(i*j*k)
                # check if the value is in the fourDigit / fiveDigit coverage lists, if so, remove them

                k_index = k_index + 1
            k_index = 0
            j_index = j_index + 1
        j_index = 0
        i_index = i_index + 1




def storeTest():
    global fourDigitScore
    global fiveDigitScore
    fourDigitScore = 9999-len(fourDigitCoverage)
    fiveDigitScore = 99999-len(fiveDigitCoverage)
    storageFile.loc[len(storageFile.index)] = [fourDigitScore, fiveDigitScore, a,b,c,d,e,f]


runTest()
storeTest()







def randomVariables():
    global a,b,c,d,e,f
    a = random.randrange(0,10)
    b = random.randrange(0,15)
    c = random.randrange(0,20)
    d = random.randrange(0,25)
    e = random.randrange(0,30)
    f = random.randrange(0,35)



cycleCounts = 5000
i = 0

"""
while (i < cycleCounts):
    randomVariables()
    runTest()
    storeTest()
    i = i + 1
    print(i)
"""
















"""
this system works really well as feedback to what works well and what doesn't work at all.

now that we have a great feedback loop, it's time to maximize the 5 bit version..
and maybe consider a 6 bit version (with 38 variable numbers, as compared to 6)


We also need to establish rules around variables with decimals places, and what happens with decimal places in product.

My feeling is that decimals should always ceiling or floor (as opposed to rounding), although rounding might give more
potential options. (minor digit tweaks leading to rounding up, rather than down, giving many new options)


As far as the 5 bit vs 6 bit potential..
6^6 = 45,656
38^38 = 1.07591180197999398206E+60

I feel as though, with 38^38 and hella long floats (machine learning optimized), you may be able to hit a majority
of 4 or 5 digit possibilities (even primes among others normally not accessible), and could make compression straight forward!


This would mean more 4 digits then not would go from 4 digits, down to 3 EVERY CYCLE!

For a 1,000 digit number..

1000 / 4 (number of 4 digit chunks)

250 chunks, where 1/2 or more get compressed (on average)

125 chunks (so subtract 125 from 1,000)

875 digits remaining. (a 12.5% reduction in size on disk without data loss, PER CYCLE!)


The 3 main concerns then are this.
1. To verify the validity of the above strategy as viable (especially, the ability to reach a coverage of above 50%)
2. Making the 5/5 bit or 5/6 bit swap using less than the amount that was compressed (12.5%)
"""


#print(dict_swaps)

#print(variables_count)


# we need some method for checking to see how many of the 4 digit possibilities we are covering (maybe 4-5)

# a list with all numbers between 0 - 9,999 at the start, then removing them as we use them would give us how many are left.










storageFile.to_excel(import_export_excel, index=False)
















#
