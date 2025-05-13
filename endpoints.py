@app.post("/workflows")
def create_workflow(workflow: WorkflowCreate):
  db=SessionLocal()
  if db.query(Workflow).filter_by(workflow_str_id=workflow.workflow_str_id).first():
    raise HTTPException(status_code=400,detail="Workflow exists")
  wf= Workflow(**workflow.dict())
  db.add(wf)
  db.commit()
  return {"workflow_str_id": wf.workflow_str_id, "status": "created"}

@app.post("/workflows/{workflow_str_id}/steps")
def add_step(workflow_str_id: str,step:StepCreate):
  db=SessionLocal()
  wf=db.query(Workflow).filter_by(workflow_str_id=workflow_str_id).first()
  if not wf:
    raise HTTPException(status_code=404, detail="Workflow not found")
  st= Step(step_str_id=step.step_str_id, description=step.description,workflow_id=wf.id)
  db.add(st)
  db.commit()
  return {"step_str_id": st.step_str_id,"status":"step_added"}

@app.post("/workflows/{workflow_str_id}/dependencies")
def add_dependency(workflow_str_id: str, dep: DependencyCreate):
    db = SessionLocal()
    wf = db.query(Workflow).filter_by(workflow_str_id=workflow_str_id).first()
    if not wf:
        raise HTTPException(status_code=404, detail="Workflow not found")
    
    step = db.query(Step).filter_by(step_str_id=dep.step_str_id, workflow_id=wf.id).first()
    prereq = db.query(Step).filter_by(step_str_id=dep.prerequisite_step_str_id, workflow_id=wf.id).first()
    
    if not step or not prereq:
        raise HTTPException(status_code=400, detail="Steps not found")
    
    db.add(Dependency(workflow_id=wf.id, step_id=step.id, prerequisite_step_id=prereq.id))
    db.commit()
    return {"status": "dependency_added"}
