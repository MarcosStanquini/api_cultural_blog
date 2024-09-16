from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Certo, barra no final
    path('blog/', include('blog.urls')),  # Adicione a barra no final
]
