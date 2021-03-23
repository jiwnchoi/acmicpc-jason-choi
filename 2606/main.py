def dfs(graph):
    stack = [1]
    visited = [1]
    while stack:
        next_node = stack.pop()
        
        for i in graph[next_node]:
            if i not in visited:
                stack.append(i)
                visited.append(i)
    return len(visited)-1

            
    

vertex = int(input())
edge = int(input())

graph = {x : [] for x in range(1,vertex+1)}

for i in range(edge):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
print(dfs(graph))