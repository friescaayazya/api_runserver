author = 'Friesca Ayazya'
email = 'friescacantik@gmail.com'
app_title = 'Menggunakan Python Requests Untuk Memanggil Di Django'

# memanggil # API diserver Django

url = http://127.0.0.1:8000/
impor requests

response = response.get(url)
if response.status_code == 200:
    print ('Koneksi Berhasil')
    # panggil API untuk Status: Suhu
    url_api = f'{url} api/v1/stats/'
    responses.status_code == 200
    print(response.txt)

    import json
    data = json.loads(response.txt)
    data_terakhir = data[len(data)-1]
    suhu = data_terakhir['suhu']
    humidity = data_terakhir['humidity']
    print(f'Hasil pembacaan sensor: suhu=(suhu), humidity = {humidity}')
