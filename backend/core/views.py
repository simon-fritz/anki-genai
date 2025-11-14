from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Anki GenAI — Backend</h1><p>Minimal Django scaffold is running.</p>')
