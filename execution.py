@app.get("/workflows/{workflow_str_id}/execution-order")
def get_execution_order(workflow_str_id: str):
    db = SessionLocal()
    wf = db.query(Workflow).filter_by(workflow_str_id=workflow_str_id).first()
    if not wf:
        raise HTTPException(status_code=404, detail="Workflow not found")
    
    steps = db.query(Step).filter_by(workflow_id=wf.id).all()
    deps = db.query(Dependency).filter_by(workflow_id=wf.id).all()

    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    id_to_step = {step.id: step.step_str_id for step in steps}
    str_to_id = {step.step_str_id: step.id for step in steps}

    for dep in deps:
        graph[dep.prerequisite_step_id].append(dep.step_id)
        in_degree[dep.step_id] += 1

    queue = deque([step.id for step in steps if in_degree[step.id] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(id_to_step[node])
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(steps):
        raise HTTPException(status_code=400, detail="Cycle detected")

    return {"execution_order": result}
