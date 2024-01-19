
import os
from typing import Union

from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
import subprocess
from phonet.graph import Graph

app = FastAPI()

GENERAL_PATH = '/efs/pronunciation_data'


class Item(BaseModel):
    path: str
    id: str
    sesion: str


@app.get("/")
def read_root():
    return "Root endpoint, check /health or /audio_process"


@app.get("/health")
def health():
    return "Ok"


@app.post("/audio_process")
def plot_audio_figure(path: str = Form(), id: str = Form(), sesion: str = Form()):
    try:
        subject_path = os.path.join(GENERAL_PATH, id)
        sesion_name = 'S' + str(sesion)
        sesion_path = os.path.join(subject_path, sesion_name)
        # print(subject_path)
        feature_name = str(id) + '.csv'
        # print(feature_name)
        feature_storage_path = os.path.join(sesion_path, feature_name)
        image_storage_path = os.path.join(sesion_path, 'images')
        # print(feature_storage_path)
        os.makedirs(image_storage_path, exist_ok=True)
        if (".webm" in path):
            new_path = path.replace(".webm",".wav")
            command = ['ffmpeg', '-i', path, new_path]
            subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
            path = new_path
        graph_creator = Graph(
            path, feature_storage_path, image_storage_path)
        graph_success = graph_creator.plot_store_graph()
        if graph_success == False:
            raise HTTPException(
                status_code=404, detail="Problems with the graph creation, check the backend")
        success = "Imagenes generadas exitosamente para el id "+str(id)+" fueron almacenadas en la sesion " + str(sesion)
        return success
    except:
        raise HTTPException(status_code=404, detail="Item not found")
