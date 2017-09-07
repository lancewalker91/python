try:
    1/0
except ZeroDivisionError:
    print "unkown variable"
else:
    print "that's was well"
finally:
    print "claning up"
