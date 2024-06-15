from datetime import date
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama":  "programlama kategorisine ait kurs listesi",
    "web-gelistirme": "web geliştirme kategorisine ait kurs listesi",
    "mobil": "mobil geliştirme kategorisine ait kurs listesi",
    "programlama1":  "programlama kategorisine ait kurs listesi",
    "web-gelistirme1": "web geliştirme kategorisine ait kurs listesi",
    "mobil1": "mobil geliştirme kategorisine ait kurs listesi",
}


db = {

    "courses": [
        {
            "title": "javascript kursu",
            "description": "java script kurs açıklaması",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug": "javascript-kursu",
            "date": date(2024, 1, 1),
            "isActive": True

        },
        {
            "title": "python kursu",
            "description": "python kurs açıklaması",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
            "slug": "python-kursu",
            "date": date(2024, 2, 2),
            "isActive": False

        },
        {
            "title": "web geliştirme kursu",
            "description": "web geliştirme kurs açıklaması",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2024, 3, 3),
            "isActive": True

        },
        {
            "title": "SQL kursu",
            "description": "SQL kurs açıklaması",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/2907528_f51f_2.jpg",
            "slug": "SQL-kursu",
            "date": date(2024, 4, 4),
            "isActive": True

        },
        {
            "title": "django kursu",
            "description": "django kurs açıklaması",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/4301499_60fc.jpg",
            "slug": "django-kursu",
            "date": date(2024, 5, 5),
            "isActive": True

        },],

    "categories": [
        {"id": 1, "name": "programlama", "slug": "programlama"},
        {"id": 2, "name": "web geliştirme", "slug": "web-gelistirme"},
        {"id": 3, "name": "mobil uygulamalar", "slug": "mobil-uygulamalar"},
        {"id": 4, "name": "yapay zeka", "slug": "yapay-zeka"},
        {"id": 5, "name": "modelleme", "slug": "modelleme"},
        {"id": 5, "name": "diy", "slug": "diy"}],

}


def index(request):

    kurslar = db["courses"]
    kategoriler = db["categories"]

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })


def details(request, kurs_adi):
    return render(request, 'courses/kurslar.html')


def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]

        return render(request, 'courses/kurslar.html', {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound('<h1>Uzantı bulunamadı, kontrol ediniz</h1>')


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())

    if (category_id > len(category_list)):
        return HttpResponseNotFound("Verilen id'ye uyan kurs kategorisi bulunamadı")

    category_name = category_list[category_id-1]

    redirect_url = reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)
