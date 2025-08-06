from django.db import models

class ChatMessage(models.Model):
    user_message = models.TextField(blank=True, null=True)
    bot_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_message[:30]} | Bot: {self.bot_response[:30]}"
