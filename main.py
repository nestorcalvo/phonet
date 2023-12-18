
from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI, HTTPException
from phonet.graph import Graph
import os

app = FastAPI()

GENERAL_PATH = './prueba/'

class Item(BaseModel):
    path: str
    id: str


@app.get("/")
def read_root():
    return "Root endpoint, check /health or /audio_process"


@app.get("/health")
def health():
    return "Ok"


@app.get("/audio_process")
def plot_audio_figure(item: Item):
    try:
        subject_path = os.path.join(GENERAL_PATH, item.id)
        print(subject_path)
        feature_name = str(item.id) + '.csv'
        print(feature_name)
        feature_storage_path = os.path.join(subject_path, feature_name)
        print(feature_storage_path)
        os.makedirs(subject_path, exist_ok=True) 
        graph_creator = Graph(item.path, feature_storage_path, subject_path)
        graph_success = graph_creator.plot_store_graph()
        if graph_success == False:
            raise HTTPException(status_code=404, detail="Problems with the graph creation, check the backend")
        return item 
        
    except:
        raise HTTPException(status_code=404, detail="Item not found")