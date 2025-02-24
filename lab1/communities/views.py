from django.shortcuts import render
from .models import Communities



def communities_list(request):
    commun = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'commun': commun})

def community_page(request, slug):
    community = Communities.objects.get(slug=slug)
    return render(request, 'communities/community_page.html', {'community': community})