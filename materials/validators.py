from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_youtube_url(value):
    # для проверки что ссылка ведет на YouTube
    youtube_regex = r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
    if not re.match(youtube_regex, value):
        raise ValidationError(
            _('Ссылка на видео должна вести на YouTube. Другие источники не допускаются.'),
            params={'value': value},
        )
