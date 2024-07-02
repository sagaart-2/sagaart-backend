from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from apps.products.models import Artist, GroupShow, SoloShow


class ArtistAPITest(APITestCase):
    """Проверка эндпоинтов художников."""

    def setUp(self):
        self.artist_data = {
            "name": "test_name",
            "lastname": "test_lastname",
            "gender": "male",
            "bio": "test_bio",
            "photo": SimpleUploadedFile(
                "photo.jpg", b"file_content", content_type="image/jpeg"
            ),
            "phone": "+79999999999",
            "email": "testemail@gmail.com",
            "date_of_birth": "1995-01-01",
            "city_of_birth": "Moscow",
            "city_of_residence": "Moscow",
            "country": "Russia",
            "education": "some",
            "art_education": "some",
            "teaching_experience": "yes",
            "personal_style": "No",
            "collected_by_private_collectors": True,
            "collected_by_major_institutions": False,
            "industry_award": "Best Artist 2020",
            "social": "https://example.com",
            "password": "123",
        }
        self.artist = Artist.objects.create(**self.artist_data)
        self.solo_show = SoloShow.objects.create(
            title="Solo Show 1",
            place="Gallery A",
            city="Moscow",
            country="Russia",
            year=2020,
        )
        self.group_show = GroupShow.objects.create(
            title="Group Show 1",
            place="Gallery B",
            city="Moscow",
            country="Russia",
            year=2019,
        )
        self.artist.solo_shows.add(self.solo_show)
        self.artist.group_shows.add(self.group_show)
        self.url = "/api/v1/artists/"

    def test_get_artist(self):
        """Тестирование получения данных художника."""
        self.url = f"/api/v1/artists/{self.artist.pk}/"
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.artist.name)

    def test_update_artist(self):
        """Тестирование обновления художника."""
        self.url = f"/api/v1/artists/{self.artist.pk}/"
        updated_data = {"name": "Nikita"}
        response = self.client.patch(self.url, updated_data, format="json")
        if response.status_code != status.HTTP_200_OK:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.artist.refresh_from_db()
        self.assertEqual(self.artist.name, "Nikita")

    def test_delete_artist(self):
        """Тестирование удаление художника."""
        self.url = f"/api/v1/artists/{self.artist.pk}/"
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artist.objects.count(), 0)

    def test_invalid_data(self):
        """Тестирование данных."""
        invalid_data = self.artist_data.copy()
        invalid_data["email"] = "invalid-email"
        response = self.client.post(self.url, invalid_data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
