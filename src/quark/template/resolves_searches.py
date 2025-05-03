from flask import request
from typing import Any, Optional
from ..component.table.search import Search as TableSearch

class ResolvesSearches:

    # 搜索组件
    search: TableSearch = None

    # 搜索字段
    searches: Optional[Any] = None

    # 导出功能
    export = False

    # 导出文字
    export_text = None

    # 导出路径
    export_path = None

    def set_search(self, search) -> 'ResolvesSearches':
        """设置搜索组件"""
        self.search = search
        return self

    def set_searches(self, searches) -> 'ResolvesSearches':
        """设置字段"""
        self.searches = searches
        return self
    
    def set_export(self, export: bool, export_text: str, export_path: str) -> 'ResolvesSearches':
        """设置导出功能"""
        self.export = export
        self.export_text = export_text
        self.export_path = export_path
        return self

    def index_searches(self):

        # 搜索组件
        search = self.search

        # 搜索字段
        searches = self.searches

        # 是否携带导出功能
        export = self.export
        if export:
            export_text = self.export_text # 导出按钮文字内容
            export_path = self.export_path
            search.set_export_text(export_text).set_export_api(export_path.replace("<resource>", request.view_args.get('resource')))
        
        # 解析搜索项
        for v in searches:
            # 搜索栏表单项
            item = None
            field = Field()  # 创建表单字段实例
            
            search_instance = v  # 假设每个 search 是一个 Searcher 实例

            # 获取组件名称
            component = search_instance.get_component()

            # 获取组件的标签
            label = search_instance.get_name()

            # 获取字段名，支持数组
            name = search_instance.get_column(v)

            # 获取接口
            api = search_instance.get_api()

            # 获取属性
            options = search_instance.options()

            # 获取 Select 组件的 Load
            load = search_instance.load()

            # 根据组件类型创建相应的表单项
            if component == "textField":
                item = field.text(name, label).set_width(None)
            elif component == "selectField":
                item = field.select(name, label).set_width(None).set_options(options).set_load(load["field"], load["api"])
            elif component == "radioField":
                item = field.radio(name, label).set_options(options).set_option_type("button").set_button_style("solid")
            elif component == "multipleSelectField":
                item = field.select(name, label).set_mode("multiple").set_width(None).set_options(options)
            elif component == "dateField":
                item = field.date(name, label).set_width(None)
            elif component == "datetimeField":
                item = field.datetime(name, label).set_width(None)
            elif component == "dateRangeField":
                item = field.date_range(name, label).set_width(None)
            elif component == "datetimeRangeField":
                item = field.datetime_range(name, label).set_width(None)
            elif component == "cascaderField":
                item = field.cascader(name, label).set_api(api).set_width(None).set_options(options)
            elif component == "treeSelectField":
                item = field.tree_select(name, label).set_width(None).set_tree_data(options)

            search = search.set_items(item)

        return search
