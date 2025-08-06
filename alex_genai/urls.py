from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),      # Admin panel at /admin/
    path('chat/', include('chat.urls')),  # Your chatbot available at /chat/
]
