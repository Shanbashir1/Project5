from django.shortcuts import render

# Function to alert a error 404 page
def error_404_view(request, exception):
    return render(request, '404.html')


# Function to alert a error 500 page
def error_500_view(request):
    return render(request, '500.html')