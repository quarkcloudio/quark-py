from quark import APIRouter, JSONResponse, Request, jsonable_encoder

from .. import loader

router = APIRouter(prefix="/api/admin", tags=["仪表盘"])


@router.get("/dashboard/{resource}/index")
async def index(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Dashboard")
    return JSONResponse(
        content=jsonable_encoder(await res.render(request), exclude_none=True)
    )
