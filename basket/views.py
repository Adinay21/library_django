from django.shortcuts import render, redirect, get_object_or_404
from basket.models import BasketModel
from basket.forms import BasketForm

def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            basket = form.save()
            return redirect('basketList')
    else:
        form = BasketForm()
        return render(request, template_name='basket/create_basket.html', context={'form': form})


def basket_list_view(request):
    if request.method == 'GET':
        basket_list = BasketModel.objects.all().order_by('-id')
        context = {'basket_list': basket_list}
        return render(request, template_name='basket/basket_list.html', context=context)


def basket_detail_view(request, id):
    if request.method == 'GET':
        basket_id = get_object_or_404(BasketModel, id=id)
        context = {'basket_id': basket_id}
        return render(request, template_name='basket/basket_detail.html', context=context)


def update_basket_view(request, id):
    basket_id = get_object_or_404(BasketModel, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket_id)
        if form.is_valid():
            basket = form.save()
            return redirect('basketList')
    else:
        form = BasketForm(instance=basket_id)
        return render(request, template_name='basket/basket_update.html', context={
            'basket_id': basket_id,
            'form': form})


def delete_basket_view(request, id):
    basket_id = get_object_or_404(BasketModel, id=id)
    basket_id.delete()
    return redirect('basketList')