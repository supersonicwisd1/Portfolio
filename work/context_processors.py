from .models import Tag

def project_tags(request):
    tags = Tag.objects.all()

    return {'project_tags': tags}
