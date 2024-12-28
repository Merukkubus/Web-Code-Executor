import time

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import execute_code

def home(request):
    return render(request, 'execute.html')

class CodeExecutionView(APIView):
    def post(self, request):
        try:
            # Получение данных из запроса
            language = request.data.get("language")
            code = request.data.get("code")

            # Проверка наличия данных
            if not language or not code:
                return Response(
                    {"error": "Both 'language' and 'code' are required fields"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Проверка поддерживаемых языков
            if language not in ["python", "javascript"]:
                return Response(
                    {"error": f"Unsupported language: {language}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Выполнение кода
            result = execute_code(language, code)

            # Обработка ошибок выполнения
            if "error" in result:
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            # Общая обработка ошибок
            return Response(
                {"error": f"Server error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )