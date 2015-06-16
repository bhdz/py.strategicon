#!/usr/bin/env python

class Details(object):
    """ All properties starting with '_' and '__' are separated from the propper
     class properties. """
    def __init__(self, hidden1={}, hidden2={}, *args, **kw):
        self.__details = {}
        self.__test = 1
        self._hidden = {}

    def __getattr__(self, name):
        r = None
        s = self.__dict__
        k = self.__class__
        kn = k.__name__
        
        t = None
        if name.startswith('_%s' % kn):
            print "$%s" % (name)
            t = self.__dict__
        else:
            print "!%s" % (name)
            t = self.__dict__['_%s__details' % kn]
            
        if not (t is None):
            r = t[name]
        return r
        
    def __setattr__(self, name, value):
        r = None
        t = None
        s = self.__dict__
        k = self.__class__
        kn = k.__name__
        
        t = None
        if name.startswith('_%s' % kn):
            print "$%s := %s" % (name, value)
            t = self.__dict__
        else:
            print "!%s := %s" % (name, value)
            t = self.__dict__['_%s__details' % kn]
        
        if not (t is None):
            t[name] = value
            print "\t[%s] -> %s" % (name, t[name])
            r = value
        return r

def check_Details():
    import os, sys
    h = Details()
    h.test = 1.0
    h._test = "One"
    h.__test = 23
    
    print h.test
    print h._test
    print h.__test

test_Details()
###

class Adapt(Details):
    def __init__(self, adaptee, to, *args, **kw):
        self.__trunk = {}

def check_Adapt():
    class A(object):
        def __init__(self, *a, **k):
            pass
            
        def foo(self, baz, bar):
            r = None
            print "foo@A: baz:%s, bar:%s = %s" % (baz, bar, r)

        def foobar(self, baz, bar, msg):
            pass
            
    class B(object):
        def __init__(self, *a, **k):
            pass
            
        def foo(self, baz):
            r = None
            print "foo@B: baz:%s = %s" % (baz, r)
            
        def bar(self, msg):
            r = None
            print "bar@B: msg:%s = %s" % (msg, r)

    a = A()
    a.foo("Joe", 1)

    b = B()
    b.foo("Joe")


    # Adapt instances
    b2 = Adapt(a, b)
    b2.foo("Joe2", 2)

    # Adapt whole classes

    b3 = B2() # Must produce an adapted instance. 
    b3.foo("Joe3", 3)
    b3.bar("blabla")
#check_Adapter
###



