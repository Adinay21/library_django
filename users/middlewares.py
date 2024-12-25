from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class ProgerSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            level = str(request.POST.get("level"))
            if level == "jun":
                request.salary = "Зарплата 700$"
            elif level == "middle":
                request.salary = "Зарплата 1000$"
            elif level == "senior":
                request.salary = "Зарплата 2000$"
            else:
                return HttpResponseBadRequest("Поднимите свой уровень")
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "salary", "Зарплата не определена")
