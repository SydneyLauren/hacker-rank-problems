# import sys
# h = map(int,raw_input().strip().split(' '))
# word = raw_input().strip()
# n,k = raw_input().strip().split(' ')
# n,k = [int(n),int(k)]
# costs = raw_input().strip().split(' ')
# costs = [int(c) for c in costs]
# bill = raw_input().strip()
# bill = int(bill)

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


def apple_and_orange(s, t, a, b, m, n, apple, orange):
    print 'apples and oranges'
    print len([app + a for app in apple if app + a >= s and app + a <= t])
    print len([ora - b for ora in orange if ora + b <= t and ora + b >= s])
apple_and_orange(7, 11, 5, 15, 3, 2, [-2, 2, 1], [5, -6])


def bon_appetit():
    # import sys
    # n,k = raw_input().strip().split(' ')
    # n,k = [float(n),float(k)]
    # costs = raw_input().strip().split(' ')
    # costs = [float(c) for c in costs]
    # bill = raw_input().strip()
    # bill = float(bill)
    calc_bill = sum([c/2 if i != k else 0 for i, c in enumerate(costs)])
    if bill == calc_bill:
        print 'Bon Appetit'
    else:
        print int(bill - calc_bill)


def utopian_tree(lst):
    print 'utopian tree'
    for i in lst:
        h = 1
        for j in xrange(i):
            if j % 2 == 0:
                h *= 2
            if j % 2 == 1:
                h += 1
        print h

utopian_tree([0, 1, 4])
