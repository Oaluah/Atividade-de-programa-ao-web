from django.shortcuts import render
from django.shortcuts import render
from .models import Produto

def lista(request):
    produtos = Produto.objects.select_related("marca", "categoria").all()
    return render(request, "produtos/lista.html", {"produtos": produtos})
