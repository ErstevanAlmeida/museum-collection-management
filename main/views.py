from django.shortcuts import render

def show_main(request):
    context = {
        'apps_name': 'DS Museum Collections',
        'name': 'Erstevan Laurel Lucky Almeida',
        'npm': '2206082493',
        'class': 'PBP - E',
        'collection': 'Wanderer above the Sea of Fog',
        'type': 'Paintings',
        'amount': 1,
        'year': 1818,
        'description': 'Wanderer above the Sea of Fog is a painting by German Romanticist artist Caspar David Friedrich made in 1818. It depicts a man standing upon a rocky precipice with his back to the viewer; he is gazing out on a landscape covered in a thick sea of fog through which other ridges, trees, and mountains pierce, which stretches out into the distance indefinitely.\n(source: Wikipedia)'
    }

    return render(request, "main.html", context)