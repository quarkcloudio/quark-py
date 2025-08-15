from quark import APIRouter, JSONResponse, Request, jsonable_encoder

from .. import loader

router = APIRouter(prefix="/api/admin", tags=["管理后台布局"])


@router.get("/layout/{resource}/index")
async def index(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Layout")
    return JSONResponse(
        content=jsonable_encoder(await res.render(request), exclude_none=True)
    )
