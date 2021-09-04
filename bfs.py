from collections import defaultdict

class graph:
	def __init__(self):
		self.adjacencyList= defaultdict(list)

	def addEdge(self,source,destination):
		self.adjacencyList[source].append(destination)

	def BFS(self, start):

		queue=[]
		visited=[0]*len(self.adjacencyList)
		visited[start]=1
		queue.append(start)
		while queue:
			node=queue.pop(0)
			print(node, end=" ")
			for i in self.adjacencyList[node]:
				if visited[i]==0:
					queue.append(i)
					visited[i]=1


g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS(2)