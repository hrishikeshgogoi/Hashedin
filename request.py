class WorkflowCreate(Basemodel):
  workflow_str_id: str
  name: str
  description: str

class StepCreate(Basemodel):
  step_str_id: str
  description: str

class DependencyCreate(Basemodel):
  step_str_id: str
  prerequisite_step_str_id: str
