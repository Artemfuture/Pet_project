import csv
from django.http import HttpResponse


def export_to_csv(queryset, fields, filename):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    response.write('\ufeff')
    writer = csv.writer(response, delimiter=';')

    writer.writerow(fields)

    for obj in queryset:
        row = []
        for field in fields:
            value = getattr(obj, field)

            if hasattr(value, '__str__'):
                value = str(value)

            row.append(value)

        writer.writerow(row)

    return response