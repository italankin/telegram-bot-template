import os


class Config:
    bot_token: str
    admin_id: int

    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.admin_id = int(os.getenv('TELEGRAM_ADMIN_ID', "-1"))
