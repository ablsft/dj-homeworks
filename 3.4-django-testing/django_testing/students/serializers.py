from rest_framework import serializers
from django.conf import settings

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        students_quantity = 0
        students = data.get('students')
        
        if students:
            students_quantity = len(data.get('students'))

        if students_quantity > settings.MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError([
                'Allowed quantity of students exceeded'
            ])
        else:
            return data