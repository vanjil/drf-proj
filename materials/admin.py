from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Kurs, Urok, Payment


# Регистрация моделей в админке
@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Urok)
class UrokAdmin(admin.ModelAdmin):
    list_display = ('name', 'kurs', 'video_link')
    search_fields = ('name', 'kurs__name')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid_course', 'paid_lesson', 'amount', 'payment_date', 'payment_method')
    search_fields = ('user__username', 'paid_course__name', 'paid_lesson__name')


# Создаем группу модераторов и задаем ей права
def create_moderator_group():
    moderator_group, created = Group.objects.get_or_create(name='Moderators')

    if created:
        # Получаем ContentType для моделей Kurs и Urok
        kurs_content_type = ContentType.objects.get_for_model(Kurs)
        urok_content_type = ContentType.objects.get_for_model(Urok)

        # Добавляем права на изменение и просмотр курсов и уроков
        permissions = Permission.objects.filter(
            content_type__in=[kurs_content_type, urok_content_type],
            codename__in=['change_kurs', 'view_kurs', 'change_urok', 'view_urok']
        )
        moderator_group.permissions.set(permissions)
        moderator_group.save()


# Создаем группу модераторов при старте сервера (или при миграциях)
create_moderator_group()
