import copy
import random


class RomaniaProblem(object):
            
            graph = {'Arad' : [{'Zerind':75},{'Timisoara':118},{'Sibiu':140}],
                     'Zerind' : [{'Orada':71},{'Arad':75}],
                     'Orada' : [{'Zerind':71},{'Sibiu':151}],
                     'Timisoara' : [{'Arad':118},{'Lugoj':111}],
                     'Lugoj' : [{'Timisoara':111},{'Mehadia':70}],
                     'Mehadia' : [{'Lugoj':70},{'Drobeta':75}],
                     'Drobeta' : [{'Mehadia':75},{'Craiova':120}],
                     'Craiova' : [{'Drobeta':120},{'Rimnicu':146},{'Pitesti':138}],
                     'Sibiu' : [{'Orada':151},{'Arad':140},{'Rimnicu':80},{'Fagaras':99}],
                     'Rimnicu' : [{'Sibiu':80},{'Craiova':146},{'Pitesti':97}],
                     'Pitesti' : [{'Rimnicu':97},{'Craiova':138},{'Bucharest':101}],
                     'Fagaras' : [{'Sibiu':99},{'Bucharest':211}],
                     'Giurgiu' : [{'Bucharest':90}],
                     'Bucharest' : [{'Pitesti':101},{'Giurgiu':90},{'Urziceni':85}],
                     'Urziceni' : [{'Bucharest':85},{'Hirsova':98},{'Vaslui':142}],
                     'Hirsova' : [{'Urziceni':98},{'Erfoie':86}],
                     'Erfoie' : [{'Hirsova':86}],
                     'Vaslui' : [{'Urziceni':142},{'Iasi':92}],
                     'Iasi' : [{'Vaslui':92},{'Neamt':87}],
                     'Neamt' : [{'Iasi':87}]
                    }
            
            defalut_h_values = {
                'Arad':366,
                'Timisoara':329,
                'Sibiu':253,
                'Zerind':374,
                'Lugoj':244,
                'Rimnicu':193,
                'Fagaras':178,
                'Orada':380,
                'Mehadia':241,
                'Craiova':160,
                'Pitesti':98,
                'Bucharest':0,
                'Drobeta':242,
                'Giurgiu':77,
                'Urziceni':80,
                'Hirsova':151,
                'Erfoie':161,
                'Vaslui':199,
                'Iasi':226,
                'Neamt':234
            }


class NQueenProblem:
    
    def __init__(self,n = 8):
        self.n = n
        self.placement = [None] * n
    
    @staticmethod
    def getAdjacents(placement):
        adjacent_array = []
        temp = []
        array_length = len(placement)
        for i, value in enumerate(placement):
            if value == None:
                first_none = i
                break
                
        placement_temp = copy.deepcopy(placement)
        for j in range(array_length):
            placement_temp[first_none] = j
            if NQueenProblem.errorCheck(placement_temp,first_none):
                temp.append(j)
        
        for value in temp:
            placement_copy = copy.deepcopy(placement)
            placement_copy[first_none] = value
            adjacent_array.append(placement_copy)
        
        return adjacent_array
    
    @staticmethod
    def errorCheck(array,first_none):
        for i in range(first_none):
            if abs(i - first_none) == abs(array[i] - array[first_none]) or array[i] == array[first_none]:
                return False
        return True
    
            
    
