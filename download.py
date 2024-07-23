from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse
import os, math

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


@app.get("/")
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

@app.get("/download/{file}")
async def download_file(file: str):
    file_path = os.path.join(os.getcwd(), 'savefiles', file)
    return FileResponse(file_path, media_type='application/octet-stream', filename=os.path.basename(file_path))
