from Problems import *
from Algorithms import *
import math
import random

class RomaniaBFSAgent(BFS):
    
    def __init__(self,initial_state='Arad',goal_state='Bucharest'):
        self.graph = RomaniaProblem.graph
        super().__init__(initial_state=initial_state,goal_state=goal_state)
        
            
    def getAdjacents(self,node):
        temp = []
        adjacents = self.graph[node.name]
        for pair in adjacents:
             temp.append(list(pair.keys())[0])

        return temp


       
class RomaniaDFSAgent(DFS):
    
    def __init__(self,initial_state='Arad',goal_state='Bucharest'):
        self.graph = RomaniaProblem.graph
        super().__init__(initial_state=initial_state,goal_state=goal_state)
        
            
    def getAdjacents(self,node):
        temp = []
        adjacents = self.graph[node.name]
        for pair in adjacents:
             temp.append(list(pair.keys())[0])

        return temp



class RomaniaUCSAgent(UCS):
    
    def __init__(self,initial_state='Arad',goal_state='Bucharest'):
        self.graph = RomaniaProblem.graph
        super().__init__(initial_state=initial_state,goal_state=goal_state)
        
            
    def getAdjacents(self,node):
        temp = []
        adjacents = self.graph[node.name]
        for pair in adjacents:
            name = list(pair.keys())[0]
            g_value = list(pair.values())[0]
            temp.append([name,g_value])
        
        return temp



class RomaniaAStarAgent(AStar):
    
    def __init__(self,initial_state='Arad',goal_state='Bucharest'):
        self.graph = RomaniaProblem.graph
        self.h = RomaniaProblem.defalut_h_values
        initial_state_h_value = self.h[initial_state]
        super().__init__(initial_state_h_value,initial_state=initial_state,goal_state=goal_state)
        
            
    def getAdjacents(self,node):
        temp = []
        adjacents = self.graph[node.name]
        for pair in adjacents:
            name = list(pair.keys())[0]
            g_value = list(pair.values())[0]
            h_value = self.h[list(pair.keys())[0]]
            temp.append([name,g_value,h_value])
        
        return temp



class RomaniaDLSAgent(DLS):
    
    def __init__(self,initial_state='Arad',goal_state='Bucharest',max_depth=0):
        self.graph = RomaniaProblem.graph
        super().__init__(initial_state=initial_state,goal_state=goal_state,max_depth=max_depth)
        
            
    def getAdjacents(self,node):
        temp = []
        adjacents = self.graph[node.name]
        for pair in adjacents:
             temp.append(list(pair.keys())[0])

        return temp



class RomaniaIDSAgent:
    
    def __init__(self,initial_state='Arad',goal_state='Bucharest'):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.depth = 0
        self.romania_dls_agent = None
    
    def run(self):
        while(True):
            self.romania_dls_agent = RomaniaDLSAgent(max_depth=self.depth)
            found_answer = self.romania_dls_agent.run()
            if found_answer:
                return found_answer
            else:
                self.depth += 1














class NQueenBFSAgent(BFS):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenProblem.getAdjacents(node.name)
        return temp
    
    def checkGoal(self,node):
        if None not in node.name:
            return True



class NQueenDFSAgent(DFS):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenProblem.getAdjacents(node.name)
        return temp
    
    def checkGoal(self,node):
        if None not in node.name:
            return True
        else:
            return False





class NQueenHillClimbingAgent(HillClimbing):
    def __init__(self,n=8):
        self.board = NQueenIncrementalProblem.getPlacement(n=n)
        super().__init__(initial_state=self.board,goal_state=None)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenIncrementalProblem.getAdjacents(node.name)
        return temp
    
    def getValue(self,placement):
        return NQueenIncrementalProblem.errorCheck(placement)



class NQueenRRHillClimbingAgent(RRHillClimbing):
    def __init__(self,n=8,steps=1):
        self.n = n
        self.board = NQueenIncrementalProblem.getPlacement(n=self.n)
        super().__init__(steps=steps)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenIncrementalProblem.getAdjacents(node.name)
        return temp
    
    def getValue(self,placement):
        return NQueenIncrementalProblem.errorCheck(placement)
    
    def getInitialState(self):
        return NQueenIncrementalProblem.getPlacement(n=self.n)



