from fasapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from squalchemy import create_engine,Column, Integer, String, ForeignKey
from squalchemy.orm import sessionmarker, declarative_base, relationship

app=FastAPI()
Base=declarative_base()
engine=create_engine(workflow.db)
SessionLocal=sessionmaker(bind=engine)


class Workflow(Base):
  __tablename__="workflows"
  id = Column(Integer, primary_key=True)
  workflow_str_id=Column(String,unique=True)
  name=Column(String)
  description=Column(String)
  steps=relationship("Steps",back_populates="workflow")

class Step(Base)
  __tablename__="steps"
  id=Column(Integer, primary_key=True)
  step_str_id=Column(String)
  description=Column(String)
  workflow_id=Column(Integer,Foreignkey("workflows.id"))
  workflow=relationship("Workflow",back_populates="steps")

class Dependency(Base):
  __tablename__="dependencies"
  id=Column(Integer,primary_key=True)
  workflow_id=Column(Integer)
  prerequisite_step_is=Column(Integer)

Base.metadata.create_all(bind=engine)
