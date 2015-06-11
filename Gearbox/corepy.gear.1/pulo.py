#!/usr/bin/env python

# Self ~ Notice -> Lol this is going to be a gewd pulo file, and this error here is _implied_
#  what if... you do this:: string("something").Part_Of(Self.Notice) ... OMG OMG!
#  what if... you do this:: string("something").part(Self.Notice) ... OMG OMG! 
#   Reverse OOP!!! Sh-shshshshshsh!... fnord...

# This .is: a Registry/Catalog for objects! Keep an Eye on them objects, the 
#  hierarchical way. Fun little Borgish concept 
class Eye(object):
    __state = {}

    def __init__(self, bindage, *args, **context): # There is always something bound on the Eye.
        self.__dict__ = Eye.__state

def check_Eye():
    alpha = "aaaa"
    alpha_beta = "aaa__bbb"

    Eye().alpha = alpha
    Eye().alpha.beta = alpha_beta

    eye = Eye()

    print eye.alpha, eye.alpha.beta

    del e


def echo(what, *args, **keys):
    count = 0
    def print_what():
        print "$$: (({_what}))".format(_what=str(what)),
        count=1

    def print_what():
        print "[[",
        count += 1

    def print_arguments():
        print "[[",
        count += 1
        _it = iter(args)
        arg = next(_it)

        count += 1
        print "arg?",arg,

        for arg in _it:

            print ";arg?{_arg}".format(_arg=arg)
            _count += 1

    def print_
    return _count


