from typing import Any
from ..component import Component

class Line(Component):
    """折线图表类"""
    component: str = "line"
    api: str = ""
    width: int = 0
    height: int = 0
    auto_fit: bool = False
    padding: Any = None
    append_padding: Any = None
    renderer: str = ""
    limit_in_plot: bool = False
    locale: str = ""
    data: Any = None
    x_field: str = ""
    y_field: str = ""
    meta: Any = None
    smooth: bool = False
    key: str = ""
    crypt: bool = False

    # 数据接口
    def set_api(self, api: str) -> 'Line':
        self.api = api
        return self

    # 设置图表宽度
    def set_width(self, width: int) -> 'Line':
        self.width = width
        return self

    # 设置图表高度
    def set_height(self, height: int) -> 'Line':
        self.height = height
        return self

    # 图表是否自适应容器宽高。当 autoFit 设置为 true 时，width 和 height 的设置将失效。
    def set_auto_fit(self, auto_fit: bool) -> 'Line':
        self.auto_fit = auto_fit
        return self

    # 画布的 padding 值，代表图表在上右下左的间距，可以为单个数字 16，或者数组 [16, 8, 16, 8] 代表四个方向，或者开启 auto，由底层自动计算间距。
    def set_padding(self, padding: Any) -> 'Line':
        self.padding = padding
        return self

    # 额外增加的 appendPadding 值，在 padding 的基础上，设置额外的 padding 数值，可以是单个数字 16，或者数组 [16, 8, 16, 8] 代表四个方向。
    def set_append_padding(self, append_padding: Any) -> 'Line':
        self.append_padding = append_padding
        return self

    # 设置图表渲染方式为 canvas 或 svg。
    def set_renderer(self, renderer: str) -> 'Line':
        self.renderer = renderer
        return self

    # 是否对超出坐标系范围的 Geometry 进行剪切。
    def set_limit_in_plot(self, limit_in_plot: bool) -> 'Line':
        self.limit_in_plot = limit_in_plot
        return self

    # 指定具体语言，目前内置 'zh-CN' and 'en-US' 两个语言，你也可以使用 G2Plot.registerLocale 方法注册新的语言。语言包格式参考：src/locales/en_US.ts
    def set_locale(self, locale: str) -> 'Line':
        self.locale = locale
        return self

    # 数据
    def set_data(self, data: Any) -> 'Line':
        self.data = data
        return self

    # X轴字段
    def set_x_field(self, x_field: str) -> 'Line':
        self.x_field = x_field
        return self

    # y轴字段
    def set_y_field(self, y_field: str) -> 'Line':
        self.y_field = y_field
        return self

    # 通过 meta 可以全局化配置图表数据元信息，以字段为单位进行配置。在 meta 上的配置将同时影响所有组件的文本信息。传入以字段名为 key，MetaOption 为 value 的配置，同时设置多个字段的元信息。
    def set_meta(self, meta: Any) -> 'Line':
        self.meta = meta
        return self

    # 是否平滑
    def set_smooth(self, smooth: bool) -> 'Line':
        self.smooth = smooth
        return self

    # 初始化
    def init(self) -> 'Line':
        self.component = "line"
        self.set_key("DEFAULT_KEY", False)
        return self

    def set_key(self, key: str, crypt: bool) -> 'Line':
        self.key = key
        self.crypt = crypt
        return self