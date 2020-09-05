from DataStructs import *
from Nodes import *
import math
import random
from abc import abstractmethod, ABC
import copy



class BFS(ABC,object):
    
    def __init__(self,initial_state=None,goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.queue = Queue()
        self.queue.addQueue(Node(initial_state,parent=None))
        self.path = []
        self.stop = False
        
    def run(self):
        while(True):
            if self.stop:
                return
            element = self.queue.deQueue()
            if(not self.checkGoal(element)):
                adjacents = self.getAdjacents(element)
                for adjacent in adjacents:
                    self.queue.addQueue(Node(adjacent,element))
            else:
                self.returnAnswer(element)
                return self.path
            
    @abstractmethod
    def getAdjacents(self,node):
        pass

    
    def checkGoal(self,node):
        if node.name == self.goal_state:
            return True
        else:
            return False
        
    def returnAnswer(self,node):
        while(node.parent != None):
            self.path.append(node.name)
            node = node.parent
        self.path.append(self.initial_state)
        self.path.reverse()



class DFS(ABC):
    
    def __init__(self,initial_state=None,goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.stack = Stack()
        self.stack.push(Node(self.initial_state,parent=None))
        self.path = []
        self.stop = False
        
    def run(self):
        while(True):
            if self.stop:
                return
            element = self.stack.pop()
            if(not self.checkGoal(element)):
                adjacents = self.getAdjacents(element)
                random.shuffle(adjacents)
                for adjacent in adjacents:
                    self.stack.push(Node(adjacent,element))
            else:
                self.returnAnswer(element)
                return self.path
    
    @abstractmethod
    def getAdjacents(self,node):
        pass

            
    def checkGoal(self,node):
        if node.name == self.goal_state:
            return True
        else:
            return False
        
    def returnAnswer(self,node):
        while(node.parent != None):
            self.path.append(node.name)
            node = node.parent
        self.path.append(self.initial_state)
        self.path.reverse()
        


class UCS(ABC):
    
    def __init__(self,initial_state=None,goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.priorityQueue = UCSMinheap()
        self.priorityQueue.insert(UCS_Node(initial_state,g_value=0,parent=None))
        self.path = []
        self.stop = False
        
    def run(self):
        while(True):
            if self.stop:
                return
            element = self.priorityQueue.delMin()
            print(element.name)
            if(not self.checkGoal(element)):
                adjacents = self.getAdjacents(element)
                for adjacent in adjacents:
                    adjacent_g_value = element.g_value + adjacent[1]
                    self.priorityQueue.insert(UCS_Node(adjacent[0],g_value=adjacent_g_value,parent=element))
                    
            else:
                self.returnAnswer(element)
                return self.path
    
    @abstractmethod
    def getAdjacents(self,node):
        pass
    
    def checkGoal(self,node):
        if node.name == self.goal_state:
            return True
        else:
            return False
        
    def returnAnswer(self,node):
        while(node.parent != None):
            self.path.append(node.name)
            node = node.parent
        self.path.append(self.initial_state)
        self.path.reverse()
        


class AStar(ABC):
    
    def __init__(self,initial_state_h_value,initial_state=None,goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.priorityQueue = AStarMinheap()
        self.priorityQueue.insert(A_Star_Node(initial_state,g_value=0,h_value=initial_state_h_value,parent=None))
        self.path = []
        self.pause = False
        self.memory = 0
        self.stop = False
        
    def run(self):
        while(True):
            if self.stop:
                return
            if not self.pause:
                element = self.priorityQueue.delMin()
                if(not self.checkGoal(element)):
                    adjacents = self.getAdjacents(element)
                    for adjacent in adjacents:
                        self.memory += 1
                        adjacent_g_value = element.g_value + adjacent[1]
                        self.priorityQueue.insert(A_Star_Node(adjacent[0],g_value=adjacent_g_value,h_value=adjacent[2],parent=element))

                else:
                    self.returnAnswer(element)
                    return self.path
    
    @abstractmethod
    def getAdjacents(self,node):
        pass
    
    def checkGoal(self,node):
        print (self.memory, end="\r")
        if node.name == self.goal_state:
            return True
        else:
            return False
        
    def returnAnswer(self,node):
        while(node.parent != None):
            self.path.append(node.name)
            node = node.parent
        self.path.append(self.initial_state)
        self.path.reverse()


      
        
class DLS(ABC):
    
    def __init__(self,initial_state=None,goal_state=None,max_depth=0):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.max_depth = max_depth
        self.stack = Stack()
        self.stack.push(DLS_Node(self.initial_state,depth=0,parent=None))
        self.path = []
        self.stop = False
        
    def run(self):
        while(True):
            if self.stop:
                return
            element = self.stack.pop()
            if element == None:
                return False
            if(not self.checkGoal(element)):
                if element.depth < self.max_depth:
                    adjacents = self.getAdjacents(element)
                    random.shuffle(adjacents)
                    for adjacent in adjacents:
                        self.stack.push(DLS_Node(adjacent,depth=element.depth+1,parent=element))
            else:
                self.returnAnswer(element)
                return self.path
    
    @abstractmethod
    def getAdjacents(self,node):
        pass

            
    def checkGoal(self,node):
        if node.name == self.goal_state:
            return True
        else:
            return False
        
    def returnAnswer(self,node):
        while(node.parent != None):
            self.path.append(node.name)
            node = node.parent
        self.path.append(self.initial_state)
        self.path.reverse()


   
class HillClimbing(ABC,object):
    
    def __init__(self,initial_state=None,goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.element = HillClimbingNode(name=self.initial_state,value=self.getValue(self.initial_state))
        self.step = 0
        self.stop = False
        
    def run(self):
        while(True):
            if self.stop:
                return
            print(self.step,end='\r')
            self.step += 1
            adjacents = self.getAdjacents(self.element)
            name, value = self.findMaxValue(adjacents)
            node = HillClimbingNode(name=name,value=value)
            if not self.checkGoal(node):
                self.element = node
            else:
                return self.element.name, self.element.value
                
                
    def findMaxValue(self,adjacents):
        maximum_value = sys.maxsize
        maximum_node = None
        for adjacent in adjacents:
            if adjacent[1] < maximum_value:
                maximum_value = adjacent[1]
                maximum_node = adjacent
        return maximum_node
    
    @abstractmethod
    def getAdjacents(self,node):
        pass
    
    @abstractmethod
    def getValue(self,node):
        pass
    
    def checkGoal(self,node):
        if node.value < self.element.value:
            return False
        else:
            return True




class CSP: 

    def __init__(self,graph,initial_state,domain_count,MRV_heuristic=False,degree_heuristic=False,lcv_heuristic=False,forward_checking=False,arc_consistency=False): 
        self.graph = graph
        self.MRV_heuristic = MRV_heuristic
        self.degree_heuristic = degree_heuristic
        self.lcv_heuristic = lcv_heuristic
        self.forward_checking = forward_checking
        self.arc_consistency = arc_consistency
        self.stack = Stack()
        self.stack.push(initial_state)
        self.domain_count = domain_count
        self.current_element = initial_state
        self.pause = False
        self.have_answer = True
        self.nodes = []
        self.edges = []
        self.done = False
        self.stop = False
        for key, values in self.graph.items():
            self.nodes.append(key)
            for value in values: 
                self.edges.append([key,value])
            
        

    



    def run(self):
        while(True):
            if self.stop:
                return
            if(not self.pause):
                element = self.stack.pop()
                if element == None:
                    self.have_answer = False
                    return
                variable = self.getNextVar(element)
                if(self.lcv_heuristic):
                    pass

                else:
                    for domain in element.domains[variable]:
                        x = copy.deepcopy(element)
                        x.domains[variable] = [domain]
                        x.assignments[variable] = domain

                        if self.arc_consistency:
                            res, x_new = self.arcConsistency(x,variable)
                            if(res == True):
                                self.current_element = x_new
                                x_new.unassigned_vars = element.unassigned_vars - 1
                                self.stack.push(x_new)
                                if self.checkGoal(x_new):
                                    self.done = True
                                    return x_new.assignments

                        elif self.forward_checking:
                            res, x_new = self.forwardCheking(x,variable)
                            if(res == True):
                                self.current_element = x_new
                                x_new.unassigned_vars = element.unassigned_vars - 1
                                for adjacent in self.graph[variable]:
                                    if x_new.assignments[adjacent] == None:
                                        x_new.degree_of_unassigned_vars[adjacent] -= 1

                                self.stack.push(x_new)  
                                if(self.checkGoal(x_new)):
                                    self.done = True
                                    return x_new.assignments                  

                        else:
                            res, x_new = self.checkValidityWithNoHeuristic(x,variable)
                            if(res == True):
                                self.current_element = x_new
                                x_new.unassigned_vars = element.unassigned_vars - 1
                                self.stack.push(x_new)
                                if(self.checkGoal(x_new)):
                                    self.done = True
                                    return x_new.assignments

    


    def getNextVar(self,element):
        variable = None
        
        if self.MRV_heuristic:
            temp = self.MRV(element)
            if (len(temp) > 1) and self.degree_heuristic:
                variable = self.degree(element,temp)
            
            elif (len(temp) > 1) and not self.degree_heuristic:
                variable = temp[0]
            
            elif len(temp) == 1:
                variable = temp[0]
            
        
        elif self.degree_heuristic:
            variable = self.degree(element)
        
        else:
            for key,value in element.assignments.items():
                if value == None:
                    variable = key
                    break

        return variable
    



    def MRV(self,element):
        temp = []
        min_domain_choice = sys.maxsize
        for key, values in element.domains.items():
            if element.assignments[key] == None:
                if len(values) < min_domain_choice: 
                    temp = []
                    min_domain_choice = len(values)
                    temp.append(key)

                elif len(values) == min_domain_choice:
                    temp.append(key)
        return temp
    

    def degree(self,element,candidates=None):
        max_value = 0
        id_of_candidate = None
        if(candidates != None):
            for candidate in candidates:
                if element.degree_of_unassigned_vars[candidate] >= max_value:
                    max_value = element.degree_of_unassigned_vars[candidate]
                    id_of_candidate = candidate
                
            
        
        else: 
            for id_ in self.nodes:
                if element.assignments[id_] == None:
                    if element.degree_of_unassigned_vars[id_] >= max_value:
                        max_value = element.degree_of_unassigned_vars[id_]
                        id_of_candidate = id_                      
            
        return id_of_candidate
    
    


    def lcv(self,element):
        pass

    

    def arcConsistency(self,x,variable):
        edge_queue = Queue()
        for edge in self.edges:
            edge_queue.addQueue(edge)
        
        while(True):
            arc = edge_queue.deQueue()
            if(arc == None):
                return True, x
            
            if self.removeInconsistentDomains(x,arc[0],arc[1]):
                if x.domains[arc[0]] == []:
                    return False, x
                for adjacent in self.graph[arc[0]]:
                    edge_queue.addQueue([adjacent,arc[0]])
                
    def removeInconsistentDomains(self,x,node_1,node_2):
        final_res = False
        res = None
        remove_candidates = []
        index = None
        
        for domain_1 in x.domains[node_1]:
            res = False
            for domain_2 in x.domains[node_2]:
                if(domain_1 != domain_2):
                    res = True
            
            if(res != True): 
                remove_candidates.append(domain_1)
                final_res = True
            
        
        for domain in remove_candidates:
            x.domains[node_1].remove(domain)
        
        return final_res    
        
    

    def forwardCheking(self,x,variable):
        value = x.assignments[variable]
        for adjacent in self.graph[variable]: 
            if value in x.domains[adjacent]:
                x.domains[adjacent].remove(value)
                if x.domains[adjacent] == []:
                    return False, x
            
        
        return True, x
    

    def checkValidityWithNoHeuristic(self,x,variable):
        value = x.assignments[variable]
        for adjacent in self.graph[variable]:
            if value == x.assignments[adjacent]:
                return False, x
        
        return True, x
    

    def checkGoal(self,x_new):
        if x_new.unassigned_vars == 0:
            return True    
        else: 
            return False




class RRHillClimbing(ABC,object):
    
    def __init__(self,steps=1):
        self.initial_state = None
        self.steps = steps
        self.max_value = sys.maxsize
        self.max_node = None
        self.step = 0
        self.stop = False
        
    def run(self):
        for i in range(self.steps):
            self.initial_state = self.getInitialState()
            self.element = HillClimbingNode(name=self.initial_state,value=self.getValue(self.initial_state))
            while(True):
                    if self.stop:
                        return
                    print(self.step,end='\r')
                    self.step += 1
                    adjacents = self.getAdjacents(self.element)
                    name, value = self.findMaxValue(adjacents)
                    node = HillClimbingNode(name=name,value=value)
                    if not self.checkGoal(node):
                        self.element = node
                    else:
                        break
            if self.element.value < self.max_value:
                self.max_node = self.element.name
                self.max_value = self.element.value
        return self.max_node, self.max_value
                
                
    def findMaxValue(self,adjacents):
        maximum_value = sys.maxsize
        maximum_node = None
        for adjacent in adjacents:
            if adjacent[1] < maximum_value:
                maximum_value = adjacent[1]
                maximum_node = adjacent
        return maximum_node
    
    @abstractmethod
    def getInitialState(self):
        pass
    
    @abstractmethod
    def getAdjacents(self,node):
        pass
    
    @abstractmethod
    def getValue(self,node):
        pass
    
    def checkGoal(self,node):
        if node.value < self.element.value:
            return False
        else:
            return True
        



class GenticAlgorithm(ABC):
    
    def __init__(self,initial_chromosomes,max_fitness,steps,mutation_prob):
        self.steps = steps
        self.population = len(initial_chromosomes)
        self.chromosomes = []
        self.chromosome_length = len(initial_chromosomes[0])
        for chromosome in initial_chromosomes:
            self.chromosomes.append(GeneticAlgorithmNode(name=chromosome,value=self.getValue(chromosome)))
        self.mutation_prob = mutation_prob
        self.total_fitness = 0
        self.max_fitness = max_fitness
        self.test = 0
        
    def selectPrents(self):
        self.computeFitnesses()
        temp = []
        for i in range(self.population):
            parent_1 = self.selectParent()
            parent_2 = self.selectParent()
            temp.append([parent_1,parent_2])
        return temp
    
    def computeFitnesses(self):
        self.total_fitness = 0
        for i, chromosome in enumerate(self.chromosomes):
            chromosome.fitness = pow(chromosome.value, 8)
            chromosome.interval[0] = self.total_fitness
            self.total_fitness += chromosome.fitness
            chromosome.interval[1] = self.total_fitness - 1
            
            
        for chromosome in self.chromosomes:
            chromosome.prob = chromosome.fitness / self.total_fitness
            print(chromosome.name,chromosome.value,chromosome.prob)
    
    
    def run(self):
        for step in range(self.steps):
            temp_children = []
            #selection
            selected_parents = self.selectPrents()
            #crossover
            for parent_1, parent_2 in selected_parents:
                child = self.crossover(parent_1,parent_2)
                #mutation
                child = self.mutate(child)
                #append to list
                child_value = self.getValue(child)
                #goal check
                if child_value == self.max_fitness:
                    return child
                
                temp_children.append(GeneticAlgorithmNode(name=child,value=child_value))

            self.chromosomes = temp_children
            
        return child
    
    
    def selectParent(self):
        rand_number = random.randint(0,self.total_fitness)
        for chromosome in self.chromosomes:
            if rand_number >= chromosome.interval[0] and rand_number <= chromosome.interval[1]:
                return chromosome

            
    def crossover(self,parent_1,parent_2):
        cross_point = random.randint(0,self.chromosome_length - 1)
        child = parent_1.name[:cross_point] + parent_2.name[cross_point:]
        return child
    
    def mutate(self,child):
        prob = random.uniform(0, 1)
        if prob <= self.mutation_prob:
            rand_index = random.randint(0,self.chromosome_length - 1)
            rand_number = random.randint(0,self.chromosome_length - 1)
            child[rand_index] = rand_number
        
        return child
            
    
    
    

class SimulatedAnnealing(ABC):
    
    def __init__(self,initial_state,goal_state=None,T=10000,coefficient=.999,threshold=.005):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.element = SimulatedAnnealingNode(name=self.initial_state,value=self.getValue(self.initial_state))
        self.T = T
        self.coefficient = coefficient
        self.threshold = threshold
        self.best = self.element
        
    def run(self):
        while(True):
            if self.T < self.threshold or self.checkGoal(self.element):
                return [self.best.name, self.best.value]
            else:
                adjacents = self.getAdjacents(self.element)
                chosen_adjacent = random.choice(adjacents)
                if chosen_adjacent[1] >= self.element.value:
                    self.element = SimulatedAnnealingNode(name=chosen_adjacent[0],value=chosen_adjacent[1])
                else:
                    delta_e = self.element.value - chosen_adjacent[1]
                    try:
                        if random.uniform(0,1) < pow(math.e,(delta_e / self.T)):
                            self.element = SimulatedAnnealingNode(name=chosen_adjacent[0],value=chosen_adjacent[1])
                    except:
                        return [self.best.name, self.best.value]
            
                self.T = self.T * self.coefficient
                
                if self.best.value < self.element.value:
                    self.best = self.element
                
                print(self.T)
                    
            
    @abstractmethod
    def getAdjacents(self,node):
        pass
    
    @abstractmethod
    def getValue(self,node):
        pass

    def checkGoal(self,node):
        pass   





class LocalBeamSearch(ABC,object):
    
    def __init__(self,initial_states=None,goal_state=None,k=1):
        self.k = k
        self.states = []
        self.goal_state = goal_state
        for initial_state in initial_states:
            self.states.append(HillClimbingNode(name=initial_state,value=self.getValue(initial_state)))
        
    def run(self):
        while(True):
            temp_states = []
            temp_all = []
            for state in self.states:
                adjacents = self.getAdjacents(state)
                for adjacent in adjacents:
                    temp_all.append(adjacent)
            max_items = self.findKMaxValue(temp_all)
            for max_item in max_items:
                if not self.checkGoal(max_item):
                    node = HillClimbingNode(name=max_item[0],value=max_item[1])
                    temp_states.append(node)
                else:
                    return [max_item[0], max_item[1]]
                
            self.states = temp_states
                
                
    def findKMaxValue(self,adjacents):
        adjacents.sort(key=lambda x: x[1])
        return adjacents[:self.k]
    
    @abstractmethod
    def getAdjacents(self,node):
        pass
    
    @abstractmethod
    def getValue(self,node):
        pass
    
    def checkGoal(self,node):
        pass
        

