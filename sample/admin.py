from django.contrib import admin
from .models import Sample

class SampleAdmin(admin.ModelAdmin):
    # Listeleme sayfasında gösterilecek alanlar. 'title' ve 'image' alanları kullanılabilir.
    list_display = ['title', 'image']

    # Listeleme sayfasında filtreleme için kullanılacak alanlar. 'title' alanı kullanılabilir.
    list_filter = ['title']

    # Listeleme sayfasında tıklanabilir bağlantılar. Burada sadece 'title' alanı tıklanabilir.
    list_display_links = ['title']

# Sample modelini admin arayüzüne kaydederken SampleAdmin sınıfını kullan
admin.site.register(Sample, SampleAdmin)
