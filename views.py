from django.shortcuts import render
from django.shortcuts import render
from wishlist.models import BarangWishlist

def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Rafi Nur'
    }

    return render(request, "wishlist.html", context)
    

# Create your views here.
