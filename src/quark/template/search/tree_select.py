from .search import Search


class TreeSelect(Search):

    def __init__(self, column: str = "", name: str = ""):
        self.component = "treeSelectField"
        return self

    # 设置 Option
    def option(self, title: str, value):
        return {"value": value, "title": title}

    # 可选项数据源
    #
    # 示例：
    # set_tree_data([{"value": "zhejiang", "title": "Zhejiang"}])
    #
    # 或者
    #
    # set_tree_data(options, parent_key_name, title_name, value_name)
    #
    # 或者
    #
    # set_tree_data(options, 0, parent_key_name, title_name, value_name)
    def set_tree_data(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            self.tree_select_options = args[0]
            return self

        if len(args) == 4:
            self.tree_select_options = self.list_to_tree_data(
                args[0], 0, args[1], args[2], args[3]
            )
            return self

        if len(args) == 5:
            self.tree_select_options = self.list_to_tree_data(
                args[0], args[1], args[2], args[3], args[4]
            )
            return self

        return self

    @staticmethod
    def list_to_tree_data(data, parent_id, parent_key, title_key, value_key):
        """模拟从列表结构生成树形数据"""
        tree_data = []
        data_map = {}

        # 构建所有节点的映射关系
        for item in data:
            item_id = item[value_key]
            data_map[item_id] = {
                "title": item[title_key],
                "value": item_id,
                "children": [],
            }

        # 根据 parentId 构建父子关系
        for item in data:
            node = data_map[item[value_key]]
            if item[parent_key] == parent_id:
                tree_data.append(node)
            else:
                parent_node = data_map.get(item[parent_key], None)
                if parent_node is not None:
                    parent_node["children"].append(node)

        return tree_data
