class HandlerGET:
    def __init__(self, func):
        self.infunction = func
    
    def __call__(self, request, *args, **kwargs):
        item = request.get("method","GET")
        if not item or item != "GET":
            return None
        return self.get(self.infunction, request)

    def get(self, func, request, *args, **kwargs):
        print(func(request))
        return f"GET: {func(request)}"


@HandlerGET
def index(request):
    return "главная страница сайта"

res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"