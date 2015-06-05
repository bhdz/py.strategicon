#!/usr/bin/env python

class N(dict):
    def __init__(self, *args, **keys):
        self.value = None

    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, val):
        del self._value
        self._value = val

    @property
    def name(self):
        return self._value
        
    @name.setter
    def name(self, nam):
        del self._nam
        self._name = nam

    def is_leaf(self):
        return False

    def leafs(self):
        pass

    def branches(self):
        pass

    def branch_first(self):
        pass

    def branch(self, which):
        pass

    def blossom(self)
        pass

    def __str__(self):
        pass

class L(N):
    def __init__(self, value_, *args, **kw):
        super(L, self).__init__(*args, **kw)
        self.value = value_

class Tree(object):
    def __init__(self, *args, **keyword):
        


t = Tree()
Tree.insert(t.root, L("pear"), L("pear2"), N( L()

class Mindmap(Tree):
    pass
