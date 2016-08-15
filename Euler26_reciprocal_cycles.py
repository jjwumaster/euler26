from decimal import *

# figures out after chopping leading #'s what repeating string is
def recurr(strang):
    if len(strang) < 5:
	return 0
    pos = 1
    repeater = 'blah'
    tester = 'woof'
    while repeater != tester:
	repeater = strang[:pos]
	tester = strang[pos:pos + len(repeater)]
	pos += 1
    return repeater


def lengthfinder(minnum, maxnum): # max limit + len of trailing decimal
    maxlen = 0 #length of longest repeating reciprocal

    for x in range(minnum, maxnum):
	if x < 767:
	    decLength = 10 * x
	else:
	    decLength = 1000 * x
        getcontext().prec = decLength
        fR = str(Decimal(1) / Decimal(x)) # full result of division
        tR = fR[2:len(fR)] # truncated result of division w/o leading '0.'
        origtR = tR
        i = 1
    # chop leading zeroes
        if tR[:i] == '0':
	    while tR[:i] == '0':
	        tR = tR[i:]
    # chop leading other #'s!!!!!!!!!!!!!!!!!
    # just chop a few off the front after leading 0's (?)
        tR = tR[5:]
        if len(str(recurr(tR))) > maxlen:
            maxlen = len(str(recurr(tR))) # return longest recurring recip
	print x, ', ' + str(recurr(tR)), ', ' + str(len(str(recurr(tR))))
    return 'max length = ' + str(maxlen)

print lengthfinder(800, 802)

#767

'''
    while strang[pos:pos + 1] == strang[pos - 1:pos]:
	# shit might be repeating
	leadRep = leadRep + strang[pos:pos + 1]
	pos += 1 # keep checking if it's repeating
	# now repeater = all the repeating elements

    if len(leadRep)
    tR = strang[len(leadRep):]
    return tR
# right now this function returns all #'s after leading repeating #'s
'''
