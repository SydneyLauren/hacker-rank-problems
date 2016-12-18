

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


def GOT_palindrome(string):
    l = list(string)
    odd_count = sum([l.count(c) % 2 for c in set(l)])
    if odd_count > 1:
        print 'NO'
    else:
        print 'YES'
GOT_palindrome('cdefghmnopqrstuvw')


def insertionSort(ar):
    for i in range(1, len(ar)):  # loop from one to last index in list
        temp_val = ar[i]  # record the current value
        # compare the current value to each on that precedes it in the list
        j = i
        while j > 0 and temp_val < ar[j - 1]:
            # if the value at previous index is greater, move it back in the list
            ar[j] = ar[j - 1]
            j -= 1
        ar[j] = temp_val  # current value either maintains position or moves forward
        print ' '.join(['%s' % k for k in ar])
print 'insertion sort'
insertionSort([1, 4, 3, 5, 6, 2])
