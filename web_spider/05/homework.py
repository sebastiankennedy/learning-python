# 歌词爬取
import requests
import bs4
import time


def get_song():
    for page in range(1, 6):
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

        headers = {
            'accept': 'application/json, text/javascript',
            'origin': 'https://y.qq.com',
            'referer': 'https://y.qq.com/portal/search.html',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }

        params = {
            'ct': '24',
            'qqmusic_ver': '1298',
            'new_json': '1',
            'remoteplace': 'txt.yqq.song',
            'searchid': '54156788897113206',
            't': '0',
            'aggr': '1',
            'cr': '1',
            'catZhida': '1',
            'lossless': '0',
            'flag_qc': '0',
            'p': page,
            'n': '10',
            'w': '周杰伦',
            'g_tk': '1210542345',
            'loginUin': '2794408425',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0',
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print('请求错误码：' + response.status_code)
            print('请求错误体：' + response.text)
            continue

        json = response.json()
        song_list = json['data']['song']['list']

        for song in song_list:
            print('查询歌曲：' + song['name'] + '++++++++++++++++++++++++')
            lyric = get_song_lyric(song['id'])
            print(lyric)
            print('查询歌曲：' + song['name'] + '++++++++++++++++++++++++')
        time.sleep(1)


def get_song_lyric(music_id):
    url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
    headers = {
        'accept': 'application/json, text/javascript',
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/n/yqq/song/001PLl3C4gPSCI.html',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    params = {
        'nobase64': '1',
        'musicid': music_id,
        '-': 'jsonp1',
        'g_tk': '1210542345',
        'loginUin': '2794408425',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
    }
    res = requests.get(url, headers=headers, params=params)
    if res.status_code != 200:
        print('请求错误码：' + res.status_code)
        print('请求错误体：' + res.text)

    html = res.json()['lyric']
    soup = bs4.BeautifulSoup(html, 'html.parser')
    lyric = soup.string
    return lyric


def get_song_detail(media_id):
    url = 'https://y.qq.com/n/yqq/song/' + media_id + '.html'
    headers = {
        'accept': 'application/json, text/javascript',
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/portal/search.html',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print('请求错误码：' + res.status_code)
        print('请求错误体：' + res.text)

    html = res.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup


get_song()
