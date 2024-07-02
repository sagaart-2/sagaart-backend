from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.api.v1.products.serializers import StyleSerializer
from apps.products.models import Style


class StyleAPITest(APITestCase):
    """Проверка эндпоинтов стилей."""

    def setUp(self):
        self.client = APIClient()
        self.style_data = {"name": "Test Style"}
        self.style = Style.objects.create(**self.style_data)
        self.url = "/api/v1/styles/"

    def test_get_style_list(self):
        """Тестирование списка стилей."""
        response = self.client.get(self.url)
        styles = Style.objects.all()
        serializer = StyleSerializer(styles, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_style(self):
        """Тестирование удаление стиля."""
        response = self.client.delete(f"{self.url}{self.style.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Style.objects.filter(id=self.style.id).exists())
