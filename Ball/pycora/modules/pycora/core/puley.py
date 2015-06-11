#!/usr/bin/env python

if __name__ == "__main__":
    pass

def mix(obj, *objects, **properties):
    return None

def check_mix():
    person = {'age': 35, 'sex': 'male'}
    mix(person, {'name': None}, name = "Borko", location = "Bulgaria")


class Labeled(dict):
    def __init__(self, _value, *args, **context):
        self.value = _value
        for a in args:
            self[a] = None
        for k, v in context.iteritems():
            self[k] = v

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, another):
        self._value = another

    @property
    def labels(self):
        return dict(self)


def check_Labeled():
    my_weight = Labeled(120, 'kg')
    print my_weight.value


    homes = Labeled('My Sweet homes', flat = False)
    homes['suburban'] = False
    homes['rural'] = True
    print homes.labels

class Node(Labeled):
    def __init__(self, value, **context):
        super(Node, self).__init__(value)

    def __getitem__(self, key):
        return super(Node, self).__getitem__(key)

    def __setitem__(self, key, value):
        value = Node(value)
        super(Node, self).__setitem__(key, value)

def check_Node():
    r = Node("root")
    #r.car = "Toyota"
    #r.car.color = "Blue"
    #r.car.color.paintjob = "Metalic"
    #r.car.engine = "V8"
    #r.car.engine.power = Labeled(300 'hp')
    r['car'] = "Toyota"
    print "r['car'] = ", r['car']
    r['car']['color'] = "Red"
    r['car']['color']['paintjob'] = "Metalic"
    r['car']['engine'] = "Merlin"
    r['car']['engine']['power'] = Labeled(300, 'hp')
    print r['car'].value
    print r['car']['color'].value
    print r['car']['color']['paintjob'].value
    print r['car']['engine']['power'].value
    print "> ", r['car']['engine']['power']


class Registry(Node):

    def __init__(self, value, section = None):
        super(Registry, self).__init__(value)
        #self._section = Node(section)

    def __setattr__(self, name, val):
        #value = Registry(val)
        super(Registry, self).__setitem__(name, val)

    def __getattr__(self, name):
        
        ret = super(Registry, self).__getitem__(name)
    

        return ret

def check_Registry():
    car = Registry("Mazda")
    car.paint = "Metalic"
    print car.paint
    car.paint.color = "Red"
    print car.paint.color
    car.engine = "Big"
    car.engine.type = "V8"
    print car.engine.type
    car.engine.type.smack = "V8asdasd"

class Proxy(object):
    def __init__(self, *args, **kw):
        pass


class Eye(object):
    __state = {}

    def __init__(self, section):
        pass
        
def check_Eye():
    Eye().person.boril 

if __name__ == "__main__":
    #check_Labeled()
    #check_Details()
    #check_Node()
    check_Registry()
