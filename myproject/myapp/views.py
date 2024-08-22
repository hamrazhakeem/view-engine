from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'home.html')

def cards_view(request):
    card_data = [
       {'title': 'Australia', 'text': 'The Last Frontier', 'link': '#', 'image': 'download.jpeg'},
        {'title': 'Singapore', 'text': 'The Asian Crossroads', 'link': '#', 'image': 'download (1).jpeg'},
        {'title': 'Japan', 'text': 'A Beacon of Innovation', 'link': '#', 'image': 'download (2).jpeg'},
    ]
    return render(request,'cards.html',{'card_data': card_data})

def tables_view(request):
    table_data = [
        {'id': 1, 'first_name': 'Fauz', 'last_name': 'Abdul', 'handle': '@fauz_abdul'},
        {'id': 2, 'first_name': 'Hamraz', 'last_name': 'Hakeem', 'handle': '@hamraz_hakeem'},
        {'id': 3, 'first_name': 'Anurag', 'last_name': '', 'handle': '@anurag'},
    ]
    return render(request, 'tables.html', {'table_data': table_data})