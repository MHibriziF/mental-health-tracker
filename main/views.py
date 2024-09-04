from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165585',
        'name': 'Muhammad Hibrizi Farghana',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
