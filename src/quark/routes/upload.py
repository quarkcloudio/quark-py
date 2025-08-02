from quark import APIRouter, Request, JSONResponse, jsonable_encoder
from .. import loader

router = APIRouter(prefix="/api/admin", tags=["文件上传"])


@router.post("/upload/{resource}/handle")
async def handle(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Upload")
    return JSONResponse(
        content=jsonable_encoder(await res.handle(request), exclude_none=True)
    )


@router.post("/upload/{resource}/base64Handle")
async def base64_handle(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Upload")
    return JSONResponse(
        content=jsonable_encoder(await res.base64_handle(request), exclude_none=True)
    )
