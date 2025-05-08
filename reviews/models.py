from django.db import models
from movies.models import Movies
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movies, on_delete = models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators = [MinValueValidator(0,'Avaliacao nao pode ser inferior a 0 estrelas'),
                                              MaxValueValidator(5, 'Avaliacao nao pode ser superior a 5 estrelas.')])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie.title