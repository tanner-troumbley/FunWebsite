from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import API_form
from .models import API

# Create your views here.
def api_tree_view(request):

    record_list = API.objects.order_by('-name')
    if request.method == "POST":
        form = API_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('api')
    form = API_form()

    page = {
        "forms": form,
        "list": record_list,
        "Title": "APIs"
    }
    request.render(request, "API/list_view.html", page)

def api_delete(request, record_id):
    record = API.objects.get(id=record_id)
    # messages.info(f"Deleting API {record.name}.")
    record.delet()
    return api_tree_view(request)
