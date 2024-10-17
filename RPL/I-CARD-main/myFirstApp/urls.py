from django.contrib import admin
from django.urls import path, include
from . import views
# from django.http HttpResponse
from django.conf import settings
from django.conf.urls.static import static # type: ignore


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('admin-page/', views.admin_page, name='admin_page'),  # Sesuaikan nama rute dengan views.py
    path('admin/', admin.site.urls),
    path('upload/', views.upload_image, name='upload_image'), # masih blom
    path('image/<int:image_id>/download/', views.download_image, name='download_image'),
    path('image_view/<int:image_id>/', views.image_view, name='image_view'),
    path('show_images/', views.show_images, name='show_images'),  # Define the URL pattern for show_images
    path('image/<int:image_id>/', views.image_view, name='views.image_view'),
    path('image/<int:image_id>/delete/', views.delete_image, name='delete_image'),
    path('image/<int:image_id>/update/', views.update_image, name='update_image'),
    path('card/', views.card, name='card'),
    path('card/create/', views.card_create, name='card_create'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('card/<int:card_id>/update/', views.card_update, name='card_update'),
    path('card/<int:card_id>/delete/', views.card_delete, name='card_delete'),
    path('image/<int:image_id>/download/', views.download_image, name='download_image'),
]
    
   



# Tambahkan ini untuk mendukung menampilkan gambar yang diunggah
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)