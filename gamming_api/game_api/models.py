from django.db import models


# Create your models here.


# create games product

class Games(models.Model):
    game_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    game_type = models.CharField(max_length=255, null=True, blank=True)
    game_code = models.CharField(max_length=255, null=True, blank=True)
    gamephoto = models.ImageField(upload_to='game_image', null=True, blank=True)
    membership_price = models.CharField(max_length=200, null=True, blank=True)
    why_stem_education = models.TextField(null=True, blank=True)
    mode = models.CharField(max_length=255, null=True, blank=True)
    age_group = models.CharField(max_length=50, null=True, blank=True)
    emi = models.CharField(max_length=255, null=True, blank=True)
    key_skills = models.TextField(null=True, blank=True)
    key_concept = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    game_type = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    membership = models.CharField(max_length=255, null=True, blank=True)
    shipping = models.CharField(max_length=255, null=True, blank=True)
    program = models.TextField(null=True, blank=True)
    discount = models.CharField(max_length=50, null=True, blank=True)
    components = models.TextField(null=True, blank=True)
    learning_projects = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_video = models.CharField(max_length=255, null=True, blank=True)
    total_level_kits = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

    def __str__(self):
        return self.game_name

# create game levels

class Level(models.Model):
    level_number = models.IntegerField( null=True, blank=True)
    level_code = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    level_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    hardware_components = models.TextField(null=True, blank=True)
    learning_concepts = models.TextField(null=True, blank=True)
    programming_skill = models.TextField(null=True, blank=True)
    key_skills = models.TextField(null=True, blank=True)
    discount = models.CharField(max_length=50, null=True, blank=True)
    game = models.ForeignKey(Games,related_name='levels', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.level_number},{self.level_code},{self.level_name},{self.price}'

# create challenge in levels

class Tasks(models.Model):
    task_code = models.CharField(max_length=255, null=True, blank=True)
    task_number = models.CharField(max_length=255, null=True, blank=True)
    task_name = models.CharField(max_length=255, null=True, blank=True)
    hardware_components = models.TextField(null=True, blank=True)
    video_link = models.CharField(max_length=255, null=True, blank=True)
    engineering = models.TextField(null=True, blank=True)
    technology = models.TextField(null=True, blank=True)
    science  = models.TextField(null=True, blank=True)
    maths = models.TextField(null=True, blank=True)
    programming_skill = models.TextField(null=True, blank=True)
    learning_concepts = models.TextField(null=True, blank=True)
    key_skills = models.TextField(null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f'{self.task_code},{self.task_name}'
# create student model !


class Student(models.Model):
    
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
     )
    name = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=12, blank=True, unique=True)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES)
    email = models.EmailField(null=True,blank=True)
    class_semester = models.CharField(max_length = 50,null = True, blank = True)
    parent_contact = models.CharField(max_length=12, null=True, blank=True)
    school_name = models.TextField(max_length=255, null = True, blank = True)
    is_captain = models.BooleanField(default=False) 
    is_ilp_member=models.BooleanField(default=False,null = True, blank = True) 
    game = models.ManyToManyField(Games, null = True, blank = True)
    level = models.ManyToManyField(Level, null = True, blank = True)
    task = models.ManyToManyField(Tasks, null = True, blank = True)
    join_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.name},{self.contact},{self.email},{self.parent_contact},{self.is_captain},{self.gender},{self.school_name},{self.class_semester}'  