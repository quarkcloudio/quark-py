from quark import APIRouter, Request, JSONResponse, jsonable_encoder
from .. import loader

router = APIRouter(prefix="/api/admin", tags=["仪表盘"])


@router.get("/dashboard/{resource}/index")
async def index(resource: str, request: Request):
    data = await loader.load_resource_object(resource, "Dashboard").render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)
