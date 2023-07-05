from django.shortcuts import render,redirect
from Perfil.models import Categoria,Conta
from django.http import HttpResponse
from .models import Valores
from django.contrib import messages
from django.contrib.messages import constants

def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all() 
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    elif request.method == "POST":
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')
        
        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo,
        )
        
        conta = Conta.objects.get(id=conta)
        if tipo == 'E':
            conta.valor += int(valor)
        elif tipo == 'S':
            conta.valor -= int(valor)
            
        conta.save()

        valores.save()
        messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
        return redirect('/extrato/novo_valor')