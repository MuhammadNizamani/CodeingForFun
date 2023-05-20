import io
from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uuid
from PIL import Image
from rembg import remove
from fastapi.responses import FileResponse
import tempfile


async def removesbg(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)) 
    output_image = remove(image)
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        output_image.save(tmp, format = "png")
        tmp.flush()
        tmp.seek(0)
        # background_color = (255,255,255)
        # background_image = Image.new('RGB', output_image.size, background_color)
        # background_image.paste(output_image, mask=output_image.convert('RGBA'))
    # output_image.show()
    return FileResponse(tmp.name, media_type="image/png")