from pytest import fixture

from app import app

from views.product import get_default_products


@fixture
def client():
    with app.test_client() as client:
        # мы делаем йилд и он у нас берется из этой функции, те вытаскивается генератором,
        # отдается сним что-то делается, а потом фикстура закрывается и выходит из этого кентеста with.
        yield client
        # return client  # на ретерн автоматически закрывается контекст


def test_get_default_products():
    res = get_default_products()
    assert isinstance(res, dict)
    assert all(map(lambda x: isinstance(x, int), res.keys()))  # проверим что все ключи у нас являются int


# тест на апи
def test_recover_products(client):
    resp = client.post("/products/recover/")
    data = resp.json
    assert data == {"ok": True}
