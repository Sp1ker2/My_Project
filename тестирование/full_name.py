# Test
def full_name(first, last, middle=''):
    if middle:
        full = first + ' ' + last + ' ' + middle
    else:
        full = first + ' ' + last
    return full.title()


"""вот тут создали функцию которая пишет имя и функцию и выводить её на экран"""
