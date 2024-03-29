from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet
# Register your models here.


admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']









class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'


    def lookups(self, request, model_admin):
        return [('<40', 'Низкий'), ('от 40 до 59', 'Средний'), ('от 60 до 79', 'Высокий'), ('>=80', 'Высочайший')]


    def queryset(self, request, queryset: QuerySet):
        if self.value()=='<40':
            return queryset.filter(rating__lt=40)
        if self.value()=='от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value()=='от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value()=='>=80':
            return queryset.filter(rating__gte=80)

        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields = ['rating', 'name'] # какие именно показывать
    #exclude = ['slug']  #исключать поля
    #readonly_fields = ['year'] #запретить изменять
    prepopulated_fields = {'slug': ('name', )} #Есть вычисляемое поле, оно будет вычисляться на основе кортежа, в кортеже передаем поля, чтобы поле вычислилось
    list_display = ['name', 'rating', 'director', 'budget']
    list_editable = ['rating', 'director', 'budget']
    filter_horizontal = ['actors']
    ordering = ['-rating', '-name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__istartswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]


    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено - {count_updated} записей',
            messages.ERROR
        )
