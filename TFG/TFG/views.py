"""Project-level views."""

from django.shortcuts import render


def homepage(request):
    """Render the homepage template (home.html)."""
    return render(request, 'home.html')