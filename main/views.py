from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275954',
        'name': 'Ida Made Revindra Dikta Mahendra',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)