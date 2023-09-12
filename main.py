from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi import  UploadFile, HTTPException
from typing import List



# templates klasörünü tanımlıyoruz.
templates = Jinja2Templates(directory="templates")





app = FastAPI()

#static klasörünü tanımlıyoruz.
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    # index.html i döndürüyoruz.
    return templates.TemplateResponse("index.html", {"request": request })

def add_file_to_local_storage(file: UploadFile):
    with open("files/"+file.filename, "wb") as f:
        f.write(file.file.read())
    return file



@app.post("/uploadfiles")
async def create_upload_files(files: List[UploadFile]):
    for file in files:
        add_file_to_local_storage(file)
        
    return {"filenames": [file.filename for file in files]}
