from django.db import models
from django.core import management

# Create your models here.
class Branch(models.Model):
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.branch

class Subjects(models.Model):
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE)
    subjectID = models.CharField(max_length=20)
    subjectName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subjectName

class QuestionBank(models.Model):
    subjectID = models.CharField(max_length=20, default=None)
    questionBank = models.FileField(upload_to='QuestionBanks/',default=None,null=True)

class Professors(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    #subject = models.ForeignKey(Subjects, on_delete = models.CASCADE)
    subjectID = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName, self.subjectID

class Students(models.Model):
    registrationNum = models.CharField(max_length=20)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.registrationNum
    
class Tests(models.Model):
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE, default=None)
    subject = models.ForeignKey(Subjects, on_delete = models.CASCADE)
    testName = models.CharField(max_length=20)
    numberOfQuestions = models.IntegerField(default=None)
    #testDuration = models.DurationField(default=None)
    testDate = models.DateField(default=None)
    testStartTime = models.TimeField(default=None)
    testEndTime = models.TimeField(default=None)
    testBufferTime = models.TimeField(default=None)    

    def __str__(self):
        return self.testName
    
class Questions(models.Model):
    #subject = models.ForeignKey(Subjects, on_delete = models.CASCADE, default=None, null=True)
    # means if this category is terminated then all questions related to this category will also get deleted
    #subject = models.CharField(max_length=100)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, default=None, null=True)
    question = models.TextField()
    opt_1 = models.CharField(max_length=200)
    opt_2 = models.CharField(max_length=200)
    opt_3 = models.CharField(max_length=200)
    opt_4 = models.CharField(max_length=200)
    right_opt = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question