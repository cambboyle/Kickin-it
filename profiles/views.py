from django.shortcuts import render


def profile(request):
    """A view to show the user's profile"""

    return render(request, 'profiles/profile.html')
    context = {}

    return render(request, 'profiles/profile.html', context)