class EightPuzzleProblem:
    goal_state = [
            [1,2,3],
            [4,5,6],
            [7,8,'X']
        ]
    def __init__(self,initial_state=None):
        if initial_state == None:
            initial_state = [1,2,3,4,5,6,7,8,'X']
            random.shuffle(initial_state)
            initial_state_new = [['X','X','X'],['X','X','X'],['X','X','X']]
            k = 0
            for i in range(3):
                for j in range(3):
                    initial_state_new[i][j] = initial_state[i*3+j]
                    k += 1
            self.initial_state = initial_state_new
        else:
            self.initial_state = initial_state
        self.goal_state = EightPuzzleProblem.goal_state
    
    @staticmethod
    def getIndex(grid,value):
        for i in range(3):
            for j in range(3):
                if grid[i][j] == value:
                    return i,j
    
    
    @staticmethod
    def getAdjacents(grid):
        temp_array = []
        index_i, index_j = EightPuzzleProblem.getIndex(grid,'X')
        
        if index_j == 0:
            temp_grid = copy.deepcopy(grid)
            temp = temp_grid[index_i][index_j + 1]
            temp_grid[index_i][index_j + 1] = 'X'
            temp_grid[index_i][index_j] = temp
            temp_array.append(temp_grid)
        
        elif index_j == 2:
            temp_grid = copy.deepcopy(grid)
            temp = temp_grid[index_i][index_j - 1]
            temp_grid[index_i][index_j - 1] = 'X'
            temp_grid[index_i][index_j] = temp
            temp_array.append(temp_grid)
            
        else:
            temp_grid = copy.deepcopy(grid)
            temp = temp_grid[index_i][index_j + 1]
            temp_grid[index_i][index_j + 1] = 'X'
            temp_grid[index_i][index_j] = temp
            temp_array.append(temp_grid)
            
            temp_grid = copy.deepcopy(grid)
            temp = temp_grid[index_i][index_j - 1]
            temp_grid[index_i][index_j - 1] = 'X'
            temp_grid[index_i][index_j] = temp
            temp_array.append(temp_grid)

        if index_i == 0:
            temp_grid = copy.deepcopy(grid)
            temp = temp_grid[index_i + 1][index_j]
            temp_grid[index_i + 1][index_j] = 'X'
            temp_grid[index_i][index_j] = temp
            temp_array.append(temp_grid)

        elif index_i == 2:
            temp_grid = copy.deepcopy(grid)
            temp = temp_grid[index_i - 1][index_j]
            temp_grid[index_i - 1][index_j] = 'X'
            temp_grid[index_i][index_j] = temp
            temp_array.append(temp_grid)
            
        else:
            temp_grid = copy.deepcopy(grid)
            temp = temp_grid[index_i + 1][index_j]
            temp_grid[index_i + 1][index_j] = 'X'
            temp_grid[index_i][index_j] = temp
            temp_array.append(temp_grid)
            
            temp_grid = copy.deepcopy(grid)
            temp = temp_grid[index_i - 1][index_j]
            temp_grid[index_i - 1][index_j] = 'X'
            temp_grid[index_i][index_j] = temp
            temp_array.append(temp_grid)
            
        return temp_array
    
    @staticmethod
    def manhattanDistance(grid):
        manhattan_distance = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] != 'X':
                    x = (grid[i][j] - 1) // 3
                    y = (grid[i][j] - 1) % 3
                    manhattan_distance += abs(x - i) + abs(y - j) 
        return manhattan_distance
    
    @staticmethod
    def misplacedDistance(grid):
        misplaced_distance = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] != 'X':
                    x = (grid[i][j] - 1) // 3
                    y = (grid[i][j] - 1) % 3
                    if i != x or j != y:
                        misplaced_distance += 1
        return misplaced_distance


class NQueenIncrementalProblem:
    
    @staticmethod
    def getPlacement(n=8):
        placement = list(range(n))
        random.shuffle(placement)
        return placement
    
    @staticmethod
    def errorCheck(array):
        n_error = 0
        array_length = len(array)
        for i in range(0,array_length):
            for j in range(i+1,array_length):
                if abs(i - j) == abs(array[i] - array[j]) or array[i] == array[j]:
                    n_error += 1
        
        return n_error
    
    @staticmethod
    def getAdjacents(array):
        temp = []
        array_length = len(array)
        
        for i in range(array_length):
            for j in range(array_length):
                if j == array[i]:
                    continue
                else:
                    temp_array = copy.deepcopy(array)
                    temp_array[i] = j
                    n_error = NQueenIncrementalProblem.errorCheck(temp_array)
                    temp.append([temp_array,n_error])
                    
        return temp


