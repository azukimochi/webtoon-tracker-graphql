from . models import Author, DayOfRelease

def get_valid_authors(authors):
    valid_authors = []
    for username in authors:
        print('Karen the username is: ', username)
        if Author.objects.filter(username=username).exists():
            existing_author = Author.objects.filter(username=username)[0]  
            valid_authors.append(existing_author)
        else:
            new_author = Author(username=username)
            new_author.save()
            valid_authors.append(new_author)
    print('Karen valid authors: ', valid_authors)
    return valid_authors

def get_valid_days_of_release(days_of_release):
    valid_days_of_release = []
    for day in days_of_release:
        print('Karen the day is: ', day)
        day = DayOfRelease.objects.get(day_of_week=day)
        print('Karen day from query_set: ', day)
        valid_days_of_release.append(day)
    print('Karen valid days of release: ', valid_days_of_release)
    return valid_days_of_release