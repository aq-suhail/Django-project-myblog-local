try:
    import markdown as md
except Exception:
    md = None

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='markdown')
@stringfilter
def markdown(value):
    if md:
        return md.markdown(value, extensions=['markdown.extensions.fenced_code'])
    # fallback: return escaped/plain text if markdown not available
    from django.utils.html import escape
    return '<pre>{}</pre>'.format(escape(value))