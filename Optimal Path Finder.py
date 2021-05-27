import csv
import copy
from csv import writer
from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight



def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]
        # print(destinations)
        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path






def create_edges(csv_file):

	with open(csv_file ) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		i =1
		path = {}
		for row in csv_reader:
			path[i] = row
			i = i+1

	test = copy.deepcopy(path)

	# print(test)
	for i in range(1,len(test)+1):
		all_keys = []
		key = test[i][0]
		all_keys.append(key)
		if key == '0':
			continue
		else:
			# print("in else",i)
			test[i].append(str(test[int(key)][0]))
			key2 = str(test[int(key)][0])
			# all_keys.append(key2)
			check = False
			while key2 is not '0':
				if key2 == key:
					break
				else:
					if  check is True:
						break
					if key2 in all_keys:
						check = True
					test[i].append(str(test[int(key2)][0]))
					# print("else test", test)
					key2 = str(test[int(key2)][0])
					all_keys.append(key2)

	# print(test)

	all_students = []
	for list_of_elem in test :
		edges = []
		# print(list_of_elem)
		edges.append((str(list_of_elem),test[list_of_elem][0], 1))
		for e in range(len(test[list_of_elem])-1):
			edges.append((test[list_of_elem][e],test[list_of_elem][int(e)+1], 1))
		all_students.append(edges)
	return all_students

ds_routes = create_edges('C:/Users/Govind Satwani/Desktop/DS-Sheet1.csv')
pcp_routes = create_edges('C:/Users/Govind Satwani/Desktop/PCP - Sheet1.csv')
#dms_routes = create_edges('/home/vassar/Desktop/DMS - Sheet1.csv')


student_wise_edges = {}
for i in range(len(pcp_routes)):
	student_wise_edges[i] = pcp_routes[i]
	for j in ds_routes[i]: 
		student_wise_edges[i].append(j)




for i in student_wise_edges :
	print(i+1, student_wise_edges[i])
	graph = Graph()
	for edge in student_wise_edges[i]:
		graph.add_edge(*edge)

	path = dijsktra(graph, str(int(i)+1), '0')

	print("selected-----" , path)
	print('\n')


# student_wise_edges = {}
# for i in range(len(dms_routes)):
# 	student_wise_edges[i] = dms_routes[i]
# 	for j in ds_routes[i]: 
# 		student_wise_edges[i].append(j)
# 	for k in pcp_routes[i]:
# 		student_wise_edges[i].append(k)


# for i in student_wise_edges :
# 	print(i+1, student_wise_edges[i])
# 	graph = Graph()
# 	for edge in student_wise_edges[i]:
# 		graph.add_edge(*edge)

# 	path = dijsktra(graph, str(int(i)+1), '0')

# 	print("selected-----" , path)
# 	print('\n')