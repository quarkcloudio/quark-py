from quark import APIRouter, Request, JSONResponse, jsonable_encoder
from .. import loader

router = APIRouter(prefix="/api/admin", tags=["管理员登录"])


@router.get("/login/{resource}/index")
async def index(resource: str, request: Request):
    data = await loader.load_resource_object(resource, "Login").render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


@router.get("/login/{resource}/captchaId")
async def captcha_id(resource: str, request: Request):
    data = await loader.load_resource_object(resource, "Login").captcha_id(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


@router.get("/login/{resource}/captcha/{id}")
async def captcha(resource: str, request: Request):
    return await loader.load_resource_object(resource, "Login").captcha(request)


@router.post("/login/{resource}/handle")
async def handle(resource: str, request: Request):
    data = await loader.load_resource_object(resource, "Login").handle(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


@router.get("/logout/{resource}/handle")
async def logout(resource: str, request: Request):
    data = await loader.load_resource_object(resource, "Login").logout(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)
