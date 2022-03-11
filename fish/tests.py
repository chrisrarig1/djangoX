from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Fish

class FishTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.fish = Fish.objects.create(
            species="perch", angler=self.user, description="description test", 
        )

    def test_string_representation(self):
        self.assertEqual(str(self.fish), "perch")

    def test_fish_content(self):
        self.assertEqual(f"{self.fish.species}", "perch")
        self.assertEqual(f"{self.fish.angler}", "tester@email.com")
        self.assertEqual(f"{self.fish.description}", "description test")

    def test_fish_list_view(self):
        response = self.client.get(reverse("fish_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "perch")
        self.assertTemplateUsed(response, "fishpage/fish_list.html")

    def test_fish_detail_view(self):
        response = self.client.get(reverse("fish_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Angler: tester")
        self.assertTemplateUsed(response, "fishpage/fish_detail.html")

    def test_fish_create_view(self):
        response = self.client.post(
            reverse("fish_create"),
            {
                "species": "Bass",
                "description": "test",
                "angler": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("fish_detail", args="2"))
