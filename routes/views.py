from django.shortcuts import render
from .models import Airport
from .forms import (
    AirportNodeForm,
    DirectionSearchForm,
)

from django.shortcuts import redirect
from django.contrib import messages

# Add Airport Node (Root / Left / Right)

def add_airport_node(request):
    if request.method == "POST":
        form = AirportNodeForm(request.POST)

        if form.is_valid():
            parent = form.cleaned_data['parent_airport']
            position = form.cleaned_data['position']
            airport_code = form.cleaned_data['airport_code']
            duration = form.cleaned_data['duration']

            # Root node
            if not parent:
                Airport.objects.create(
                    airport_code=airport_code,
                    duration=duration
                )
                messages.success(request, "Root airport added successfully")
                return redirect('routes:add_airport')

            # Check if position already exists
            if Airport.objects.filter(parent=parent, position=position).exists():
                messages.error(
                    request,
                    f"{position.capitalize()} node already exists for {parent.airport_code}"
                )
                return redirect('routes:add_airport')

            Airport.objects.create(
                airport_code=airport_code,
                duration=duration,
                parent=parent,
                position=position
            )

            messages.success(request, "Airport node added successfully")
            return redirect('routes:add_airport')

    else:
        form = AirportNodeForm()

    return render(request, "routes/add_airport.html", {"form": form})




# 1. Find Nth Left or Right Node

def nth_node_search(request):
    result = None

    if request.method == "POST":
        form = DirectionSearchForm(request.POST)

        if form.is_valid():
            current = form.cleaned_data['start_airport']
            direction = form.cleaned_data['direction']

            # Strict directional traversal

            while True:
                next_node = current.children.filter(position=direction).first()

                if not next_node:
                    result = current
                    break

                current = next_node
    else:
        form = DirectionSearchForm()

    return render(
        request,
        "routes/nth_node.html",
        {
            "form": form,
            "result": result
        }
    )


# 2. Finds the longest route node across ALL airports.

def longest_node(request):

    result = Airport.objects.order_by('-duration').first()

    return render(request, 'routes/longest_route.html', {
        'longest': result
    })


# 3. Shortest Node Between Two Airports

def shortest_node(request):
    shortest = Airport.objects.exclude(parent__isnull=True).order_by('duration').first()

    return render(
        request,
        "routes/shortest_node.html",
        {
            "shortest": shortest
        }
    )
