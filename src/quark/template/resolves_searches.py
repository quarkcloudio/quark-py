import inspect

class Template:
    def __init__(self, template):
        self.template = template
    
    def index_searches(self, ctx):
        # 模版实例
        template = ctx.template  # 假设 ctx 对象有 template 属性
        searches = template.searches(ctx)

        # 搜索组件
        search = template.get_table_search(ctx)

        # 是否携带导出功能
        export = template.get_export()
        if export:
            export_text = template.get_export_text()  # 导出按钮文字内容
            export_path = getattr(ctx.template, 'export_path', '')
            search.set_export_text(export_text).set_export_api(export_path.replace(":resource", ctx.param('resource')))
        
        # 解析搜索项
        for v in searches:
            # 搜索栏表单项
            item = None
            field = Field()  # 创建表单字段实例
            
            search_instance = v  # 假设每个 search 是一个 Searcher 实例

            # 初始化模板
            search_instance.new(ctx)
            search_instance.init(ctx)

            # 获取组件名称
            component = search_instance.get_component()

            # 获取组件的标签
            label = search_instance.get_name()

            # 获取字段名，支持数组
            name = search_instance.get_column(v)

            # 获取接口
            api = search_instance.get_api()

            # 获取属性
            options = search_instance.options(ctx)

            # 获取 Select 组件的 Load
            load = search_instance.load(ctx)

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
