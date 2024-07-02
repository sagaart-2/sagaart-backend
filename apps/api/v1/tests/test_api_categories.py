from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.api.v1.products.serializers import CategorySerializer
from apps.products.models import Category


class CategoryAPITest(APITestCase):
    """Проверка эндпоинтов категорий."""

    def setUp(self):
        self.client = APIClient()
        self.category_data = {"name": "Test Category"}
        self.category = Category.objects.create(**self.category_data)
        self.url = "/api/v1/categories/"

    def test_get_category_list(self):
        """Тестирование списка категорий."""
        response = self.client.get(self.url)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        """Тестирование удаление категории."""
        response = self.client.delete(f"{self.url}{self.category.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())
