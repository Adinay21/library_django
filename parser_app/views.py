from django.shortcuts import render, HttpResponse
from . import models, forms
from django.views import generic


class TopListView(generic.ListView):
    template_name = 'parser/top_list.html'
    context_object_name = 'top'
    model = models.TopModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class TopFormView(generic.FormView):
    template_name = 'parser/top_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('STATUS 200')
        else:
            return super(TopFormView, self).post(request, *args, **kwargs)
