from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import TripForm


def home(request):
    return render(request, 'destinations/home.html')


def destination_list(request):
    destinations = Destination.objects.all().order_by('-created_at')
    return render(request, 'destinations/list.html', {'destinations': destinations})


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    submitted = False

    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.destination = destination
            trip.save()
            submitted = True
            form = TripForm()  # reset form after successful submit
    else:
        form = TripForm()

    return render(request, 'destinations/detail.html', {
        'destination': destination,
        'form': form,
        'submitted': submitted,
    })
