from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_student_info(request):
    moodle_login = request.query_params.get('login', None)

    if moodle_login:
        if moodle_login == "is-31fiot-23-083":
            data = {
                "surname": "Сичов",
                "name": "Олександр",
                "course": 2,
                "group": "ІС-31"
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Невірний логін"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Вкажіть логін"}, status=status.HTTP_400_BAD_REQUEST)