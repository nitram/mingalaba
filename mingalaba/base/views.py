import json

from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
from django.http import JsonResponse

from wagtail.images.models import Image


# Return image data of certain image id
def get_image(image_id):
    image_data = dict(Image.objects.filter(id=image_id).values(
            'title',
            'file',
            'width',
            'height')[0])
    
    return image_data


# Create your views here.
# View of url: gtimg/
def load_image(request, image_id):
    return JsonResponse(get_image(image_id), safe=False)