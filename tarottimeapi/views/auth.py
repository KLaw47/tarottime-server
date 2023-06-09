from tarottimeapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    uid = request.data['uid']

    user = User.objects.filter(uid=uid).first()

    if user is not None:
        data = {
            'id': user.id,
            'name': user.name,
            'uid': user.uid,
        }
        return Response(data)
    else:
        data = {'valid': False}
        return Response(data)

@api_view(['POST'])
def register_user(request):

    user = User.objects.create(
        name=request.data['name'],
        uid=request.data['uid']
    )
    data = {
        'id': user.id,
        'name': user.name,
        'uid': user.uid,
    }
    return Response(data)
