import math
import random
from abc import abstractmethod, ABC
import copy
import sys





class Queue:
    
    def __init__(self):
        self.queue = []
        self.len = 0

    def addQueue(self,item):
        self.queue.append(item)
        self.len += 1
        
    def deQueue(self):
        if self.len == 0:
            return None
        self.len -= 1
        temp = self.queue[0]
        del self.queue[0]
        return temp
    
    def top(self):
        return self.queue[-1]


class Stack:
    
    def __init__(self):
        self.stack = []
        self.len = 0
    
    def push(self,element):
        self.stack.append(element)
        self.len += 1

    def pop(self):
        if self.len > 0:
            temp = self.stack[-1]
            del self.stack[-1]
            self.len -= 1
            return temp
        else:
            return None
    
    def top(self):
        return self.stack[-1]



class GreedyMinheap:
    
    def __init__(self):
        self.array = []
        self.len = 0
    
    def insert(self,greedy_node):
        temp = self.len
        self.array.append(greedy_node)
        while(temp != 0):
            if self.array[temp].h_value < self.array[math.floor((temp + 1) / 2) - 1].h_value:
                self.array[temp], self.array[math.floor((temp + 1) / 2) - 1] =                 self.array[math.floor((temp + 1) / 2) - 1], self.array[temp]
                temp = math.floor((temp + 1) / 2) - 1
            else:
                break
                
        self.len += 1
            
    def delMin(self):
        temp_1 = self.array[0]
        temp_2 = 0
        self.array[0] = self.array[-1]
        del self.array[-1]
        
        while(True):
            child_1 = ((temp_2 + 1) * 2) - 1
            child_2 = ((temp_2 + 1) * 2)
            exist_child_1 = True if child_1 <= self.len - 2 else False
            exist_child_2 = True if child_2 <= self.len - 2 else False
            if exist_child_1 and exist_child_2:      
                if self.array[child_1].h_value > self.array[child_2].h_value:
                    if self.array[temp_2].h_value> self.array[child_2].h_value:
                        self.array[temp_2], self.array[child_2] = self.array[child_2], self.array[temp_2]
                        temp_2 = child_2
                    else:
                        break
                        
                else:
                    if self.array[temp_2].h_value > self.array[child_1].h_value:
                        self.array[temp_2], self.array[child_1] = self.array[child_1], self.array[temp_2]
                        temp_2 = child_1
                    else:
                        break
            
            elif exist_child_1 and not exist_child_2:
                if self.array[temp_2].h_value > self.array[child_1].h_value:
                    self.array[temp_2], self.array[child_1] = self.array[child_1], self.array[temp_2]
                    temp_2 = child_1
                else:
                    break
            
            elif not exist_child_1 and not exist_child_2:
                break
                
        self.len -= 1
        return temp_1

    
    def getMin(self):
        return self.array[0]


# In[14]:


class Minheap:
    
    def __init__(self):
        self.array = []
        self.len = 0
    
    def insert(self,node):
        temp = self.len
        self.array.append(node)
        while(temp != 0):
            parent_index = math.floor((temp + 1) / 2) - 1
            if self.array[temp] < self.array[parent_index]:
                self.array[temp], self.array[parent_index] =                 self.array[parent_index], self.array[temp]
                temp = parent_index
            else:
                break
                
        self.len += 1
            
    def delMin(self):
        temp_1 = self.array[0]
        temp_2 = 0
        self.array[0] = self.array[-1]
        del self.array[-1]
        
        while(True):
            child_1 = ((temp_2 + 1) * 2) - 1
            child_2 = ((temp_2 + 1) * 2)
            exist_child_1 = True if child_1 <= self.len - 2 else False
            exist_child_2 = True if child_2 <= self.len - 2 else False
            if exist_child_1 and exist_child_2:      
                if self.array[child_1] > self.array[child_2]:
                    if self.array[temp_2] > self.array[child_2]:
                        self.array[temp_2], self.array[child_2] = self.array[child_2], self.array[temp_2]
                        temp_2 = child_2
                    else:
                        break
                        
                else:
                    if self.array[temp_2] > self.array[child_1]:
                        self.array[temp_2], self.array[child_1] = self.array[child_1], self.array[temp_2]
                        temp_2 = child_1
                    else:
                        break
            
            elif exist_child_1 and not exist_child_2:
                if self.array[temp_2] > self.array[child_1]:
                    self.array[temp_2], self.array[child_1] = self.array[child_1], self.array[temp_2]
                    temp_2 = child_1
                else:
                    break
            
            elif not exist_child_1 and not exist_child_2:
                break
                
        self.len -= 1
        return temp_1

    
    def getMin(self):
        return self.array[0]


