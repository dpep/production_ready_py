def test_status(client):
  res = client.get('/')

  assert res.status_code == 200
  assert res.text == 'OK'
