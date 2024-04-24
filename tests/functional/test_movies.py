def test_get_movie(test_client):
    response = test_client.get('/movies/')
    assert response.status_code == 200
    all_movies = response.json
    assert len(all_movies) > 0
    selected_movie = all_movies[0]

    response = test_client.get('/movies/' + str(selected_movie['id']))
    assert response.status_code == 200
    movie = response.json
    assert movie is not None
    assert movie['id'] == selected_movie['id']

def test_get_movie_set(test_client, new_movies_in_db):
    response = test_client.get('/movies/?filters=TestingMovie')
    assert response.status_code == 200
    movies = response.json
    assert len(movies) == 4
    assert new_movies_in_db[0].id == movies[0]['id']

    response = test_client.get('/movies/?filters=TestingMovie&page=2&quantity=2')
    assert response.status_code == 200
    movies = response.json
    assert len(movies) == 2
    assert new_movies_in_db[2].id == movies[0]['id']
    assert new_movies_in_db[3].id == movies[1]['id']

def test_get_movie_from_imdb_using_title(test_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }
    data = {
        'title': 'The Lord of the Rings: The Fellowship of the Ring'
        # 'imdb_id': 'tt0120737'
    }
    response = test_client.post('/movies/', json=data, headers=headers)
    assert response.status_code == 200
    assert response.content_type == mimetype
    assert response.json['imdb_id'] == 'tt0120737'

def test_get_movie_from_imdb_using_id(test_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }
    data = {
        # 'title': 'Star Wars: Episode I - The Phantom Menace'
        'imdb_id': 'tt0120915'
    }
    response = test_client.post('/movies/', json=data, headers=headers)
    assert response.status_code == 200
    assert response.content_type == mimetype
    assert response.json['title'] == 'Star Wars: Episode I - The Phantom Menace'

def test_get_movie_from_imdb_ensure_failure(test_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }
    data = {
        'imdb_id': 'there is no such imdb id'
    }
    response = test_client.post('/movies/', json=data, headers=headers)
    print(response, response.status_code)
    assert response.status_code == 404
    assert response.content_type == mimetype
