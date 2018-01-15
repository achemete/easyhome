from django.shortcuts import render
from appApi.serializers import UsersSerializer, AccomodationsSerializer,ReviewsSerializer,ServicesSerializer,AttractionsSerializer,RestaurantSerializer,DealSerializer
from rest_framework import viewsets
from appApi.models import Users,Reviews,Accomodations,Services,Attractions,Restaurant,Deal
class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

"""import django_filters.rest_framework"""
from rest_framework import generics

from django.views.generic import ListView

class AccomodationsListView(ListView):
    model = Accomodations
    template_name = 'frontend/templates/frontend/index.html'
    context_object_name = 'accomodations'

def SearchView(request):
    city = request.GET.get('searched')
    accomodations = Accomodations.objects.all()
    context = {'city': city,'accomodations': accomodations}
    return render(request, "frontend/templates/frontend/template.html", context)
"""
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class AccomodationsListView(generics.ListAPIView):
    queryset = Accomodations.objects.all()
    serializer_class = AccomodationsSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('city', 'price')
    def json_search(request):
        query = request.GET.get('query')
        url = 'https://127.0.0.1/search/'
        locality = query.replace(' ', '%20')
        final_url = url + "&locality=" + locality
        json_obj = urllib2.urlopen(final_url)
        decoded_data = json.load(json_obj)
        return render(request, 'https://127.0.0.1/search/',{'objects': decoded_data['objects']})
"""

class ReviewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
class AccomodationsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Accomodations.objects.all()
    serializer_class = AccomodationsSerializer
# Create your views here.

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class AttractionsViewSet(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
