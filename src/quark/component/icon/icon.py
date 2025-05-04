from pydantic import model_validator
from typing import Union, Dict, List, Optional
from ..component import Component

class Icon(Component):
    """
    Component 类表示一个图标组件，包含图标的各种属性和方法。
    """
    component: str = "icon"  # 组件类型，默认为 "icon"
    script_url: Optional[Union[str, List[str]]] = None  # iconfont.cn 项目在线生成的 js 地址，@ant-design/icons@4.1.0 之后支持 string[] 类型
    extra_common_props: Dict[str, Union[str, int, float, bool, None]] = {}  # 给所有的 svg 图标 <Icon /> 组件设置额外的属性
    class_name: str = None  # 计算后的 svg 类名
    height: Union[int, float, str, None] = None  # svg 元素高度
    width: Union[int, float, str, None] = None  # svg 元素宽度
    type: Optional[str] = None  # 图标类型

    @model_validator(mode="after")
    def init(self):
        """
        初始化 Component 对象，并设置默认值。
        """
        self.set_key()
        return self

    def set_script_url(self, script_url: Union[str, List[str]]) -> 'Icon':
        """
        设置 iconfont.cn 项目在线生成的 js 地址。

        :param script_url: js 地址，可以是单个字符串或字符串列表
        :return: 当前 Component 对象
        """
        self.script_url = script_url
        return self

    def set_extra_common_props(self, extra_common_props: Dict[str, Union[str, int, float, bool, None]]) -> 'Icon':
        """
        设置给所有的 svg 图标 <Icon /> 组件的额外属性。

        :param extra_common_props: 额外属性字典
        :return: 当前 Component 对象
        """
        self.extra_common_props = extra_common_props
        return self

    def set_class_name(self, class_name: str) -> 'Icon':
        """
        设置计算后的 svg 类名。

        :param class_name: 类名字符串
        :return: 当前 Component 对象
        """
        self.class_name = class_name
        return self

    def set_height(self, height: Union[int, float, str, None]) -> 'Icon':
        """
        设置 svg 元素的高度。

        :param height: 高度值，可以是整数、浮点数、字符串或 None
        :return: 当前 Component 对象
        """
        self.height = height
        return self

    def set_width(self, width: Union[int, float, str, None]) -> 'Icon':
        """
        设置 svg 元素的宽度。

        :param width: 宽度值，可以是整数、浮点数、字符串或 None
        :return: 当前 Component 对象
        """
        self.width = width
        return self

    def set_type(self, icon_type: str) -> 'Icon':
        """
        设置图标类型。

        :param icon_type: 图标类型字符串
        :return: 当前 Component 对象

        "icon-database", "icon-sever", "icon-mobile", "icon-tablet", "icon-redenvelope",
        "icon-book", "icon-filedone", "icon-reconciliation", "icon-file-exception",
        "icon-filesync", "icon-filesearch", "icon-solution", "icon-fileprotect",
        "icon-file-add", "icon-file-excel", "icon-file-exclamation", "icon-file-pdf",
        "icon-file-image", "icon-file-markdown", "icon-file-unknown", "icon-file-ppt",
        "icon-file-word", "icon-file", "icon-file-zip", "icon-file-text", "icon-file-copy",
        "icon-snippets", "icon-audit", "icon-diff", "icon-Batchfolding", "icon-securityscan",
        "icon-propertysafety", "icon-insurance", "icon-alert", "icon-delete", "icon-hourglass",
        "icon-bulb", "icon-experiment", "icon-bell", "icon-trophy", "icon-rest", "icon-USB",
        "icon-skin", "icon-home", "icon-bank", "icon-filter", "icon-funnelplot", "icon-like",
        "icon-unlike", "icon-unlock", "icon-lock", "icon-customerservice", "icon-flag",
        "icon-moneycollect", "icon-medicinebox", "icon-shop", "icon-rocket", "icon-shopping",
        "icon-folder", "icon-folder-open", "icon-folder-add", "icon-deploymentunit",
        "icon-accountbook", "icon-contacts", "icon-carryout", "icon-calendar-check",
        "icon-calendar", "icon-scan", "icon-select", "icon-boxplot", "icon-build", "icon-sliders",
        "icon-laptop", "icon-barcode", "icon-camera", "icon-cluster", "icon-gateway", "icon-car",
        "icon-printer", "icon-read", "icon-cloud-server", "icon-cloud-upload", "icon-cloud",
        "icon-cloud-download", "icon-cloud-sync", "icon-video", "icon-notification", "icon-sound",
        "icon-radarchart", "icon-qrcode", "icon-fund", "icon-image", "icon-mail", "icon-table",
        "icon-idcard", "icon-creditcard", "icon-heart", "icon-block", "icon-error", "icon-star",
        "icon-gold", "icon-heatmap", "icon-wifi", "icon-attachment", "icon-edit", "icon-key",
        "icon-api", "icon-disconnect", "icon-highlight", "icon-monitor", "icon-link", "icon-man",
        "icon-percentage", "icon-pushpin", "icon-phone", "icon-shake", "icon-tag", "icon-wrench",
        "icon-tags", "icon-scissor", "icon-mr", "icon-share", "icon-branches", "icon-fork", "icon-shrink",
        "icon-arrawsalt", "icon-verticalright", "icon-verticalleft", "icon-right", "icon-left",
        "icon-up", "icon-down", "icon-fullscreen", "icon-fullscreen-exit", "icon-doubleleft",
        "icon-doubleright", "icon-arrowright", "icon-arrowup", "icon-arrowleft", "icon-arrowdown",
        "icon-upload", "icon-colum-height", "icon-vertical-align-botto", "icon-vertical-align-middl",
        "icon-totop", "icon-vertical-align-top", "icon-download", "icon-sort-descending",
        "icon-sort-ascending", "icon-fall", "icon-swap", "icon-stock", "icon-rise", "icon-indent",
        "icon-outdent", "icon-menu", "icon-unorderedlist", "icon-orderedlist", "icon-align-right",
        "icon-align-center", "icon-align-left", "icon-pic-center", "icon-pic-right", "icon-pic-left",
        "icon-bold", "icon-font-colors", "icon-exclaimination", "icon-font-size", "icon-check-circle",
        "icon-infomation", "icon-CI", "icon-line-height", "icon-Dollar", "icon-strikethrough", "icon-compass",
        "icon-underline", "icon-close-circle", "icon-number", "icon-frown", "icon-italic", "icon-info-circle",
        "icon-code", "icon-left-circle", "icon-column-width", "icon-down-circle", "icon-check", "icon-EURO",
        "icon-ellipsis", "icon-copyright", "icon-dash", "icon-minus-circle", "icon-close", "icon-meh",
        "icon-enter", "icon-plus-circle", "icon-line", "icon-play-circle", "icon-minus", "icon-question-circle",
        "icon-question", "icon-Pound", "icon-rollback", "icon-right-circle", "icon-small-dash", "icon-smile",
        "icon-pause", "icon-trademark", "icon-bg-colors", "icon-time-circle", "icon-crown", "icon-timeout",
        "icon-drag", "icon-earth", "icon-desktop", "icon-YUAN", "icon-gift", "icon-up-circle", "icon-stop",
        "icon-warning-circle", "icon-fire", "icon-sync", "icon-thunderbolt", "icon-transaction",
        "icon-alipay", "icon-undo", "icon-taobao", "icon-redo", "icon-wechat-fill", "icon-reload",
        "icon-comment", "icon-reloadtime", "icon-login", "icon-message", "icon-clear", "icon-dashboard",
        "icon-issuesclose", "icon-poweroff", "icon-logout", "icon-piechart", "icon-setting",
        "icon-eye", "icon-location", "icon-edit-square", "icon-export", "icon-save", "icon-Import",
        "icon-appstore", "icon-close-square", "icon-down-square", "icon-layout", "icon-left-square",
        "icon-play-square", "icon-control", "icon-codelibrary", "icon-detail", "icon-minus-square",
        "icon-plus-square", "icon-right-square", "icon-project", "icon-wallet", "icon-up-square",
        "icon-calculator", "icon-interation", "icon-check-square", "icon-border", "icon-border-outer",
        "icon-border-top", "icon-border-bottom", "icon-border-left", "icon-border-right", "icon-border-inner",
        "icon-border-verticle", "icon-border-horizontal", "icon-radius-bottomleft", "icon-radius-bottomright",
        "icon-radius-upleft", "icon-radius-upright", "icon-radius-setting", "icon-adduser", "icon-deleteteam",
        "icon-deleteuser", "icon-addteam", "icon-user", "icon-team", "icon-areachart", "icon-linechart",
        "icon-barchart", "icon-pointmap", "icon-container", "icon-atom", "icon-zanwutupian", "icon-safetycertificate",
        "icon-password", "icon-article", "icon-page", "icon-plugin", "icon-admin", "icon-banner"
        """
        self.type = icon_type
        return self