class NQueenUCSAgent(UCS):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp_1 = []
        temp_2 = NQueenProblem.getAdjacents(node.name)
        for item in temp_2:
            temp_1.append([item,1])
    
    def checkGoal(self,node):
        if None not in node.name:
            return True
        else:
            return False


class NQueenAStarAgent(AStar):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state_h_value=n,initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp_1 = []
        temp_2 = NQueenProblem.getAdjacents(node.name)
        for item in temp_2:
            temp_1.append([item,1,0])
    
    def checkGoal(self,node):
        if None not in node.name:
            return True
        else:
            return False


class NQueenDLSAgent(DLS):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenProblem.getAdjacents(node.name)
        return temp
    
    def checkGoal(self,node):
        if None not in node.name:
            return True
        else:
            return False
















class EightPuzzleBFSAgent(BFS):
    def __init__(self):
        self.puzzle = EightPuzzleProblem()
        super().__init__(initial_state=self.puzzle.initial_state,goal_state=self.puzzle.goal_state)
    
            
    def getAdjacents(self,node):
        temp = []
        name = node.name
        temp = EightPuzzleProblem.getAdjacents(name)
        return temp



class EightPuzzleDFSAgent(DFS):
    def __init__(self):
        self.puzzle = EightPuzzleProblem()
        super().__init__(initial_state=self.puzzle.initial_state,goal_state=self.puzzle.goal_state)
    
            
    def getAdjacents(self,node):
        temp = []
        name = node.name
        temp = EightPuzzleProblem.getAdjacents(name)
        return temp



class EightPuzzleAStarAgent(AStar):
    
    def __init__(self,initial_state=None,heuristic=None):
        self.heuristic = heuristic
        if initial_state == None:
            self.puzzle = EightPuzzleProblem()
        else:
            self.puzzle = EightPuzzleProblem(initial_state=initial_state) 
        if self.heuristic == None:
            initial_h_value = 0
        elif self.heuristic == 'misplaced':
            initial_h_value = EightPuzzleProblem.misplacedDistance(self.puzzle.initial_state)
        elif self.heuristic == 'manhattan':
            initial_h_value = EightPuzzleProblem.manhattanDistance(self.puzzle.initial_state)
            
        super().__init__(initial_state_h_value=initial_h_value,initial_state=self.puzzle.initial_state,goal_state=self.puzzle.goal_state)
        
            
    def getAdjacents(self,node):
        temp = []
        name = node.name
        adjacents = EightPuzzleProblem.getAdjacents(name)
        if self.heuristic == None:
            for adjacent in adjacents:
                temp.append([adjacent,1,0])
        elif self.heuristic == 'misplaced':
            for adjacent in adjacents:
                misplaced_distance = EightPuzzleProblem.misplacedDistance(adjacent)
                temp.append([adjacent,1,misplaced_distance])
        elif self.heuristic == 'manhattan':
            for adjacent in adjacents:
                manhattan_distance = EightPuzzleProblem.manhattanDistance(adjacent)
                temp.append([adjacent,1,manhattan_distance])
        
        return temp



class EightPuzzleBFSAgent(BFS):
    
    def __init__(self,initial_state=None):
        if initial_state == None:
            self.puzzle = EightPuzzleProblem()
        else:
            self.puzzle = initial_state
        super().__init__(initial_state=self.puzzle.initial_state,goal_state=self.puzzle.goal_state)
    
            
    def getAdjacents(self,node):
        temp = []
        name = node.name
        temp = EightPuzzleProblem.getAdjacents(name)
        return temp



class EightPuzzleDFSAgent(DFS):
    
    def __init__(self,initial_state=None):
        if initial_state == None:
            self.puzzle = EightPuzzleProblem()
        else:
            self.puzzle = initial_state
        super().__init__(initial_state=self.puzzle.initial_state,goal_state=self.puzzle.goal_state)
    
            
    def getAdjacents(self,node):
        temp = []
        name = node.name
        temp = EightPuzzleProblem.getAdjacents(name)
        return temp



