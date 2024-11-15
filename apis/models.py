from django.db import models

class Actor(models.Model):
    name = models.CharField( max_length=250)
    GENDER = (
        ("MALE", "male"),
        ("FEMALE", "female"),
    )
    gender = models.CharField(choices=GENDER, max_length=50)
    def __str__(self):
        return self.name
    
class Director(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField( max_length=150)
    year = models.IntegerField()
    time = models.CharField( max_length=50)
    lang = models.CharField( max_length=50)
    rel_date = models.DateField(auto_now=False)
    country = models.CharField( max_length=150)
    def __str__(self):
        return self.title

class Genres(models.Model):
    title = models.CharField( max_length=50)
    def __str__(self):
        return self.title

class Reviewer(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name

class MovieDirector(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
class MovieCast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField( max_length=50)
    def __str__(self):
        return self.role

class MovieGenres(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)   
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    STARS = (
        ("1",1),
        ("2",2),
        ("3",3),
        ("4",4),
        ("5",5),
    )
    stars = models.CharField(choices=STARS, max_length=50)
    num_o_ratings = models.IntegerField()

    def __str__(self):
        return self.stars

    