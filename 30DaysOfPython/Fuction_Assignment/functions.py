def make_shirt(size,text):
    print(f'The size of the shirt is {size} and the message to be printed is "{text}"')


def describe_city(city,country='Nigeria'):
    print(f'{city} is in {country}')


def city_country(city,country):
    print(f'{city}, {country}')


def make_album(artist_name,album_title,n_songs=None):
    album={'Artist name':artist_name,'Album title':album_title}
    if n_songs:
        album['Number of songs']=n_songs
    return album


def show_messages(m_list):
    for m in m_list:
        print(m)