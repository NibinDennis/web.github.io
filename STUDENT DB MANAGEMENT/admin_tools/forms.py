from django.forms import ModelForm

from .models import Department, Semester, AcademicSession


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class SemesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'


class AcademicSessionForm(ModelForm):
    class Meta:
        model = AcademicSession
        fields = '__all__'
