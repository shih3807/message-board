from fastapi import UploadFile, File, Form, Request

from backend.models.message_model import MessageModel
from backend.services.storage_service import StorageService


class MessageController:
    # 創建訊息
    @staticmethod
    async def create_message(
        request: Request,
        username: str = Form(None),
        content: str = Form(None),
        image: UploadFile = File(None),
    ):
        if not content and not image:
            return {"error": True, "msg": "content cannot be empty"}

        try:
            image_url = StorageService.save_image(image)

            result = MessageModel.create_message(
                username=username, content=content, image_url=image_url
            )

            if result.get("error"):
                return result

            return {"success": True, "msg": "message created"}
        except Exception as e:
            return {"error": True, "msg": str(e)}
