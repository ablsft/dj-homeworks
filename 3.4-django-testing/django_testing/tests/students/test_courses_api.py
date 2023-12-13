import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_course_retrieve(client, courses_factory):
    course = courses_factory()
    
    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course.name

@pytest.mark.django_db
def test_courses_list(client, courses_factory):
    courses = courses_factory(_quantity=50)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)

    for i, d in enumerate(data):
        assert d['name'] == courses[i].name

@pytest.mark.django_db
def test_courses_filter_id(client, courses_factory):
    courses = courses_factory(_quantity=10)

    response = client.get('/api/v1/courses/', data={'id': courses[2].pk})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[2].name

@pytest.mark.django_db
def test_courses_filter_name(client, courses_factory):
    courses = courses_factory(_quantity=10)

    response = client.get('/api/v1/courses/', data={'name': courses[2].name})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[2].name

@pytest.mark.django_db
def test_course_create(client):
    name = 'testcourse'

    response_post = client.post('/api/v1/courses/', data={'name': name})
    response_get = client.get('/api/v1/courses/')

    assert response_post.status_code == 201
    assert response_get.status_code == 200
    data = response_get.json()
    assert data[0]['name'] == name

@pytest.mark.django_db
def test_course_update(client, courses_factory):
    course = courses_factory()
    name = 'updated name'

    response_patch = client.patch(f'/api/v1/courses/{course.pk}/', 
                                  data={'name': name})
    response_get = client.get('/api/v1/courses/')

    assert response_patch.status_code == 200
    assert response_get.status_code == 200
    data = response_get.json()
    assert data[0]['name'] == name

@pytest.mark.django_db
def test_course_delete(client, courses_factory):
    course = courses_factory()

    response_delete = client.delete(f'/api/v1/courses/{course.pk}/')
    response_get = client.get(f'/api/v1/courses/{course.pk}/')

    assert response_delete.status_code == 204
    assert response_get.status_code == 404

@pytest.mark.django_db
@pytest.mark.parametrize('students_quantity', [20, 21])
def test_students_add(client, students_factory,
                      students_quantity, courses_factory):
    course = courses_factory()
    students = students_factory(_quantity=students_quantity)

    response_post = client.post(f'/api/v1/courses/', data={'name': 'test', 
                            'students': [student.id for student in students]})
    
    response_patch = client.patch(f'/api/v1/courses/{course.pk}/', data={
                            'students': [student.id for student in students]})

    assert response_post.status_code == 201
    assert response_patch.status_code == 200

@pytest.mark.parametrize('students_quantity', [20, 21])
def test_students_add_no_factory(students_quantity, settings):
    max_number = settings.MAX_STUDENTS_PER_COURSE

    assert students_quantity <= max_number
