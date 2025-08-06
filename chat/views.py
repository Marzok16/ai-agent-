import os
import uuid
from PIL import Image
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import default_storage
from .models import ChatMessage
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=settings.GEMINI_KEY)

def chat_view(request):
    response = None
    error_message = None

    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        print("📩 Message received:", message)

        try:
            if message:
                model = genai.GenerativeModel(
                    "gemini-1.5-flash",
                    generation_config={
                        "temperature": 0.7,
                        "max_output_tokens": 256,
                        "top_p": 1,
                        "top_k": 40,
                    }
                )
                result = model.generate_content(message)
                response = result.text
                print("🤖 Gemini Response:", response)

                ChatMessage.objects.create(
                    user_message=message,
                    bot_response=response
                )
            else:
                error_message = "Please enter a message."
                print("⚠️ Empty message.")

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            print(f"[Gemini Error] {e}")

    messages = ChatMessage.objects.all().order_by('created_at')
    return render(request, 'chat/index.html', {
        'messages': messages,
        'error_message': error_message,
    })
