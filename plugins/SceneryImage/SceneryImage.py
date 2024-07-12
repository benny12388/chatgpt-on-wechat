# encoding:utf-8
import requests
import plugins
from bridge.context import ContextType, EventContext, Event, EventAction
from bridge.reply import Reply, ReplyType
from common.log import logger

@plugins.register(
    name="风景图片",
    desire_priority=0,
    desc="输入关键词'风景图片'即可获取随机风景图片的链接",
    version="1.0",
    author="WolfmanAI"
)
class SceneryImage(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[SceneryImage-WolfmanAI] inited.")

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content  # 获取事件上下文中的消息内容
        if content == "风景图片":  # 如果消息内容为 "风景图片"
            api_url = "https://api.vvhan.com/api/wallpaper/views?type=json"  # 使用提供的JSON格式接口地址
            response = requests.get(api_url)
            if response.status_code == 200:
                image_data = response.json()  # 解析JSON格式的响应数据
                if image_data.get("success"):
                    # 构建JSON格式的回复内容
                    reply_content = {
                        "type": image_data.get("type"),  # 图片类型
                        "url": image_data.get("url")  # 图片URL
                    }
                    reply = Reply()
                    reply.type = ReplyType.TEXT  # 假设ReplyType.TEXT可以返回JSON字符串
                    reply.content = reply_content  # 直接使用字典作为回复内容

                    e_context["reply"] = reply
                    e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑
                else:
                    logger.error("API response does not indicate success.")
            else:
                logger.error(f"Failed to fetch image data, status code: {response.status_code}")

    def get_help_text(self, **kwargs):
        help_text = "关键词【风景图片】获取随机风景图片链接 - By WolfmanAI"
        return help_text