class EightPuzzleAStarAgent(AStar):
    
    def __init__(self,initial_state=None,heuristic=None):
        self.heuristic = heuristic
        if initial_state == None:
            self.puzzle = EightPuzzleProblem()
        else:
            self.puzzle = EightPuzzleProblem(initial_state=initial_state) 
        if self.heuristic == None:
            initial_h_value = 0
        elif self.heuristic == 'misplaced':
            initial_h_value = EightPuzzleProblem.misplacedDistance(self.puzzle.initial_state)
        elif self.heuristic == 'manhattan':
            initial_h_value = EightPuzzleProblem.manhattanDistance(self.puzzle.initial_state)
            
        super().__init__(initial_state_h_value=initial_h_value,initial_state=self.puzzle.initial_state,goal_state=self.puzzle.goal_state)
        
            
    def getAdjacents(self,node):
        temp = []
        name = node.name
        adjacents = EightPuzzleProblem.getAdjacents(name)
        if self.heuristic == None:
            for adjacent in adjacents:
                temp.append([adjacent,1,0])
        elif self.heuristic == 'misplaced':
            for adjacent in adjacents:
                misplaced_distance = EightPuzzleProblem.misplacedDistance(adjacent)
                temp.append([adjacent,1,misplaced_distance])
        elif self.heuristic == 'manhattan':
            for adjacent in adjacents:
                manhattan_distance = EightPuzzleProblem.manhattanDistance(adjacent)
                temp.append([adjacent,1,manhattan_distance])
        
        return temp


class MapColoringCSPAgent(CSP):
    
    def __init__(self,map_name,color_count=3,forward_checking=False,arc_consistency=False,mrv_heuristic=False,degree_heuristic=False,lcv_heuristic=False):
        if color_count == 3:
            domain_values = ['red','blue','green']
        elif color_count == 4:
            domain_values = ['red','blue','green','yellow']
            
        graph = MapColoringProblem.graphs[map_name]
        assignments = {}
        domains = {}
        unassigned_vars = 0
        degree_of_unassigned_vars = {}
        for key, adjacents in graph.items(): 
            domains[key] = copy.deepcopy(domain_values)
            assignments[key] = None
            degree_of_unassigned_vars[key] = len(adjacents)
            unassigned_vars += 1
        
        initial_state = CSPNode(assignments,domains,degree_of_unassigned_vars,unassigned_vars)
        super().__init__(graph,initial_state,len(domain_values),forward_checking=False,MRV_heuristic=mrv_heuristic,degree_heuristic=degree_heuristic,arc_consistency=arc_consistency,lcv_heuristic=lcv_heuristic)



