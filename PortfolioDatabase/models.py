from django.db import models

class Portfolio(models.Model):
    project_title = models.CharField(max_length=200)
    project_desc = models.TextField()
    project_image = models.TextField(default='https://example.com/default-image.jpg')
    project_paragraph = models.TextField(default='default paragraph')

    def __str__(self):
        return self.project_title

    def project_summary(self):
        return {
            "title": self.project_title,
            "description": self.project_desc,
            "image": self.project_image,
            "paragraph": self.project_paragraph
        }

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.message}'