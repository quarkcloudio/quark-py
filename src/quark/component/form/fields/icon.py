from typing import Any, Dict, List, Optional

from pydantic import model_validator

from .base import Base


class Icon(Base):

    component: str = "iconField"
    """
    组件名称
    """

    default_value: Optional[Any] = None
    """
    默认的选中项
    """

    disabled: bool = False
    """
    整组失效，默认 False
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    placeholder: Optional[str] = None
    """
    占位符
    """

    size: str = ""
    """
    大小，large | middle | small，默认
    """

    allow_clear: bool = True
    """
    是否支持清除，默认 True
    """

    allow_search: bool = True
    """
    是否支持搜索，默认 True
    """

    options: List[str] = []
    """
    可选项数据源
    """

    @model_validator(mode="after")
    def init(self):
        self.options = [
		"ant-design:database-outlined", "ant-design:mobile-outlined", "ant-design:tablet-outlined", "ant-design:red-envelope-outlined",
		"ant-design:book-outlined", "ant-design:file-done-outlined", "ant-design:reconciliation-outlined",
		"ant-design:file-sync-outlined", "ant-design:file-search-outlined", "ant-design:solution-outlined", "ant-design:file-protect-outlined",
		"ant-design:file-add-outlined", "ant-design:file-excel-outlined", "ant-design:file-exclamation-outlined", "ant-design:file-pdf-outlined",
		"ant-design:file-image-outlined", "ant-design:file-markdown-outlined", "ant-design:file-unknown-outlined", "ant-design:file-ppt-outlined",
		"ant-design:file-word-outlined", "ant-design:file-outlined", "ant-design:file-zip-outlined", "ant-design:file-text-outlined", "ant-design:copy-outlined",
		"ant-design:snippets-outlined", "ant-design:audit-outlined", "ant-design:diff-outlined", "ant-design:security-scan-outlined",
		"ant-design:property-safety-outlined", "ant-design:insurance-outlined", "ant-design:alert-outlined", "ant-design:delete-outlined", "ant-design:hourglass-outlined",
		"ant-design:bulb-outlined", "ant-design:experiment-outlined", "ant-design:bell-outlined", "ant-design:trophy-outlined", "ant-design:rest-outlined", "ant-design:usb-outlined",
		"ant-design:skin-outlined", "ant-design:home-outlined", "ant-design:bank-outlined", "ant-design:filter-outlined", "ant-design:funnel-plot-outlined", "ant-design:like-outlined",
		"ant-design:dislike-outlined", "ant-design:unlock-outlined", "ant-design:lock-outlined", "ant-design:customer-service-outlined", "ant-design:flag-outlined",
		"ant-design:money-collect-outlined", "ant-design:medicine-box-outlined", "ant-design:shop-outlined", "ant-design:rocket-outlined", "ant-design:shopping-outlined",
		"ant-design:folder-outlined", "ant-design:folder-open-outlined", "ant-design:folder-add-outlined", "ant-design:deployment-unit-outlined",
		"ant-design:account-book-outlined", "ant-design:contacts-outlined", "ant-design:carry-out-outlined",
		"ant-design:calendar-outlined", "ant-design:scan-outlined", "ant-design:select-outlined", "ant-design:box-plot-outlined", "ant-design:build-outlined", "ant-design:sliders-outlined",
		"ant-design:laptop-outlined", "ant-design:barcode-outlined", "ant-design:camera-outlined", "ant-design:cluster-outlined", "ant-design:gateway-outlined", "ant-design:car-outlined",
		"ant-design:printer-outlined", "ant-design:read-outlined", "ant-design:cloud-server-outlined", "ant-design:cloud-upload-outlined", "ant-design:cloud-outlined",
		"ant-design:cloud-download-outlined", "ant-design:cloud-sync-outlined", "ant-design:notification-outlined", "ant-design:sound-outlined",
		"ant-design:radar-chart-outlined", "ant-design:qrcode-outlined", "ant-design:fund-outlined", "ant-design:mail-outlined", "ant-design:table-outlined",
		"ant-design:idcard-outlined", "ant-design:credit-card-outlined", "ant-design:heart-outlined", "ant-design:block-outlined", "ant-design:star-outlined",
		"ant-design:gold-outlined", "ant-design:heat-map-outlined", "ant-design:wifi-outlined", "ant-design:edit-outlined", "ant-design:key-outlined",
		"ant-design:api-outlined", "ant-design:disconnect-outlined", "ant-design:highlight-outlined", "ant-design:monitor-outlined", "ant-design:link-outlined", "ant-design:man-outlined",
		"ant-design:percentage-outlined", "ant-design:pushpin-outlined", "ant-design:phone-outlined", "ant-design:shake-outlined", "ant-design:tag-outlined",
		"ant-design:tags-outlined", "ant-design:scissor-outlined", "ant-design:share-alt-outlined", "ant-design:branches-outlined", "ant-design:fork-outlined", "ant-design:shrink-outlined",
		"ant-design:vertical-right-outlined", "ant-design:vertical-left-outlined", "ant-design:right-outlined", "ant-design:left-outlined",
		"ant-design:up-outlined", "ant-design:down-outlined", "ant-design:fullscreen-outlined", "ant-design:fullscreen-exit-outlined", "ant-design:double-left-outlined",
		"ant-design:double-right-outlined", "ant-design:arrow-right-outlined", "ant-design:arrow-up-outlined", "ant-design:arrow-left-outlined", "ant-design:arrow-down-outlined",
		"ant-design:upload-outlined", "ant-design:column-height-outlined", "ant-design:vertical-align-bottom-outlined", "ant-design:vertical-align-middle-outlined",
		"ant-design:to-top-outlined", "ant-design:vertical-align-top-outlined", "ant-design:download-outlined", "ant-design:sort-descending-outlined",
		"ant-design:sort-ascending-outlined", "ant-design:fall-outlined", "ant-design:swap-outlined", "ant-design:stock-outlined", "ant-design:rise-outlined",
		"ant-design:menu-outlined", "ant-design:unordered-list-outlined", "ant-design:ordered-list-outlined", "ant-design:align-right-outlined",
		"ant-design:align-center-outlined", "ant-design:align-left-outlined", "ant-design:pic-center-outlined", "ant-design:pic-right-outlined", "ant-design:pic-left-outlined",
		"ant-design:bold-outlined", "ant-design:font-colors-outlined", "ant-design:exclamation-outlined", "ant-design:font-size-outlined", "ant-design:check-circle-outlined",
		"ant-design:info-outlined", "ant-design:ci-outlined", "ant-design:line-height-outlined", "ant-design:dollar-outlined", "ant-design:strikethrough-outlined", "ant-design:compass-outlined",
		"ant-design:underline-outlined", "ant-design:close-circle-outlined", "ant-design:number-outlined", "ant-design:frown-outlined", "ant-design:italic-outlined", "ant-design:info-circle-outlined",
		"ant-design:code-outlined", "ant-design:left-circle-outlined", "ant-design:column-width-outlined", "ant-design:down-circle-outlined", "ant-design:check-outlined",
		"ant-design:ellipsis-outlined", "ant-design:copyright-outlined", "ant-design:dash-outlined", "ant-design:minus-circle-outlined", "ant-design:close-outlined", "ant-design:meh-outlined",
		"ant-design:enter-outlined", "ant-design:plus-circle-outlined", "ant-design:line-outlined", "ant-design:play-circle-outlined", "ant-design:minus-outlined", "ant-design:question-circle-outlined",
		"ant-design:question-outlined", "ant-design:pound-outlined", "ant-design:rollback-outlined", "ant-design:right-circle-outlined", "ant-design:small-dash-outlined", "ant-design:smile-outlined",
		"ant-design:pause-outlined", "ant-design:trademark-outlined", "ant-design:bg-colors-outlined", "ant-design:field-time-outlined", "ant-design:crown-outlined",
		"ant-design:drag-outlined", "ant-design:desktop-outlined", "ant-design:gift-outlined", "ant-design:up-circle-outlined", "ant-design:stop-outlined",
		"ant-design:warning-outlined", "ant-design:fire-outlined", "ant-design:sync-outlined", "ant-design:thunderbolt-outlined", "ant-design:transaction-outlined",
		"ant-design:alipay-outlined", "ant-design:undo-outlined", "ant-design:taobao-outlined", "ant-design:redo-outlined", "ant-design:wechat-outlined", "ant-design:reload-outlined",
		"ant-design:comment-outlined", "ant-design:login-outlined", "ant-design:message-outlined", "ant-design:clear-outlined", "ant-design:dashboard-outlined",
		"ant-design:issues-close-outlined", "ant-design:poweroff-outlined", "ant-design:logout-outlined", "ant-design:pie-chart-outlined", "ant-design:setting-outlined",
		"ant-design:eye-outlined", "ant-design:export-outlined", "ant-design:save-outlined", "ant-design:import-outlined",
		"ant-design:appstore-outlined", "ant-design:close-square-outlined", "ant-design:down-square-outlined", "ant-design:layout-outlined", "ant-design:left-square-outlined",
		"ant-design:play-square-outlined", "ant-design:control-outlined", "ant-design:minus-square-outlined",
		"ant-design:plus-square-outlined", "ant-design:right-square-outlined", "ant-design:project-outlined", "ant-design:wallet-outlined", "ant-design:up-square-outlined",
		"ant-design:calculator-outlined", "ant-design:interaction-outlined", "ant-design:check-square-outlined", "ant-design:border-outlined", "ant-design:border-outer-outlined",
		"ant-design:border-top-outlined", "ant-design:border-bottom-outlined", "ant-design:border-left-outlined", "ant-design:border-right-outlined", "ant-design:border-inner-outlined",
		"ant-design:border-verticle-outlined", "ant-design:border-horizontal-outlined", "ant-design:radius-bottomleft-outlined", "ant-design:radius-bottomright-outlined",
		"ant-design:radius-upleft-outlined", "ant-design:radius-upright-outlined", "ant-design:radius-setting-outlined", "ant-design:user-add-outlined", "ant-design:usergroup-delete-outlined",
		"ant-design:user-delete-outlined", "ant-design:usergroup-add-outlined", "ant-design:user-outlined", "ant-design:area-chart-outlined", "ant-design:line-chart-outlined",
		"ant-design:bar-chart-outlined", "ant-design:container-outlined", "ant-design:safety-certificate-outlined",
        ]
        self.set_width("200px")
        self.set_key()
        return self

    def set_width(self, width: Any):
        """
        设置组件宽度。

        Args:
            width (Any): 宽度值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        style: Dict[str, Any] = {}
        if self.style:
            style = self.style.copy()
        style["width"] = width
        self.style = style
        return self

    def set_options(self, options: List[str]):
        """
        设置可选项数据源。

        Args:
            options (List[str]): 可选项列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.options = options
        return self

    def set_placeholder(self, placeholder: str):
        """
        设置输入框占位文本。

        Args:
            placeholder (str): 占位文本内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.placeholder = placeholder
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
