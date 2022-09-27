class RenderList:
    def __init__(self,type_list='ul'):
        self.type_list=type_list

    def __call__(self, *args, **kwargs):
        if self.type_list.strip()=='ol':
            a='ol'
        else:
            a='ul'

        d=f'<{a}>\n'
        for i in args[0]:
            d+=f'<li>{i}</li>\n'
        d+=f'/<{a}>\n'
        return d

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList('ol')
html = render(lst)
print(html)