from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        api_request = requests.get(f"https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{ID}")

        try:
            api = json.loads(api_request.content)
            category_description = ""
            category_color = ""

            if api['stIndexLevel']['indexLevelName'] == "Bardzo dobry":
                category_description = "(0-50) Nie istnieje realne zagrożenie dla zdrowia podczas wykonywania jakichkolwiek aktywności na zewnątrz"
                category_color = "bd"
            elif api['stIndexLevel']['indexLevelName'] == "Dobry":
                category_description = "(50,1 - 100) Zanieczyszczenia nie stanowią zagrożenia dla zdrowia lub ryzyko jest niewielkie. Dopuszcza się dowolną aktywność na zewnątrz bez ograniczeń."
                category_color = "db"
            elif api['stIndexLevel']['indexLevelName'] == "Umiarkowany":
                category_description = "(100,1-200) Akceptowalna jakość powietrza, ale zanieczyszczenie może być zagrożeniem dla osób szczególnie wrażliwych (starszych, chorych, kobiet w ciąży i małych dzieci). Warto częściowo ograniczyć aktywność na wolnym powietrzu"
                category_color = "um"
            elif api['stIndexLevel']['indexLevelName'] == "Dostateczny":
                category_description = "(200,1 - 350) Zanieczyszczenie stanowi już zagrożenie dla zdrowia, zwłaszcza dla grup wrażliwych. Aktywność na wolnym powietrzu powinna zostać skrócona do minimum, zwłaszcza jeśli jest to intensywny wysiłek fizyczny"
                category_color = "dost"
            elif api['stIndexLevel']['indexLevelName'] == "Zły":
                category_description = "(350,1 - 500 ) Zanieczyszczenie jest na tyle duże, że osoby osoby chore lub starsze, kobiety w ciąży oraz małe dzieci powinny unikać przebywania na zewnątrz, pozostali spoza grupy ryzyka natomiast ograniczyć je do minimum. Najlepiej zupełnie zrezygnować z uprawiania sportu na wolnym powietrzu."
                category_color = "zły"
            elif api['stIndexLevel']['indexLevelName'] == "Bardzo zły":
                category_description = "(> 500) Jakość powietrza, która powoduje problemy ze zdrowiem. Może prowadzić do zaburzeń ze strony układów oddechowego, naczyniowo-sercowego oraz odpornościowego. Przebywanie na zewnątrz należy ograniczyć do niezbędnego minimum."
                category_color = "bzły"

            return render(request, 'home.html', {
                'api': api,
                'category_description': category_description,
                'category_color': category_color
            })

        except Exception as e:
            api = "Error..."
            category_description = "Wystąpił błąd podczas pobierania danych"

            return render(request, 'home.html', {
                'api': api,
                'category_description': category_description
            })
    else:
        return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {})
