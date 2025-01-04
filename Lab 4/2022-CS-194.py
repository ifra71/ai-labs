class node:
    def _init_ (self):
        self.adj_list={}


class graph:
        def _init_ (self):
          self.graph=[]
    

        def add_edge(self,s,d):
         if s not in self.graph:
            self.graph[s]=[]
         if d not in self.graph:
            self.graph[d]=[]
            self.graph[s].append[d]
            self.graph[d].append[s] 


        def delete_edge(self,s,d):
            if s in self.graph and d in self.graph:
                if d in self.graph[s]:
                 self.graph[s].remove(d)
                if s in self.graph[d]:
                 self.graph[d].remove(s)
            else:
               print("node not found")
           
        def get_connected_nodes(self,node):
           return self.graph.get(node,[])
        

        
        def get_edge(self,node1,node2):
           if node1 in self.graph and node2 in self.graph[node1]:
              return  (node1 and node2)
           elif node1 in self.graph and node2 in self.graph[node2]:
              return  (node1 and node2)
           return None 
        

        def print_graph(self):
           for node,neighbors in self.graph.items():
              print(f"vertex{node}:{neighbors}")
           
        def are_connected(self,node1,node2):
           return node2 in self.graph.get(node1,[])
        
        def isValidPath(self,path):
           for i in range(len(path)-1):
              if path [i+1] not in self.graph.get(path[i],[]):
                 return False
              return True
           


graph=graph()
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(0,3)
graph.add_edge(0,4)
graph.add_edge(0,5)

graph.print_graph()
print("connected nodes of 0:",graph.get_connected_nodes(1))





