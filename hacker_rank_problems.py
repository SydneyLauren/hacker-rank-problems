

def plus_minus(l, string):
    arr = map(int, string.strip().split(' '))
    print '{:f}'.format(len([x for x in arr if x > 0])/float(l))
    print '{:f}'.format(len([x for x in arr if x < 0])/float(l))
    print '{:f}'.format(len([x for x in arr if x == 0])/float(l))
plus_minus(6, '-4 3 -9 0 4 1')


def staircase(n):
    for i in xrange(1, n + 1):
        print ' ' * (n - i) + '#' * i
staircase(4)


def two_characters(s):
    lst = list(s)
    output = 0
    st = set(s)

    for c1 in st:
        for c2 in st:
            ns = [s for s in lst if s in [c1, c2] if c1 != c2]
            if len(set(ns[1::2])) == 1 & len(set(ns[0::2])) == 1 & len(ns) > output:
                output = len(ns)
    print output
two_characters('xyxy')


def mars_exploration(s):
    sos_string = 'SOS' * (len(s) / 3)

    diffs = [c for i, c in enumerate(s) if c != sos_string[i]]
    print len(diffs)

mars_exploration('SOSSOT')
