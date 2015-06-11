#!/usr/bin/env python

class Labeled(dict):
    pass

class Dict(Labeled):
    pass

class Dictionary(Dict):
    class Meta(Dictionary):
        pass

    def __init__(self, *arguments, **context):
        super(Dictionary, self).__init__(*arguments, **context)

class Rune(Dictionary):
    pass

class Grammar(Rune):
    pass

class Syntax(Rune):
    pass
