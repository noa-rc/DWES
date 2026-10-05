"""Views for the showcase app."""

from django.shortcuts import render


def showcase(request):
    """Render the showcase page."""
    return render(request, 'showcase/showcase.html')