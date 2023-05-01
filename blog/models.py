from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='blog/images/',
                              default='blog/images/default.png')
    category = models.ForeignKey(Category, verbose_name="Category",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100]

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
