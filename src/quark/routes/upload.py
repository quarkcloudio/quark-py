from quark import APIRouter, JSONResponse, Request, jsonable_encoder

from .. import loader

router = APIRouter(prefix="/api/admin", tags=["文件上传"])


@router.get("/upload/{resource}/getList")
async def get_list(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Upload")
    return JSONResponse(
        content=jsonable_encoder(await res.get_list(request), exclude_none=True)
    )


@router.get("/upload/{resource}/delete")
async def delete_get(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Upload")
    return JSONResponse(
        content=jsonable_encoder(await res.delete(request), exclude_none=True)
    )


@router.post("/upload/{resource}/delete")
async def delete_post(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Upload")
    return JSONResponse(
        content=jsonable_encoder(await res.delete(request), exclude_none=True)
    )


@router.post("/upload/{resource}/crop")
async def crop(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Upload")
    return JSONResponse(
        content=jsonable_encoder(await res.crop(request), exclude_none=True)
    )


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
