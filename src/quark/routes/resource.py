from quark import APIRouter, Request, JSONResponse, jsonable_encoder
from .. import loader

router = APIRouter(prefix="/api/admin", tags=["后台增、删、改、查"])


# 列表
@router.get("/{resource}/index")
async def index(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").index_render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 表格行内编辑
@router.get("/{resource}/editable")
async def editable(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").editable_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 执行行为
@router.get("/{resource}/action/{uriKey}")
async def action_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").action_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 行为表单值
@router.get("/{resource}/action/{uriKey}/values")
async def action_values_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").action_values_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 创建页面
@router.get("/{resource}/create")
async def creation_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").creation_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 创建方法
@router.post("/{resource}/store")
async def store_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").store_render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 编辑页面
@router.get("/{resource}/edit")
async def edit_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").edit_render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 获取编辑表单值
@router.get("/{resource}/edit/values")
async def edit_values_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").edit_values_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 保存编辑值
@router.post("/{resource}/save")
async def save_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").save_render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 导入数据
@router.post("/{resource}/import")
async def import_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").import_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 导出数据
@router.get("/{resource}/export")
async def export_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").export_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 详情页
@router.get("/{resource}/detail")
async def detail_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").detail_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 获取详情页值
@router.get("/{resource}/detail/values")
async def detail_values_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").detail_values_render(
        request
    )
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 导入模板
@router.get("/{resource}/import/template")
async def import_template_render(resource, request: Request):
    data = await loader.load_resource_object(
        resource, "Resource"
    ).import_template_render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)


# 表单页
@router.get("/{resource}/form")
async def form_render(resource, request: Request):
    data = await loader.load_resource_object(resource, "Resource").form_render(request)
    encoded = jsonable_encoder(data, exclude_none=True)
    return JSONResponse(content=encoded)
