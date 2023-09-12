from django.shortcuts import render

def show_main(request):
    context = {
        'apps_name': 'DS Museum Collections',
        'name': 'Erstevan Laurel Lucky Almeida',
        'class': 'PBP - E'
    }

    return render(request, "main.html", context)