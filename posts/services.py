from django.db.models import Count, Avg, Min, Max
from .models import AccessLog


class QueryService:

    @staticmethod
    def visits_by_driver():
        """Сводка по каждому водителю"""
        return AccessLog.objects.filter(
        event_type='OUT'  
        ).values(
            'car__driver__id_driver',
            'car__driver__surname',
            'car__driver__first_name'
        ).annotate(
            count_visits=Count('id_log'),
            avg_duration=Avg('duration_minutes'),
            min_duration=Min('duration_minutes'),
            max_duration=Max('duration_minutes')
        ).order_by('car__driver__surname')
    
        

    @staticmethod
    def visits_by_car():
        """Сводка по каждой машине"""
        return AccessLog.objects.filter(
        event_type='OUT').values(
            'car__id_car',
            'car__number_auto',
            'car__driver__surname',
            'car__driver__first_name'
        ).annotate(
            count_visits=Count('id_log'),
            avg_duration=Avg('duration_minutes'),
            min_duration=Min('duration_minutes'),
            max_duration=Max('duration_minutes')
        ).order_by('car__number_auto')

    @staticmethod
    def visits_by_garage():
        """Сводка по каждому гаражу"""
        return AccessLog.objects.filter(
        event_type='OUT'  
        ).values(
            'place__garage__id_garage',
            'place__garage__name',
        ).annotate(
            count_visits=Count('id_log'),
            avg_duration=Avg('duration_minutes'),
            min_duration=Min('duration_minutes'),
            max_duration=Max('duration_minutes')
        ).order_by('place__garage__name')

    @staticmethod
    def visits_flat():
        """Плоская таблица всех посещений"""
        return AccessLog.objects.select_related(
            'car', 'car__driver', 'place', 'place__garage', 'card'
        ).all().order_by('-event_time')

    @staticmethod
    def visits_by_year():
        """Сводка по году"""
        from django.db.models.functions import ExtractYear
        return AccessLog.objects.annotate(year=ExtractYear('event_time')).values(
            'year'
        ).annotate(
            count_visits=Count('id_log'),
            avg_duration=Avg('duration_minutes'),
            min_duration=Min('duration_minutes'),
            max_duration=Max('duration_minutes')
        ).order_by('year')