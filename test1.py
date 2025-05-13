from collections import defaultdict, deque
class Workflowengine:
	Def __init__(self):
		self.graph=defaultdict(list)
		self.in_degree=default(int)
		self.steps=set()
def addstep(self,stepID):
	If stepID not in self.steps:
		self.step.add(stepID)
		self.in_degree[stepID]=self.in_degree.get(stepID,0)
def addDependency(self, stepID,prerequisite):
	self.graph[prerequisite].append(stepID)
	self.in_degree[stepID]+=1
	self.steps.add(stepID)
	self.steps.add(prerequisite)
def execorder(self):
	queue=deque([step for self.steps if self.in_degree[steps]==0])
	result=[]
	while queue:
		current = queue.popleft()
		result.append(current)
		for  neighbor in self.graph[current]:
			Self.in_degree[neighbors] -=1
			If self.in_degree[neighbors]==0
				queue.append(neighbors)
if len(results)!=len(self.steps):
	return “cycle”
return result


engine=Workflowengine()
engine.addstep(“A”)
engine.addstep(“B”)
engine.addDependency("B","A")
engine.addstep(“C”)
engine.addDependency("C","B")
print(engine.getexecorder())