class SudokuCSPAgent(CSP):
    
    def __init__(self,initial_state,forward_checking=False,arc_consistency=False,mrv_heuristic=False,degree_heuristic=False,lcv_heuristic=False):     
        self.graph = self.makeGraph()
        assignments = {}
        domains = {}
        unassigned_vars = 0
        degree_of_unassigned_vars = {}
        
        for key, value in self.graph.items():
            degree_of_unassigned_vars[key] = 0
        
        for i in range(9):
            for j in range(9):
                if initial_state[i][j] != 'X':
                    assignments['A_' + str(i) + str(j)] = initial_state[i][j]
                else:
                    assignments['A_' + str(i) + str(j)] = None
                    unassigned_vars += 1
                    for adjacent in self.graph['A_' + str(i) + str(j)]:
                        degree_of_unassigned_vars[adjacent] += 1

        temp = self.findDomains(initial_state)
        for i in range(9):
            for j in range(9):
                domains['A_' + str(i) + str(j)] = temp[i][j]
        

        initial_state_new = CSPNode(assignments,domains,degree_of_unassigned_vars,unassigned_vars)
        super().__init__(self.graph,initial_state_new,9,forward_checking=False,MRV_heuristic=mrv_heuristic,degree_heuristic=degree_heuristic,arc_consistency=arc_consistency,lcv_heuristic=lcv_heuristic) 
        
        
        
    def findDomains(self,initial_state):
        not_in_domains = [[[] for j in range(9)] for i in range(9)]
        domains = [[[] for j in range(9)] for i in range(9)]
        row_domains = [[] for i in range(9)]
        col_domains = [[] for i in range(9)]
        subtable_domains = [[[] for j in range(3)] for i in range(3)]
            
        for i in range(9):
            for j in range(9):
                subtable_row = i // 3
                subtable_col = j // 3
                if initial_state[i][j] != 'X':
                    row_domains[i].append(initial_state[i][j])
                    col_domains[j].append(initial_state[i][j])
                    subtable_domains[subtable_row][subtable_col].append(initial_state[i][j])
                            
        for i in range(9):
            for j in range(9):
                if initial_state[i][j] == 'X':
                    subtable_row = i // 3
                    subtable_col = j // 3
                    temp = (list(set().union(row_domains[i],col_domains[j],subtable_domains[subtable_row][subtable_col])))
                    not_in_domains[i][j] = temp
                else:
                    domains[i][j].append(initial_state[i][j])
        
        for i in range(9):
            for j in range(9):
                if initial_state[i][j] == 'X':
                    for value in range(1,10):
                        if value not in not_in_domains[i][j]:
                            domains[i][j].append(value)
                            
        return domains
                            
    
    def makeGraph(self):
        graph = {}
        for i in range(9):
            for j in range(9):
                graph['A_' + str(i) + str(j)] = []

        for i in range(9):
            for j in range(9):
                index = 'A_' + str(i) + str(j)
                subtable_row = i // 3
                subtable_col = j // 3

                for row in range(9):
                    if i != row:
                        graph[index].append('A_' + str(row) + str(j))

                for col in range(9):
                    if j != col:
                        graph[index].append('A_' + str(i) + str(col))
                
                subtable_row = subtable_row * 3
                subtable_col = subtable_col * 3
                for k in range(subtable_row,subtable_row + 3):
                    for t in range(subtable_col,subtable_col + 3):
                        if i != k or j != t:
                            if 'A_' + str(k) + str(t) not in graph[index]:
                                graph[index].append('A_' + str(k) + str(t))
                                
        return graph




class NQueenLocalBeamAgent(LocalBeamSearch):
    def __init__(self,n=8,k=1):
        temp_board = []
        for i in range(k):
            board = NQueenIncrementalProblem.getPlacement(n=n)
            temp_board.append(board)
        super().__init__(initial_states=temp_board,goal_state=None,k=k)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenIncrementalProblem.getAdjacents(node.name)
        return temp
    
    def getValue(self,placement):
        return NQueenIncrementalProblem.errorCheck(placement)
    
    def checkGoal(self,array):
        if array[1] != 0:
            return False
        else:
            return True



class NQueenGeneticAlgorithmAgent(GenticAlgorithm):
    def __init__(self,n,population,steps=10,mutation_prob=.2):
        temp_board = []
        self.population = population
        self.n = n
        self.max_error = ((self.n) * (self.n - 1)) / 2
        
        for i in range(self.population):
            board = NQueenIncrementalProblem.getPlacement(n=n)
            temp_board.append(board)
        super().__init__(initial_chromosomes=temp_board,max_fitness=self.max_error,steps=steps,mutation_prob=mutation_prob)
            
    
    def getValue(self,placement):
        n_error = NQueenIncrementalProblem.errorCheck(placement)
        return self.max_error - n_error
    
    


class NQueenSimulatedAnnealingAgent(SimulatedAnnealing):
    def __init__(self,n=8,T=1000,coefficient=.999,threshold=.005):
        self.board = NQueenIncrementalProblem.getPlacement(n=n)
        self.n = n
        self.max_error = (n * (n - 1)) / 2
        super().__init__(initial_state=self.board,goal_state=None,T=T,coefficient=coefficient,threshold=threshold)
        
    def getAdjacents(self,node):
        temp = []
        temp = NQueenIncrementalProblem.getAdjacents(node.name)
        return temp
    
    def getValue(self,placement):
        return self.max_error - NQueenIncrementalProblem.errorCheck(placement)
