from django.urls import path
from . import views

app_name = "routes"

urlpatterns = [
    # Add a new airport node (root / left / right)
    path("add/", views.add_airport_node, name="add_airport"),
    # Find the last reachable node 
    path('nth/', views.nth_node_search, name='nth_node_search'),
    # Display the airport node with the highest duration
    path('longest/', views.longest_node, name='longest_node'),
    # Display the shortest route between two airports
    path('shortest/', views.shortest_node, name='shortest_node'),
]
