from rest_framework.serializers import ValidationError

allowed_sites = ['youtube.com']


def validate_site(value):
    for item in allowed_sites:
        if item not in value:
            raise ValidationError(f'Ссылка не корректна. Используйте материалы с {item}.')
