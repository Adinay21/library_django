from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache



from django.shortcuts import render, redirect, get_object_or_404
from basket.models import BasketModel
from basket.forms import BasketForm
from django.views import generic


@method_decorator(cache_page(60 * 15), name='dispatch')
class CreateBasketView(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        creates = cache.get('creates')
        if not creates:
            creates = super(CreateBasketView, self).form_valid(form=form)
            cache.set('creates', creates, 60 * 15)
        return creates



# def create_basket_view(request):
#     if request.method == 'POST':
#         form = BasketForm(request.POST, request.FILES)
#         if form.is_valid():
#             basket = form.save()
#             return redirect('basketList')
#     else:
#         form = BasketForm()
#         return render(request, template_name='basket/create_basket.html', context={'form': form})

@method_decorator(cache_page(60 * 15), name='dispatch')
class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = BasketModel

    def get_queryset(self):
        baskets = cache.get('baskets')
        if not baskets:
            baskets = self.model.objects.all().order_by('-id')
            cache.set('baskets', baskets, 60 * 15)
        return baskets

# def basket_list_view(request):
#     if request.method == 'GET':
#         basket_list = BasketModel.objects.all().order_by('-id')
#         context = {'basket_list': basket_list}
#         return render(request, template_name='basket/basket_list.html', context=context)

@method_decorator(cache_page(60 * 15), name='dispatch')
class BasketDetailView(generic.DetailView):
    template_name = 'basket/basket_detail.html'
    context_object_name = 'basket_id'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        details = cache.get('details')
        if not details:
            details = get_object_or_404(BasketModel, id=basket_id)
            cache.set('details')
        return

# def basket_detail_view(request, id):
#     if request.method == 'GET':
#         basket_id = get_object_or_404(BasketModel, id=id)
#         context = {'basket_id': basket_id}
#         return render(request, template_name='basket/basket_detail.html', context=context)

@method_decorator(cache_page(60 * 15), name='dispatch')
class UpdateBasketView(generic.UpdateView):
    template_name = 'basket/basket_update.html'
    form_class = BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        updates = cache.get('updates')
        if not updates:
            updates = super(UpdateBasketView, self).form_valid(form=form)
            cache.set('updates', updates, 60 * 15)
        return updates

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(BasketModel, id=basket_id)

# def update_basket_view(request, id):
#     basket_id = get_object_or_404(BasketModel, id=id)
#     if request.method == 'POST':
#         form = BasketForm(request.POST, instance=basket_id)
#         if form.is_valid():
#             basket = form.save()
#             return redirect('basketList')
#     else:
#         form = BasketForm(instance=basket_id)
#         return render(request, template_name='basket/basket_update.html', context={
#             'basket_id': basket_id,
#             'form': form})

@method_decorator(cache_page(60 * 15), name='dispatch')
class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/basket_list/'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        deletes = cache.get('deletes')
        if not deletes:
            deletes = get_object_or_404(BasketModel, id=basket_id)
            cache.set('deletes', deletes, 60 * 15)
        return deletes

# def delete_basket_view(request, id):
#     basket_id = get_object_or_404(BasketModel, id=id)
#     basket_id.delete()
#     return redirect('basketList')


def clear_basket_cache(sender, **kwargs):
    cache.delete('baskets')
    cache.delete('creates')
    cache.delete('details')
    cache.delete('updates')
    cache.delete('deletes')