class MapColoringProblem:
    
    graphs = {
        'iran' : {'IR-01': ['IR-03', 'IR-11', 'IR-02'],
'IR-02': ['IR-01', 'IR-11', 'IR-16'],
'IR-03': ['IR-01', 'IR-11', 'IR-19'],
'IR-04': ['IR-25','IR-14','IR-18','IR-08','IR-10','IR-20','IR-22','IR-26','IR-12'],
'IR-05': ['IR-17', 'IR-20', 'IR-10'],
'IR-06': ['IR-10', 'IR-18', 'IR-14', 'IR-23'],
'IR-07': ['IR-21', 'IR-12', 'IR-26', 'IR-22', 'IR-32'],
'IR-08': ['IR-10', 'IR-04', 'IR-18'],
'IR-10': ['IR-05', 'IR-20', 'IR-04', 'IR-08', 'IR-18', 'IR-06'],
'IR-11': ['IR-02', 'IR-01', 'IR-03', 'IR-19', 'IR-28', 'IR-24', 'IR-16'],
'IR-12': ['IR-30','IR-31','IR-27','IR-21','IR-07','IR-26','IR-04','IR-25'],
'IR-13': ['IR-23', 'IR-15', 'IR-29'],
'IR-14': ['IR-06', 'IR-23', 'IR-15', 'IR-25', 'IR-04', 'IR-18'],
'IR-15': ['IR-23', 'IR-13', 'IR-14', 'IR-25', 'IR-29'],
'IR-16': ['IR-02', 'IR-11', 'IR-24', 'IR-17'],
'IR-17': ['IR-16', 'IR-24', 'IR-20', 'IR-05'],
'IR-18': ['IR-06', 'IR-14', 'IR-10', 'IR-08', 'IR-04'],
'IR-19': ['IR-03', 'IR-11', 'IR-28', 'IR-21'],
'IR-20': ['IR-05', 'IR-17', 'IR-24', 'IR-22', 'IR-04', 'IR-10'],
'IR-21': ['IR-19', 'IR-28', 'IR-32', 'IR-07', 'IR-12', 'IR-27'],
'IR-22': ['IR-26', 'IR-04', 'IR-20', 'IR-24', 'IR-28', 'IR-32', 'IR-07'],
'IR-23': ['IR-06', 'IR-14', 'IR-15', 'IR-13'],
'IR-24': ['IR-20', 'IR-17', 'IR-16', 'IR-11', 'IR-28', 'IR-22'],
'IR-25': ['IR-29', 'IR-15', 'IR-14', 'IR-04', 'IR-12', 'IR-30'],
'IR-26': ['IR-07', 'IR-12', 'IR-04', 'IR-22'],
'IR-27': ['IR-21', 'IR-12', 'IR-31'],
'IR-28': ['IR-11', 'IR-19', 'IR-21', 'IR-32', 'IR-22', 'IR-24'],
'IR-29': ['IR-13', 'IR-15', 'IR-25', 'IR-30'],
'IR-30': ['IR-31', 'IR-12', 'IR-25', 'IR-29'],
'IR-31': ['IR-30', 'IR-12', 'IR-27'],
'IR-32': ['IR-21', 'IR-07', 'IR-22', 'IR-28']},
        'france' : {"FR-HDF":["FR-NOR","FR-IDF","FR-GES"],"FR-COR":[],"FR-NOR":["FR-HDF","FR-IDF","FR-CVL","FR-PDL","FR-BRE"],"FR-BRE":["FR-NOR","FR-PDL"],"FR-PDL":["FR-BRE","FR-NOR","FR-CVL","FR-NAQ"],"FR-NAQ":["FR-PDL","FR-CVL","FR-ARA","FR-OCC"],"FR-OCC":["FR-NAQ","FR-ARA","FR-PAC"],"FR-PAC":["FR-OCC","FR-ARA"],"FR-ARA":["FR-PAC","FR-OCC","FR-NAQ","FR-CVL","FR-BFC"],"FR-CVL":["FR-NOR","FR-PDL","FR-NAQ","FR-ARA","FR-BFC","FR-IDF"],"FR-BFC":["FR-CVL","FR-ARA","FR-IDF","FR-GES"],"FR-GES":["FR-IDF","FR-HDF","FR-BFC"],"FR-IDF":["FR-HDF","FR-GES","FR-BFC","FR-CVL","FR-NOR"]},
        'germany' : {'DE-BB': ['DE-BE', 'DE-MV', 'DE-ST', 'DE-SN'],
'DE-BE': ['DE-BB'],
'DE-BW': ['DE-BY', 'DE-HE', 'DE-RP'],
'DE-BY': ['DE-BW', 'DE-HE', 'DE-TH', 'DE-SN'],
'DE-HB': ['DE-NI'],
'DE-HE': ['DE-BY', 'DE-BW', 'DE-RP', 'DE-NW', 'DE-NI', 'DE-TH'],
'DE-HH': ['DE-SH', 'DE-NI'],
'DE-MV': ['DE-SH', 'DE-NI', 'DE-BB'],
'DE-NI': ['DE-HB',
 'DE-HH',
 'DE-SH',
 'DE-MV',
 'DE-BB',
 'DE-ST',
 'DE-TH',
 'DE-HE',
 'DE-NW'],
'DE-NW': ['DE-NI', 'DE-HE', 'DE-RP'],
'DE-RP': ['DE-SL', 'DE-NW', 'DE-HE', 'DE-BW'],
'DE-SH': ['DE-MV', 'DE-HH', 'DE-NI'],
'DE-SL': ['DE-RP'],
'DE-SN': ['DE-BY', 'DE-TH', 'DE-ST', 'DE-BB'],
'DE-ST': ['DE-NI', 'DE-BB', 'DE-SN', 'DE-TH'],
'DE-TH': ['DE-NI', 'DE-ST', 'DE-SN', 'DE-BY', 'DE-HE']},
        'usa' : {"US-WA":["US-ID","US-OR"],"US-OR":["US-CA","US-NV","US-ID","US-WA"],"US-CA":["US-AZ","US-NV","US-OR"],"US-ID":["US-NV","US-OR","US-WA","US-MT","US-WY","US-UT"],"US-ME":["US-NH"],"US-NH":["US-MA","US-ME","US-VT"],"US-MA":["US-RI","US-CT","US-NY","US-VT","US-NH"],"US-VT":["US-NH","US-MA","US-NY"],"US-RI":["US-MA","US-CT"],"US-CT":["US-NY","US-RI","US-MA"],"US-NY":["US-NJ","US-PA","US-CT","US-MA","US-VT"],"US-NJ":["US-PA","US-NY","US-DE"],"US-DE":["US-MD","US-PA","US-NJ"],"US-PA":["US-DE","US-NJ","US-MD","US-WV","US-OH","US-NY"],"US-MD":["US-DE","US-PA","US-WV","US-VA"],"US-VA":["US-WV","US-MD","US-NC","US-TN","US-KY"],"US-NC":["US-SC","US-TN","US-VA","US-GA"],"US-SC":["US-GA","US-NC"],"US-GA":["US-SC","US-NC","US-TN","US-AL","US-FL"],"US-FL":["US-GA","US-AL"],"US-AL":["US-GA","US-FL","US-MS","US-TN"],"US-MS":["US-AL","US-TN","US-AR","US-LA"],"US-LA":["US-MS","US-AR","US-TX"],"US-TX":["US-LA","US-AR","US-OK","US-NM"],"US-NM":["US-TX","US-OK","US-CO","US-AZ"],"US-AZ":["US-NM","US-UT","US-NV","US-CA"],"US-NV":["US-AZ","US-UT","US-ID","US-OR","US-CA"],"US-UT":["US-AZ","US-NV","US-ID","US-WY","US-CO"],"US-MT":["US-ID","US-WY","US-SD","US-ND"],"US-WY":["US-CO","US-UT","US-ID","US-MT","US-SD","US-NE"],"US-ND":["US-SD","US-MT","US-MN"],"US-MN":["US-IA","US-SD","US-ND","US-WI"],"US-SD":["US-IA","US-NE","US-WY","US-MT","US-ND","US-MN"],"US-MI":["US-WI","US-IN","US-OH"],"US-OH":["US-PA","US-WV","US-KY","US-IN","US-MI"],"US-WI":["US-MI","US-IL","US-IA","US-MN"],"US-CO":["US-NM","US-UT","US-WY","US-NE","US-KS","US-OK"],"US-NE":["US-SD","US-WY","US-CO","US-KS","US-MO","US-IA"],"US-IA":["US-MO","US-NE","US-SD","US-MN","US-WI","US-IL"],"US-KS":["US-CO","US-NE","US-MO","US-OK"],"US-OK":["US-TX","US-NM","US-CO","US-KS","US-AR","US-MO"],"US-AR":["US-MS","US-LA","US-TX","US-OK","US-MO","US-TN"],"US-MO":["US-AR","US-OK","US-KS","US-NE","US-IA","US-IL","US-KY","US-TN"],"US-TN":["US-NC","US-GA","US-AL","US-MS","US-AR","US-MO","US-KY","US-VA"],"US-IL":["US-MO","US-IA","US-WI","US-IN","US-KY"],"US-IN":["US-OH","US-MI","US-IL","US-KY"],"US-KY":["US-TN","US-MO","US-IL","US-IN","US-OH","US-WV","US-VA"],"US-WV":["US-VA","US-KY","US-OH","US-PA","US-MD"],"US-AK":[],"US-HI":[],"PR":[],"VI":[],"AS":[],"GU":[],"MP":[]}
,
        'russia' : {'RU-AL': ['RU-TY', 'RU-KK', 'RU-KEM', 'RU-ALT'],
 'RU-ALT': ['RU-AL', 'RU-KEM', 'RU-NVS'],
 'RU-AMU': ['RU-YEV', 'RU-KHA', 'RU-SA', 'RU-ZAB'],
 'RU-ARK': ['RU-KO', 'RU-NEN', 'RU-KR', 'RU-VLG', 'RU-KIR'],
 'RU-AST': ['RU-VGG', 'RU-KL'],
 'RU-BA': ['RU-CHE', 'RU-ORE', 'RU-SVE', 'RU-PER', 'RU-UD', 'RU-TA'],
 'RU-BEL': ['RU-KRS', 'RU-VOR'],
 'RU-BRY': ['RU-SMO', 'RU-KLU', 'RU-ORL', 'RU-KRS'],
 'RU-BU': ['RU-ZAB', 'RU-IRK', 'RU-TY'],
 'RU-CE': ['RU-IN', 'RU-SE', 'RU-STA', 'RU-DA'],
 'RU-CHE': ['RU-KGN', 'RU-SVE', 'RU-BA', 'RU-ORE'],
 'RU-CHU': ['RU-KAM', 'RU-MAG', 'RU-SA'],
 'RU-CU': ['RU-ME', 'RU-TA', 'RU-ULY', 'RU-MO', 'RU-NIZ'],
 'RU-DA': ['RU-CE', 'RU-STA', 'RU-KL'],
 'RU-IN': ['RU-SE', 'RU-CE'],
 'RU-IRK': ['RU-KYA', 'RU-SA', 'RU-ZAB', 'RU-BU', 'RU-TY'],
 'RU-IVA': ['RU-YAR', 'RU-KOS', 'RU-NIZ', 'RU-VLA'],
 'RU-KAM': ['RU-CHU', 'RU-MAG'],
 'RU-KB': ['RU-SE', 'RU-STA', 'RU-KC'],
 'RU-KC': ['RU-KB', 'RU-STA', 'RU-KDA'],
 'RU-KDA': ['RU-KC', 'RU-STA', 'RU-ROS'],
 'RU-KEM': ['RU-KK', 'RU-KYA', 'RU-TOM', 'RU-NVS', 'RU-ALT', 'RU-AL'],
 'RU-KGN': ['RU-TYU', 'RU-SVE', 'RU-CHE'],
 'RU-KHA': ['RU-MAG', 'RU-SA', 'RU-AMU', 'RU-YEV', 'RU-PRI'],
 'RU-KHM': ['RU-YAN', 'RU-KYA', 'RU-TOM', 'RU-TYU', 'RU-SVE', 'RU-KO'],
 'RU-KIR': ['RU-UD',
  'RU-PER',
  'RU-KO',
  'RU-ARK',
  'RU-VLG',
  'RU-KOS',
  'RU-NIZ',
  'RU-ME',
  'RU-TA'],
 'RU-KK': ['RU-TY', 'RU-AL', 'RU-KEM', 'RU-KYA'],
 'RU-KL': ['RU-AST', 'RU-VGG', 'RU-ROS', 'RU-STA', 'RU-DA'],
 'RU-KLU': ['RU-MOW', 'RU-MOS', 'RU-SMO', 'RU-BRY', 'RU-ORL', 'RU-TUL'],
 'RU-KO': ['RU-NEN',
  'RU-YAN',
  'RU-KHM',
  'RU-SVE',
  'RU-PER',
  'RU-KIR',
  'RU-ARK'],
 'RU-KOS': ['RU-VLG', 'RU-KIR', 'RU-NIZ', 'RU-IVA', 'RU-YAR'],
 'RU-KR': ['RU-MUR', 'RU-ARK', 'RU-VLG', 'RU-LEN'],
 'RU-KRS': ['RU-BRY', 'RU-ORL', 'RU-BEL', 'RU-VOR', 'RU-LIP'],
 'RU-KYA': ['RU-SA',
  'RU-IRK',
  'RU-TY',
  'RU-KK',
  'RU-KEM',
  'RU-TOM',
  'RU-KHM',
  'RU-YAN'],
 'RU-LEN': ['RU-KR', 'RU-VLG', 'RU-NGR', 'RU-PSK'],
 'RU-LIP': ['RU-ORL', 'RU-TUL', 'RU-RYA', 'RU-TAM', 'RU-VOR', 'RU-KRS'],
 'RU-MAG': ['RU-KAM', 'RU-CHU', 'RU-SA', 'RU-KHA'],
 'RU-ME': ['RU-KIR', 'RU-TA', 'RU-CU', 'RU-NIZ'],
 'RU-MO': ['RU-NIZ', 'RU-CU', 'RU-ULY', 'RU-PNZ', 'RU-RYA'],
 'RU-MOS': ['RU-TVE',
  'RU-VLA',
  'RU-RYA',
  'RU-TUL',
  'RU-KLU',
  'RU-MOW',
  'RU-SMO'],
 'RU-MOW': ['RU-KLU', 'RU-MOS'],
 'RU-MUR': ['RU-KR'],
 'RU-NEN': ['RU-YAN', 'RU-KO', 'RU-ARK'],
 'RU-NGR': ['RU-LEN', 'RU-VLG', 'RU-TVE', 'RU-PSK'],
 'RU-NIZ': ['RU-ME',
  'RU-KIR',
  'RU-KOS',
  'RU-IVA',
  'RU-VLA',
  'RU-RYA',
  'RU-MO',
  'RU-CU'],
 'RU-NVS': ['RU-ALT', 'RU-KEM', 'RU-TOM', 'RU-OMS'],
 'RU-OMS': ['RU-NVS', 'RU-TOM', 'RU-TYU'],
 'RU-ORE': ['RU-CHE', 'RU-BA', 'RU-TA', 'RU-SAM'],
 'RU-ORL': ['RU-BRY', 'RU-KLU', 'RU-TUL', 'RU-LIP', 'RU-KRS'],
 'RU-PER': ['RU-SVE', 'RU-KO', 'RU-KIR', 'RU-UD', 'RU-BA'],
 'RU-PNZ': ['RU-MO', 'RU-ULY', 'RU-SAR', 'RU-TAM', 'RU-RYA'],
 'RU-PRI': ['RU-KHA'],
 'RU-PSK': ['RU-LEN', 'RU-NGR', 'RU-TVE', 'RU-SMO'],
 'RU-ROS': ['RU-VOR', 'RU-VGG', 'RU-KL', 'RU-KDA', 'RU-STA'],
 'RU-RYA': ['RU-MOS',
  'RU-VLA',
  'RU-NIZ',
  'RU-MO',
  'RU-PNZ',
  'RU-TAM',
  'RU-LIP',
  'RU-TUL'],
 'RU-SA': ['RU-CHU',
  'RU-MAG',
  'RU-KHA',
  'RU-AMU',
  'RU-ZAB',
  'RU-IRK',
  'RU-KYA'],
 'RU-SAK': [],
 'RU-SAM': ['RU-ORE', 'RU-TA', 'RU-ULY', 'RU-SAR'],
 'RU-SAR': ['RU-SAM', 'RU-ULY', 'RU-PNZ', 'RU-TAM', 'RU-VOR', 'RU-VGG'],
 'RU-SE': ['RU-KB', 'RU-IN', 'RU-STA'],
 'RU-SMO': ['RU-PSK', 'RU-TVE', 'RU-MOS', 'RU-KLU', 'RU-BRY'],
 'RU-STA': ['RU-SE',
  'RU-KB',
  'RU-KC',
  'RU-KDA',
  'RU-ROS',
  'RU-KL',
  'RU-DA',
  'RU-CE'],
 'RU-SVE': ['RU-KHM',
  'RU-TYU',
  'RU-KGN',
  'RU-CHE',
  'RU-BA',
  'RU-PER',
  'RU-KO'],
 'RU-TA': ['RU-BA',
  'RU-ORE',
  'RU-SAM',
  'RU-ULY',
  'RU-CU',
  'RU-ME',
  'RU-KIR',
  'RU-UD'],
 'RU-TAM': ['RU-RYA', 'RU-PNZ', 'RU-SAR', 'RU-VOR', 'RU-LIP'],
 'RU-TOM': ['RU-KYA', 'RU-KEM', 'RU-NVS', 'RU-OMS', 'RU-TYU', 'RU-KHM'],
 'RU-TUL': ['RU-KLU', 'RU-MOS', 'RU-RYA', 'RU-LIP', 'RU-ORL'],
 'RU-TVE': ['RU-PSK',
  'RU-NGR',
  'RU-VLG',
  'RU-YAR',
  'RU-SMO',
  'RU-MOS'],
 'RU-TY': ['RU-BU', 'RU-IRK', 'RU-KYA', 'RU-KK', 'RU-AL'],
 'RU-TYU': ['RU-OMS', 'RU-KHM', 'RU-SVE', 'RU-KGN'],
 'RU-UD': ['RU-PER', 'RU-KIR', 'RU-TA', 'RU-BA'],
 'RU-ULY': ['RU-SAM', 'RU-SAR', 'RU-PNZ', 'RU-MO', 'RU-CU', 'RU-TA'],
 'RU-VGG': ['RU-AST', 'RU-KL', 'RU-ROS', 'RU-VOR', 'RU-SAR'],
 'RU-VLA': ['RU-MOS', 'RU-YAR', 'RU-IVA', 'RU-NIZ', 'RU-RYA'],
 'RU-VLG': ['RU-ARK',
  'RU-KIR',
  'RU-KOS',
  'RU-YAR',
  'RU-TVE',
  'RU-NGR',
  'RU-LEN',
  'RU-KR'],
 'RU-VOR': ['RU-BEL',
  'RU-KRS',
  'RU-LIP',
  'RU-TAM',
  'RU-SAR',
  'RU-VGG',
  'RU-ROS'],
 'RU-YAN': ['RU-KYA', 'RU-KHM', 'RU-KO', 'RU-NEN'],
 'RU-YAR': ['RU-VLG', 'RU-KOS', 'RU-IVA', 'RU-VLA', 'RU-MOS', 'RU-TVE'],
 'RU-YEV': ['RU-KHA', 'RU-AMU'],
 'RU-ZAB': ['RU-AMU', 'RU-SA', 'RU-IRK', 'RU-BU']},
        'china' : {"CN-65":["CN-54","CN-63","CN-62"],"CN-54":["CN-65","CN-63","CN-51","CN-53"],"CN-62":["CN-65","CN-63","CN-51","CN-61","CN-64","CN-15"],"CN-63":["CN-54","CN-65","CN-62","CN-51"],"CN-53":["CN-54","CN-51","CN-52","CN-45"],"CN-46":[],"CN-71":[],"CN-51":["CN-54","CN-63","CN-62","CN-61","CN-50","CN-52","CN-53"],"CN-45":["CN-53","CN-52","CN-43","CN-44"],"CN-44":["CN-45","CN-43","CN-36","CN-35"],"CN-52":["CN-45","CN-53","CN-51","CN-50","CN-43"],"CN-35":["CN-44","CN-36","CN-33"],"CN-36":["CN-35","CN-44","CN-43","CN-42","CN-34","CN-33"],"CN-43":["CN-44","CN-45","CN-52","CN-50","CN-42","CN-36"],"CN-33":["CN-35","CN-36","CN-34","CN-32","CN-31"],"CN-31":["CN-33","CN-32"],"CN-32":["CN-33","CN-31","CN-34","CN-37"],"CN-34":["CN-32","CN-33","CN-36","CN-42","CN-41","CN-37"],"CN-50":["CN-52","CN-51","CN-61","CN-42","CN-43"],"CN-15":["CN-62","CN-64","CN-61","CN-14","CN-13","CN-21","CN-22","CN-23"],"CN-64":["CN-15","CN-62","CN-61"],"CN-37":["CN-32","CN-34","CN-41","CN-13"],"CN-42":["CN-34","CN-36","CN-43","CN-50","CN-61","CN-41"],"CN-61":["CN-62","CN-64","CN-15","CN-14","CN-41","CN-42","CN-50","CN-51"],"CN-41":["CN-37","CN-34","CN-42","CN-61","CN-14","CN-13"],"CN-14":["CN-15","CN-61","CN-41","CN-13"],"CN-11":["CN-13","CN-12"],"CN-13":["CN-11","CN-12","CN-37","CN-41","CN-14","CN-15","CN-21"],"CN-12":["CN-13","CN-11"],"CN-21":["CN-13","CN-15","CN-22"],"CN-23":["CN-15","CN-22"],"CN-22":["CN-21","CN-15","CN-23"]},
        'uk' : {"GB-CO":["GB-DV"],"GB-DV":["GB-CO","GB-SM","GB-DS"],"GB-SM":["GB-DV","GB-DS","GB-WL","GB-GC"],"GB-DS":["GB-DV","GB-SM","GB-WL","GB-HA"],"GB-WL":["GB-DS","GB-SM","GB-GC","GB-OX","GB-BK","GB-HA"],"GB-HA":["GB-DS","GB-WL","GB-BK","GB-SR","GB-SX"],"GB-SX":["GB-HA","GB-SR","GB-KE"],"GB-KE":["GB-SX","GB-SR","GB-GL","GB-EX"],"GB-SR":["GB-SX","GB-HA","GB-BK","GB-GL","GB-KE"],"GB-GL":["GB-KE","GB-SR","GB-BK","GB-BU","GB-HT","GB-EX"],"GB-BK":["GB-SR","GB-GL","GB-BU","GB-OX","GB-WL","GB-HA"],"GB-EX":["GB-KE","GB-GL","GB-HT","GB-CM","GB-SF"],"GB-SF":["GB-EX","GB-CM","GB-NF"],"GB-NF":["GB-SF","GB-CM","GB-LI"],"GB-CM":["GB-SF","GB-EX","GB-HT","GB-BD","GB-NA","GB-LI","GB-NF"],"GB-HT":["GB-EX","GB-GL","GB-BU","GB-BD","GB-CM"],"GB-BU":["GB-HT","GB-GL","GB-BK","GB-OX","GB-NA","GB-BD"],"GB-BD":["GB-HT","GB-BU","GB-NA","GB-CM"],"GB-GC":["GB-WL","GB-SM","GB-OX","GB-WR","GB-WO","GB-HD","GB-WA"],"GB-LI":["GB-NF","GB-CM","GB-RT","GB-NA","GB-LE","GB-NT","GB-YK"],"IE":["GB-NI"],"GB-NI":["IE"],"GB-OX":["GB-BK","GB-WL","GB-GC","GB-WR","GB-NA","GB-BU"],"GB-NA":["GB-CM","GB-BD","GB-BU","GB-OX","GB-WR","GB-LE","GB-RT","GB-LI"],"GB-RT":["GB-NA","GB-LE","GB-LI"],"GB-LE":["GB-NT","GB-LI","GB-RT","GB-NA","GB-WR","GB-ST","GB-DB"],"GB-WA":["GB-GC","GB-HD","GB-SP","GB-CH"],"GB-HD":["GB-GC","GB-WA","GB-SP","GB-WO"],"GB-WO":["GB-GC","GB-HD","GB-SP","GB-ST","GB-WR"],"GB-SP":["GB-HD","GB-WA","GB-CH","GB-ST","GB-WO"],"GB-WR":["GB-NA","GB-OX","GB-GC","GB-WO","GB-ST","GB-LE"],"GB-NT":["GB-LI","GB-LE","GB-DB","GB-YK"],"GB-ST":["GB-WR","GB-WO","GB-SP","GB-CH","GB-DB","GB-LE"],"GB-DB":["GB-NT","GB-LE","GB-ST","GB-CH","GB-LA","GB-YK"],"GB-YK":["GB-LI","GB-NT","GB-DB","GB-LA","GB-CU","GB-DH"],"GB-CH":["GB-DB","GB-ST","GB-SP","GB-WA","GB-LA"],"GB-LA":["GB-DB","GB-CH","GB-YK","GB-CU"],"GB-DH":["GB-YK","GB-NB","GB-CU"],"GB-CU":["GB-LA","GB-YK","GB-DH","GB-NB","GB-SC"],"GB-NB":["GB-DH","GB-CU","GB-SC"],"GB-SC":["GB-NB","GB-CU"]},
        'poland' : {'PL-DS': ['PL-LB', 'PL-WP', 'PL-OP'],
 'PL-KP': ['PL-PM', 'PL-WN', 'PL-MZ', 'PL-LD', 'PL-WP'],
 'PL-LB': ['PL-ZP', 'PL-WP', 'PL-DS'],
 'PL-LD': ['PL-WP', 'PL-KP', 'PL-MZ', 'PL-SK', 'PL-SL', 'PL-OP'],
 'PL-LU': ['PL-PD', 'PL-MZ', 'PL-SK', 'PL-PK'],
 'PL-MA': ['PL-PK', 'PL-SK', 'PL-SL'],
 'PL-MZ': ['PL-WN', 'PL-PD', 'PL-LU', 'PL-SK', 'PL-LD', 'PL-KP'],
 'PL-OP': ['PL-DS', 'PL-WP', 'PL-LD', 'PL-SL'],
 'PL-PD': ['PL-WN', 'PL-MZ', 'PL-LU'],
 'PL-PK': ['PL-LU', 'PL-SK', 'PL-MA'],
 'PL-PM': ['PL-ZP', 'PL-WP', 'PL-KP', 'PL-WN'],
 'PL-SK': ['PL-MZ', 'PL-LU', 'PL-PK', 'PL-MA', 'PL-SL', 'PL-LD'],
 'PL-SL': ['PL-OP', 'PL-LD', 'PL-SK', 'PL-MA'],
 'PL-WN': ['PL-PM', 'PL-KP', 'PL-MZ', 'PL-PD'],
 'PL-WP': ['PL-LB', 'PL-ZP', 'PL-PM', 'PL-KP', 'PL-LD', 'PL-OP', 'PL-DS'],
 'PL-ZP': ['PL-PM', 'PL-WP', 'PL-LB']},
        'australia' : {'AU-NSW': ['AU-VIC', 'AU-SA', 'AU-QLD'],
                     'AU-NT': ['AU-WA', 'AU-SA', 'AU-QLD'],
                     'AU-QLD': ['AU-NT', 'AU-SA', 'AU-NSW'],
                     'AU-SA': ['AU-WA', 'AU-NT', 'AU-QLD', 'AU-NSW', 'AU-VIC'],
                     'AU-TAS': [],
                     'AU-VIC': ['AU-SA', 'AU-NSW'],
                     'AU-WA': ['AU-SA', 'AU-NT']}
    }
	



class SudokuProblem:
    
    @staticmethod
    def generatePuzzle():
        while True:
            try:
                puzzle  = [[0]*9 for i in range(9)]
                rows    = [set(range(1,10)) for i in range(9)]
                columns = [set(range(1,10)) for i in range(9)]
                squares = [set(range(1,10)) for i in range(9)]
                for i in range(9):
                    for j in range(9):
                        choices = rows[i].intersection(columns[j]).intersection(squares[(i//3)*3 + j//3])
                        choice  = random.choice(list(choices))

                        puzzle[i][j] = choice

                        rows[i].discard(choice)
                        columns[j].discard(choice)
                        squares[(i//3)*3 + j//3].discard(choice)
                        
                prob = .3
                for i in range(9):
                    for j in range(9):
                        if random.uniform(0,1) > prob:
                            puzzle[i][j] = 'X'
                    
                return puzzle
            
            except IndexError:
                pass
