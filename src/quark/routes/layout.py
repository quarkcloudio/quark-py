from quark import APIRouter, Request, JSONResponse, jsonable_encoder
from .. import loader

router = APIRouter(prefix="/api/admin", tags=["管理后台布局"])


@router.get("/layout/{resource}/index")
async def index(resource: str, request: Request):
    data = await loader.load_resource_object(resource, "Layout").render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)
