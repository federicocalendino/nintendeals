from bot.commons.keys import title_, title_jp_


def format_float(value, total_digits=0):
    value = '%.2f' % value

    if total_digits == 0:
        return value
    else:
        return '0' * (total_digits - len(value)) + value


def merge(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            merge(value, node)
        else:
            destination[key] = value

    return destination


def get_title(game):
    if title_ in game:
        return game[title_]
    else:
        return game[title_jp_]
