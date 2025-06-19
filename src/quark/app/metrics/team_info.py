from quark.component.descriptions.fields.text import Text
from quark.template.metric.descriptions import Descriptions


class TeamInfo(Descriptions):
    title: str = "团队信息"
    col: int = 12

    async def calculate(self):
        return self.result(
            [
                Text().set_label("作者").set_value("tangtanglove"),
                Text().set_label("联系方式").set_value("dai_hang_love@126.com"),
                Text()
                .set_label("官方网址")
                .set_value(
                    "<a href='https://quarkcloud.io' target='_blank'>quarkcloud.io</a>"
                ),
                Text()
                .set_label("文档地址")
                .set_value(
                    "<a href='https://quarkcloud.io' target='_blank'>查看文档</a>"
                ),
                Text()
                .set_label("BUG反馈")
                .set_value(
                    "<a href='https://github.com/quarkcloudio/quark-py/issues' target='_blank'>提交BUG</a>"
                ),
                Text()
                .set_label("代码仓储")
                .set_value(
                    "<a href='https://github.com/quarkcloudio/quark-py' target='_blank'>Github</a>"
                ),
            ]
        )
