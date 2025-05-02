import json

def list_to_tree(data, pk: str, pid: str, child: str, root: int):
    """
    将列表数据转换为树形结构
    :param data: 列表数据
    :param pk: 主键字段名（如 "id"）
    :param pid: 父级字段名（如 "parent_id"）
    :param child: 子级字段名（如 "children"）
    :param root: 根节点的父级值（通常为0）
    :return: 树形结构列表
    """
    result = json.loads(json.dumps(data))  # 模拟深拷贝，处理嵌套结构
    tree_list = []

    for item in result:
        if item.get(pid) == root:
            children = list_to_tree(data, pk, pid, child, item.get(pk))
            if children:
                item[child] = children
            else:
                item[child] = None
            tree_list.append(item)

    return tree_list


def tree_to_ordered_list(tree, level: int, field: str, child: str):
    """
    将树结构转换为有序列表，并添加层级前缀
    :param tree: 树结构数据
    :param level: 当前层级
    :param field: 需要添加前缀的字段名
    :param child: 子级字段名
    :return: 有序列表
    """
    ordered_list = []

    for node in tree:
        node[field] = '—' * level + node.get(field, '')
        ordered_list.append(node)
        if node.get(child):
            children = tree_to_ordered_list(node[child], level + 1, field, child)
            ordered_list.extend(children)

    return ordered_list