from django.db import models

class Work(models.Model):
    # - start date
    # - end date
    # - job_title
    # - duty
    # - company/institute
    # - location
    company = models.CharField(max_length=50, primary_key=True, default="company_or_institute")
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=True, blank=True)
    job_title = models.CharField(max_length=50)
    duty = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=False, null=True)



class Education(models.Model):
    # - obtainment
    # - event
    # - date and year
    title = models.CharField(max_length=100, primary_key=True, default="education_title")
    acquirement = models.CharField(max_length=200)
    event = models.CharField(max_length=500)
    date_and_year = models.DateTimeField(null=False)

class Career(models.Model):
    # - start date
    # - inductral
    # - role of people
    # - value
    # - aim of earning
    title = models.CharField(max_length=100, primary_key=True, default="career_title")
    start_date = models.DateTimeField(null=False)
    industrial = models.CharField(max_length=30)
    role_of_participants = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    aim_of_earning = models.FloatField()


class Memory(models.Model):
    # - place
    # - people
    # - age
    # - year and date
    # - event
    # - mindflow
    title = models.CharField(max_length=100, primary_key=True, default="memory_title")
    date_and_year = models.DateTimeField(null=False)
    age = models.FloatField()
    event = models.CharField(max_length=500)
    mindflow = models.CharField(max_length=500)
    people = models.CharField(max_length=200)



class Now(models.Model):
    # now:
    # - aim
    # - reason
    # - start date
    title = models.CharField(max_length=100, primary_key=True, default="now_title")
    aim = models.CharField(max_length=500, null=True)
    reason = models.CharField(max_length=700, null=True)
    start_date = models.DateTimeField()


class Image_Shooting(models.Model):
    # - image file
    # - place
    # - year and date
    # - mindflow
    # - title
    # - age
    image_file = models.ImageField(upload_to="", null=False)
    title = models.CharField(max_length=100, primary_key=True, default="image_shooting_title")
    place = models.CharField(max_length=200, null=True)
    age = models.FloatField(blank=True)
    created_date_time = models.DateTimeField(null=False)
    edited_finished_date_time = models.DateTimeField(null=True, blank=True)
    mindflow = models.CharField(max_length=1000, null=True)


class Image_Me(models.Model):
    # - image file
    # - place
    # - age
    # - date and year
    # - what I am thinking
    image_file = models.ImageField(upload_to="", null=False)
    title = models.CharField(max_length=100, primary_key=True, default="image_me_title")
    place = models.CharField(max_length=200, null=True)
    age = models.FloatField()
    created_date_time = models.DateTimeField(null=False)
    edited_finished_date_time = models.DateTimeField(null=True, blank=True)
    what_I_am_thinking = models.CharField(max_length=1000, null=True)


class MTV(models.Model):
    # - mp4 file
    # - "music"
    # - camera operator
    # - editor
    # - director
    # - lighting operator
    video_file = models.FileField(upload_to="")
    cover_file = models.ImageField(upload_to="", null=False)
    finished_date_time = models.DateTimeField(null=True)
    title = models.CharField(max_length=100, primary_key=True, default="mtv_title")
    camera_oprator = models.CharField(max_length=100, default="Zhixun Teng")
    editor = models.CharField(max_length=100, default="Zhixun Teng")
    director = models.CharField(max_length=100, default="Zhixun Teng")
    lighting_operator = models.CharField(max_length=100, default="Zhixun Teng")


class Music(models.Model):
    # music:
    # - audio file
    # - title
    # - duration
    # - finished date and time
    # - composer
    # - bass player
    # - guitar player
    # - keyboarder
    # - recorder
    # - mixer
    # - producer
    audio_file = models.FileField(upload_to="")
    cover_file = models.ImageField(upload_to="", null=True)
    title = models.CharField(max_length=100, primary_key=True, default="music_title")
    duration = models.CharField(max_length=100, default="5:00")
    finished_date_time = models.DateTimeField(null=True)
    composer = models.CharField(max_length=100, default="Zhixun Teng")
    bass_player = models.CharField(max_length=100, default="Zhixun Teng")
    guitar_player = models.CharField(max_length=100, default="Zhixun Teng")
    keyboarder = models.CharField(max_length=100, default="Zhixun Teng")
    recorder = models.CharField(max_length=100, default="Zhixun Teng")
    mixer = models.CharField(max_length=100, default="Zhixun Teng")
    producer = models.CharField(max_length=100, default="Zhixun Teng")

