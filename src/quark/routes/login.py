from quark import APIRouter, JSONResponse, Request, jsonable_encoder

from .. import loader

router = APIRouter(prefix="/api/admin", tags=["管理员登录"])


@router.get("/login/{resource}/index")
async def index(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Login")
    return JSONResponse(
        content=jsonable_encoder(await res.render(request), exclude_none=True)
    )


@router.get("/login/{resource}/captchaId")
async def captcha_id(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Login")
    return JSONResponse(
        content=jsonable_encoder(await res.captcha_id(request), exclude_none=True)
    )


@router.get("/login/{resource}/captcha/{id}")
async def captcha(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Login")
    return await res.captcha(request)


@router.post("/login/{resource}/handle")
async def handle(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Login")
    return JSONResponse(
        content=jsonable_encoder(await res.handle(request), exclude_none=True)
    )


@router.get("/logout/{resource}/handle")
async def logout(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Login")
    return JSONResponse(
        content=jsonable_encoder(await res.logout(request), exclude_none=True)
    )
