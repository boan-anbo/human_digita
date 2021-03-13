from django.contrib import admin

# Register your models here.
from django_object_actions import DjangoObjectActions

from human_digita.person.admin_forms import PersonForm
from human_digita.person.models import Person
from util_functions.pinyin import name_to_pinyin


@admin.register(Person)
class PersonAdmin(DjangoObjectActions, admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'first_name_cn', 'last_name_cn']
    list_display = ['id', '__str__', 'note']
    readonly_fields = ['id']
    form = PersonForm
    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('annotations')
        return qs

    def fill_pinyin(self, request, obj: Person):
        lastname_cn = obj.last_name_cn
        firstname_cn = obj.first_name_cn
        if lastname_cn:
            obj.last_name = name_to_pinyin(lastname_cn)
        if firstname_cn:
            obj.first_name = name_to_pinyin(firstname_cn)
        if lastname_cn or firstname_cn:
            obj.save()
    fill_pinyin.label = "Fill in Pinyin"  # optional
    fill_pinyin.short_description = "Fill English Names with Pinyin."  # optional

    change_actions = ('fill_pinyin',)
