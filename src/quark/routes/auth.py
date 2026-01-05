from quark import APIRouter, JSONResponse, Request, jsonable_encoder

from .. import loader

router = APIRouter(prefix="/api/admin", tags=["管理员登录"])


@router.get("/auth/{resource}/index")
async def index(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Auth")
    return JSONResponse(
        content=jsonable_encoder(await res.render(request), exclude_none=True)
    )

@router.get("/auth/{resource}/captcha")
async def captcha(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Auth")
    return await res.captcha(request)


@router.post("/auth/{resource}/login")
async def login(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Auth")
    return JSONResponse(
        content=jsonable_encoder(await res.login(request), exclude_none=True)
    )


@router.get("/auth/{resource}/handle")
async def logout(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Auth")
    return JSONResponse(
        content=jsonable_encoder(await res.logout(request), exclude_none=True)
    )
