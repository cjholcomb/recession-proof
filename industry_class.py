from lookups import *
from helper_functions import *
from list_maker import *

class Industry(object):
    #Collects all the important info about an industry

def __init__(self, code):
    self.code = code
    self.title = all_industries [code]
    self.generation = 0
    self.parent = 0
    self.siblings = []
    self.cousins = []
    self.children = []
    self.empPeak = 0
    self.firmPeak = 0
    self.wagePeak = 0
    self.empGrowth = 0
    self.firmGrowth = 0
    self.wageGrowth = 0

def find_generation(self, code):
    if code < 100:
        self.generation = 1
    elif code < 1000:
        self.generation = 2
    elif code < 10000:
        self.generation = 3
    elif code < 100000:
        self.generation = 4
    elif code < 1000000:
        self.generation = 5

def find_parent(self, code):
    if self.code = 10:
        self.parent = None
    elif self.generation = 1:
        self.parent = 10
    else:
        parent = code //10
        parentgen = self.generation - 1
        while parent not in generation_dict[parentgen]:
            parent = -1
        self.parent = parent

def find_cousins(self,code):
    self.cousins = generation_dict[self.generation].remove(code) 

# def find_siblings(self, code):
#     if self.generation = 0:
#         self.generation = find_generation
#     if self.parent = 0:
#         self.parent = find_parent(self, code)

def find_children

    

