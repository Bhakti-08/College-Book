from django.contrib import admin
from . import models

# Register your models here.
class TestSubjectAdmin(admin.ModelAdmin):
    list_display = ['id','test_name']
admin.site.register(models.TestSubject,TestSubjectAdmin)

class TestQuestionsAdmin(admin.ModelAdmin):
    list_display = ['question','subject']
admin.site.register(models.TestQuestions,TestQuestionsAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch']
admin.site.register(models.Branch,BranchAdmin)

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['branch','subjectID','subjectName']
admin.site.register(models.Subjects,SubjectsAdmin)

class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['subjectID','questionBank']
admin.site.register(models.QuestionBank,QuestionBankAdmin)

class TestsAdmin(admin.ModelAdmin):
    list_display = ['branch','subject','testName']
admin.site.register(models.Tests,TestsAdmin)

class ProfessorsAdmin(admin.ModelAdmin):
    list_display = ['firstName','lastName','email','branch','subjectID']
admin.site.register(models.Professors,ProfessorsAdmin)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['registrationNum','firstName','lastName']
admin.site.register(models.Students,StudentsAdmin)
