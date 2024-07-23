from fastapi.responses import FileResponse, HTMLResponse
import os, math
from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    upload_directory = r"/workspaces/Concatinator/files"
    os.makedirs(upload_directory, exist_ok=True)
    file_path = os.path.join(upload_directory, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename, "file_path": file_path}


@app.get("/", response_class=HTMLResponse)
def get_files(request: Request):
    files = os.listdir(os.path.join(os.getcwd(), 'savefiles'))
    files.sort()
    files_with_sizes = []
    for file in files:
        filesize = os.path.getsize(os.path.join(os.getcwd(), 'savefiles', file))
        files_with_sizes.append({
            "file": file,
            "size": convert_size(filesize)
        })
    return templates.TemplateResponse("index.html", {"request": request, "title": "Concatinator", "files": files_with_sizes})

@app.get("/file-upload", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.get("/download/{file}")
async def download_file(file: str):
    file_path = os.path.join(os.getcwd(), 'savefiles', file)
    return FileResponse(file_path, media_type='application/octet-stream', filename=os.path.basename(file_path))
