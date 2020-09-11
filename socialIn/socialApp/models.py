from django.db import models


class UserN(models.Model):
    data_de_nascimento = models.DateField()
    username = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__ (self):
        return self.username

class Profile(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(UserN, on_delete=models.CASCADE, related_name = 'profiles')
    contats = models.ManyToManyField('self', blank=True, null=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    text = models.TextField()
    date = models.DateField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'posts')
    def __str__(self):
        return self.text

class Comment(models.Model):
    text = models.TextField()
    date = models.DateField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'comments')
    post  = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    def __str__(self):
        return ""+self.post.text+": "+self.text

class React(models.Model):
    REACTS_TYPES = (
        ('c','Curti'),
        ('a','Amei'),
        ('r','Rindo',),
        ('i','Impressionado'),
        ('e','Entristecido'),
        ('p','Irritado'),
    )
    
    type = models.CharField(max_length=1,choices=REACTS_TYPES)
    date = models.DateField()
    post =  models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'reacts')
    profile  =  models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'reacts')
    peso = models.IntegerField()
    def __str__(self):
        return ""+str(self.peso)+" "+self.type+": "+self.post.text+"by. "+self.profile.name 