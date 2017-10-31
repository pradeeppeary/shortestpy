	
#akhil jarodia 2017130 B1
def dijkstra(Graph,source):
	
	dist=[]
	prev=[]
	q=[]
	
	from math import inf
	for i in range(len(Graph[1])):
		dist.append(inf)
		q.append(i)
	dist[source]=0	
	from copy import deepcopy
				
	

	while len(q)>0:
		
		t=[]
		for i in q:
			t.append(dist[i])
		u=q[t.index(min(t))]	
		
		
		q.remove(u)
		
		
		
		for r in Graph[0][u]:
			alt=dist[u]+Graph[1][u][Graph[0][u].index(r)]
			if alt<dist[r]:
				dist[r]=alt
		


		
		
	return dist
        	


def bfs(Graph,source):
	a=[]
	a.append(source)
	b=[]
	dist=[]
	b.append(source)
	from math import inf
	for i in range(len(Graph[1])):
		dist.append(inf)
		
	dist[source]=0
	while len(a)>0:
		
		u=a[0]
		a.remove(a[0])
		for i in Graph[0][u]:
			if i not in b:
				a.append(i)
				b.append(i)
				dist[i]=dist[u]+Graph[1][u][Graph[0][u].index(i)]
		
	
	
	return dist
	



if __name__=='__main__'	:	
	n=int(input())#no of vertex

	f=[]
	e=[]
	for i in range(n):
		b=[]
		c=int(input())
		a=[]
		for j in range(c):
			d=input().split()
			d=list(map(int,d))	
			b.append(d[0])
			a.append(d[1])
		e.append(b)#connection to diff tiles	
		f.append(a)#weights
	g=[]#graph
	g.append(e)
	g.append(f)
	t=input("Enter source :")
	t=int(t)
	print(bfs(g,t))
	print(dijkstra(g,t))
		
		
		


			