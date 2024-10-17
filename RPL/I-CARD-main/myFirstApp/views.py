from django.shortcuts import render, redirect

from core import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from django.http import HttpResponse
from .forms import ImageUploadForm
from django.contrib import messages
import os
from datetime import date
from django.contrib.auth.decorators import login_required
from .models import Image
from .forms import ImageUploadForm
from django.contrib.auth import get_user_model  # Impor get_user_model di sini
from .forms import ImageForm
from .models import Account  # Impor model Account
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction





def index(request):
    user = request.user
    if isinstance(user, AnonymousUser):
        # Jika pengguna belum login, tampilkan tombol login
        return render(request, 'index.html', {'user': None})
    else:
        # Jika pengguna sudah login, tampilkan tombol logout
        return render(request, 'index.html', {'user': user})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_staff:
                    return redirect(reverse('admin_page'))  # Ubah menjadi reverse('admin_page')
                else:
                    return redirect('index')  # Redirect ke halaman setelah login untuk pengguna biasa
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Setelah register, redirect ke halaman login
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')

def admin_page(request):
    return render(request, 'admin-page.html')

def show_images(request):
    image_type = request.GET.get('image_type')

    if image_type:
        images = Image.objects.filter(image_type=image_type)
    else:
        images = Image.objects.all()

    return render(request, 'show_images.html', {'images': images})


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            uploader = request.user  # Menggunakan user yang terkait dengan permintaan saat ini
            image_type = form.cleaned_data['image_type']  # Menambahkan image_type
            new_image = Image(title=title, image=image, uploader=uploader, image_type=image_type)  # Menyertakan image_type saat membuat objek Image
            new_image.save()
            return redirect('show_images')  # Mengalihkan ke halaman show_images setelah upload
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})


def image_view(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    context = {
        'image': image,
        'image_type': image.image_type  # Menambahkan image_type ke konteks
    }
    return render(request, 'image_view.html', context)


    # image = get_object_or_404(Image, id=image_id)  # Retrieve the specific image
    # return render(request, 'image_view.html', {'image': image})
    

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def update_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.user.is_superuser:  # Memeriksa apakah pengguna adalah superuser
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES, instance=image)
            if form.is_valid():
                form.save()
                return redirect('image_view', image_id=image.id)
        else:
            form = ImageForm(instance=image)
    else:
        form = None  # Jika bukan superuser, form diatur menjadi None
        
    return render(request, 'update_image.html', {'form': form, 'image': image})

@staff_member_required
@transaction.atomic
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('show_images')


from PIL import Image as PILImage, ImageDraw, ImageFont
import os
from django.http import HttpResponse
from django.conf import settings
from .models import Image as MyImage

def download_image(request, image_id):
    try:
        # Ambil objek gambar dari database berdasarkan ID
        image = MyImage.objects.get(id=image_id)
        # Path lengkap menuju file gambar
        image_path = os.path.join(settings.MEDIA_ROOT, str(image.image))
        
        # Buka gambar
        img = PILImage.open(image_path)
        
        # Periksa apakah parameter teks diteruskan melalui URL
        text = request.GET.get('text', '')
        if text:
            # Hitung lebar dan tinggi gambar
            image_width, image_height = img.size
            
            # Hitung lebar dan tinggi teks
            font = ImageFont.truetype("arial.ttf", 36)  # Ganti dengan jenis font yang diinginkan dan ukuran font
            text_width, text_height = font.getsize(text)
            
            # Hitung posisi teks di tengah gambar
            x_position = (image_width - text_width) // 2
            y_position = (image_height - text_height) // 2
            
            # Tambahkan teks ke gambar
            draw = ImageDraw.Draw(img)
            draw.text((x_position, y_position), text, fill="black", font=font)
            
            # Konversi gambar ke mode RGB jika mode RGBA
            if img.mode == 'RGBA' or img.mode == 'P':
                img = img.convert('RGB')
            
            # Simpan gambar yang telah dimodifikasi
            modified_image_path = os.path.join(settings.MEDIA_ROOT, 'modified_image.jpg')
            img.save(modified_image_path)
            
            # Berikan gambar yang dimodifikasi kepada pengguna sebagai respons
            with open(modified_image_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type="image/jpeg")
                filename = "modified_image.jpg" if not text else "modified_certificate_{}.jpg".format(text)
                response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
                return response
        
    except MyImage.DoesNotExist:
        return HttpResponse("Image not found", status=404)




from .models import Card

def card(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'card.html', context)

def card_create(request):
    if request.method == 'POST':
        # Memproses data form yang disubmit
        message = request.POST.get('message', '')  
        image_id = request.POST.get('image_id', None)
        user = request.user

        # Membuat objek kartu baru dengan data yang diberikan
        card = Card.objects.create(message=message, image_id=image_id, user=user)
        
        # Mengarahkan pengguna ke halaman detail kartu yang baru saja dibuat
        return JsonResponse({'success': True, 'message': 'Card successfully created.'})
    else:
        # Jika metode bukan POST, kembalikan respons yang sesuai
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed for this endpoint.'}) 



def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    context = {
        'card': card,
    }
    return render(request, 'image_view.html', context)

def card_update(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        message = request.POST.get('message', '')
        image_id = request.POST.get('image_id', None)  # Ambil ID gambar dari formulir

        # Perbarui atribut Card dengan data yang diberikan
        card.message = message
        card.image_id = image_id
        card.save()
        return redirect('card_detail', card_id=card_id)
    else:
        context = {
            'card': card,
        }
        return render(request, 'card_update.html', context)

def card_delete(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    card.delete()
    return redirect('card')
