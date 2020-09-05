import math
import random
from abc import abstractmethod, ABC
import copy
import sys


class Node:
    
    def __init__(self,name,parent):
        self.name = name
        self.adjacents = []
        self.parent = parent
    
    def addAdjacent(self,node):
        self.adjacents.append(node)
        
    def getAdjacents(self):
        return self.adjacents



class DLS_Node:
    def __init__(self,name,depth,parent):
        self.name = name
        self.adjacents = []
        self.depth = depth
        self.parent = parent
    
    def addAdjacent(self,node):
        self.adjacents.append(node)
        
    def getAdjacents(self):
        return self.adjacents



class UCS_Node:
    
    def __init__(self,name,g_value,parent):
        self.name = name
        self.adjacents = {}
        self.g_value = g_value
        self.parent = parent
    
    def addAdjacent(self,node,distance):
        self.adjacents[node] = distance
        
    def getAdjacents(self):
        return self.adjacents



class A_Star_Node:
    
    def __init__(self,name,g_value,h_value,parent):
        self.name = name
        self.adjacents = {}
        self.g_value = g_value
        self.h_value = h_value
        self.parent = parent
    
    def addAdjacent(self,node,distance):
        self.adjacents[node] = distance
        
    def getAdjacents(self):
        return self.adjacents



class Greedy_Node:
    
    def __init__(self,name,h_value,parent):
        self.name = name
        self.adjacents = []
        self.h_value = h_value
        self.parent = parent
    
    def addAdjacent(self,node):
        self.adjacents.append(node)
        
    def getAdjacents(self):
        return self.adjacents



class HillClimbingNode:
    def __init__(self,name,value):
        self.name = name
        self.value = value



class SimulatedAnnealingNode:
    
    def __init__(self,name,value):
        self.name = name
        self.value = value



class GeneticAlgorithmNode:
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.fitness = None
        self.prob = None
        self.interval = [None,None]


class CSPNode:
    
    def __init__(self,assignments,domains,degree_of_unassigned_vars,unassigned_vars):
        self.assignments = assignments
        self.domains = domains
        self.unassigned_vars = unassigned_vars
        self.degree_of_unassigned_vars = degree_of_unassigned_vars

