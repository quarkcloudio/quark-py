from typing import Dict, Any, Optional, List
from .base import Base


class Geofence(Base):

    component: str = "geofenceField"
    """
    组件名称
    """

    default_value: Optional[Any] = {
        "center": {"longitude": "116.397724", "latitude": "39.903755"},
        "points": [],
    }
    """
    默认选中的选项
    """

    disabled: bool = False
    """
    整组是否失效，默认为 False
    """

    style: Dict[str, Any] = {"height": 500, "width": "100%", "marginTop": "10px"}
    """
    自定义样式
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    zoom: int = 14
    """
    缩放级别，默认为 14
    """

    map_key: str = "70ac74a1443326e66e51a4255700a4e2"
    """
    地图 Key
    """

    map_security_js_code: str = "5c4fc57d6cba5efd1c15c988d18d2a78"
    """
    地图安全密钥
    """

    def set_zoom(self, zoom: int):
        """
        设置缩放级别。

        Args:
            zoom (int): 缩放级别值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.zoom = zoom
        return self

    def set_map_key(self, key: str):
        """
        设置地图 Key。

        Args:
            key (str): 地图 Key 值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.map_key = key
        return self

    def set_map_security_js_code(self, security_js_code: str):
        """
        设置地图安全密钥。

        Args:
            security_js_code (str): 地图安全密钥值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.map_security_js_code = security_js_code
        return self

    def set_width(self, width: Any):
        """
        设置地图宽度。

        Args:
            width (Any): 地图宽度值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        style = self.style.copy()
        style["width"] = width
        self.style = style
        return self

    def set_height(self, height: Any):
        """
        设置地图高度。

        Args:
            height (Any): 地图高度值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        style = self.style.copy()
        style["height"] = height
        self.style = style
        return self

    def set_center(self, longitude: str, latitude: str):
        """
        设置中心点。

        Args:
            longitude (str): 经度。
            latitude (str): 纬度。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if isinstance(self.value, dict):
            self.value["center"] = {"longitude": longitude, "latitude": latitude}
        return self

    def set_points(self, points: List[Any]):
        """
        设置多边形围栏坐标点。

        Args:
            points (List[Any]): 坐标点列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if isinstance(self.value, dict):
            self.value["points"] = points
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
