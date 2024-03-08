from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(data_set, size):
    chunk = []
    for data in data_set:
        chunk.append(data)
        if len(chunk) == size:
            yield chunk
            chunk = []
    yield chunk