# In[15]:


class UCSMinheap:
    
    def __init__(self):
        self.array = []
        self.len = 0
    
    def insert(self,ucs_node):
        temp = self.len
        self.array.append(ucs_node)
        while(temp != 0):
            parent_index = math.floor((temp + 1) / 2) - 1
            if self.array[temp].g_value < self.array[parent_index].g_value:
                self.array[temp], self.array[parent_index] =                 self.array[parent_index], self.array[temp]
                temp = parent_index
            else:
                break
                
        self.len += 1
            
    def delMin(self):
        temp_1 = self.array[0]
        temp_2 = 0
        self.array[0] = self.array[-1]
        del self.array[-1]
        
        while(True):
            child_1 = ((temp_2 + 1) * 2) - 1
            child_2 = ((temp_2 + 1) * 2)
            exist_child_1 = True if child_1 <= self.len - 2 else False
            exist_child_2 = True if child_2 <= self.len - 2 else False
            if exist_child_1 and exist_child_2:      
                if self.array[child_1].g_value > self.array[child_2].g_value:
                    if self.array[temp_2].g_value> self.array[child_2].g_value:
                        self.array[temp_2], self.array[child_2] = self.array[child_2], self.array[temp_2]
                        temp_2 = child_2
                    else:
                        break
                        
                else:
                    if self.array[temp_2].g_value > self.array[child_1].g_value:
                        self.array[temp_2], self.array[child_1] = self.array[child_1], self.array[temp_2]
                        temp_2 = child_1
                    else:
                        break
            
            elif exist_child_1 and not exist_child_2:
                if self.array[temp_2].g_value > self.array[child_1].g_value:
                    self.array[temp_2], self.array[child_1] = self.array[child_1], self.array[temp_2]
                    temp_2 = child_1
                else:
                    break
            
            elif not exist_child_1 and not exist_child_2:
                break
                
        self.len -= 1
        return temp_1

    
    def getMin(self):
        return self.array[0]


# In[16]:


class AStarMinheap:
    
    def __init__(self):
        self.array = []
        self.len = 0
    
    def insert(self,greedy_node):
        temp = self.len
        self.array.append(greedy_node)
        while(temp != 0):
            parent_index = math.floor((temp + 1) / 2) - 1
            if self.array[temp].g_value + self.array[temp].h_value <             self.array[parent_index].g_value + self.array[parent_index].h_value:
                self.array[temp], self.array[parent_index] =                 self.array[parent_index], self.array[temp]
                temp = parent_index
            else:
                break
                
        self.len += 1
            
    def delMin(self):
        temp_1 = self.array[0]
        temp_2 = 0
        self.array[0] = self.array[-1]
        del self.array[-1]
        
        while(True):
            child_1 = ((temp_2 + 1) * 2) - 1
            child_2 = ((temp_2 + 1) * 2)
            exist_child_1 = True if child_1 <= self.len - 2 else False
            exist_child_2 = True if child_2 <= self.len - 2 else False
            if exist_child_1 and exist_child_2:      
                if self.array[child_1].g_value + self.array[child_1].h_value >                 self.array[child_2].g_value + self.array[child_2].h_value:
                    if self.array[temp_2].g_value + self.array[temp_2].h_value >                     self.array[child_2].g_value + self.array[child_2].h_value:
                        self.array[temp_2], self.array[child_2] = self.array[child_2], self.array[temp_2]
                        temp_2 = child_2
                    else:
                        break
                        
                else:
                    if self.array[temp_2].g_value + self.array[temp_2].h_value >                     self.array[child_1].g_value + self.array[child_1].h_value:
                        self.array[temp_2], self.array[child_1] = self.array[child_1], self.array[temp_2]
                        temp_2 = child_1
                    else:
                        break
            
            elif exist_child_1 and not exist_child_2:
                if self.array[temp_2].g_value + self.array[temp_2].h_value >                 self.array[child_1].g_value + self.array[child_1].h_value:
                    self.array[temp_2], self.array[child_1] = self.array[child_1], self.array[temp_2]
                    temp_2 = child_1
                else:
                    break
            
            elif not exist_child_1 and not exist_child_2:
                break
                
        self.len -= 1
        return temp_1

    
    def getMin(self):
        return self.array[0]



