from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.in_degree = 0
        self.out_nodes = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph  = defaultdict(Graph)
        dependencies = 0
        
        for i in prerequisites:
            next_course, previous_course = i[0], i[1]
            graph[previous_course].out_nodes.append(next_course)
            graph[next_course].in_degree += 1
            dependencies += 1
        
        #Start with courses that have no pre-requisites
        independent_courses = deque()
        for i, node in graph.items():
            if node.in_degree == 0:
                independent_courses.append(i)

        removed_edges = 0
        while independent_courses:
            course = independent_courses.pop()
            
            for dependent in graph[course].out_nodes:
                graph[dependent].in_degree -= 1
                removed_edges += 1
                
                if graph[dependent].in_degree == 0:
                    independent_courses.append(dependent)
                    

        if removed_edges == dependencies:
            return True
        else:
            return False
            