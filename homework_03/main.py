from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from starlette import status
from starlette.responses import JSONResponse, HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from api.items import router as items_router

app = FastAPI()
app.include_router(items_router)


@app.get("/")
def read_root():
    return {"Hello": "World!"}


@app.get("/ping")
def send_pong():
    return {"message": "pong"}


@app.exception_handler(StarletteHTTPException)
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return await http_exception_handler(request, exc)


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    if (isinstance(exception, StarletteHTTPException)
            and exception.detail != "Not Found"):
        return await http_exception_handler(request, exception)

    return JSONResponse(
        {
            "request url": request.url.path,
            "exception": str(exception),
        },
        status_code=status.HTTP_404_NOT_FOUND,
    )
