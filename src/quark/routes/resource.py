from quark import APIRouter, JSONResponse, Request, jsonable_encoder

from .. import loader

router = APIRouter(prefix="/api/admin", tags=["后台增、删、改、查"])


# 列表
@router.get("/{resource}/index")
async def index(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.index_render(request), exclude_none=True)
    )


# 表格行内编辑
@router.get("/{resource}/editable")
async def editable(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.editable_render(request), exclude_none=True)
    )


# 执行行为
@router.get("/{resource}/action/{uriKey}")
async def action_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.action_render(request), exclude_none=True)
    )


# 行为表单值
@router.get("/{resource}/action/{uriKey}/values")
async def action_values_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(
            await res.action_values_render(request), exclude_none=True
        )
    )


# 创建页面
@router.get("/{resource}/create")
async def creation_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.creation_render(request), exclude_none=True)
    )


# 创建方法
@router.post("/{resource}/store")
async def store_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.store_render(request), exclude_none=True)
    )


# 编辑页面
@router.get("/{resource}/edit")
async def edit_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.edit_render(request), exclude_none=True)
    )


# 获取编辑表单值
@router.get("/{resource}/edit/values")
async def edit_values_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(
            await res.edit_values_render(request), exclude_none=True
        )
    )


# 保存编辑值
@router.post("/{resource}/save")
async def save_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.save_render(request), exclude_none=True)
    )


# 导入数据
@router.post("/{resource}/import")
async def import_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.import_render(request), exclude_none=True)
    )


# 导出数据
@router.get("/{resource}/export")
async def export_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.export_render(request), exclude_none=True)
    )


# 详情页
@router.get("/{resource}/detail")
async def detail_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.detail_render(request), exclude_none=True)
    )


# 获取详情页值
@router.get("/{resource}/detail/values")
async def detail_values_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(
            await res.detail_values_render(request), exclude_none=True
        )
    )


# 导入模板
@router.get("/{resource}/import/template")
async def import_template_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(
            await res.import_template_render(request), exclude_none=True
        )
    )


# 表单页
@router.get("/{resource}/form")
async def form_render(request: Request, resource: str):
    res = await loader.load_resource_object(request, resource, "Resource")
    return JSONResponse(
        content=jsonable_encoder(await res.form_render(request), exclude_none=True)
    )
