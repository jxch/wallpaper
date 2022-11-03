import requests
import parsel
import random

url_base = 'http://m.bcoderss.com/tag/{}/page/{}/'
headers = {
    'Cookie': 'UM_distinctid=1747c5616688f-0da459aa281e74-3962420d-1fa400-1747c56166982d; CNZZDATA1278590218=744878758-1599811024-%7C1599811024',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}


def get_random_img_url(tag, page):
    url = url_base.format(tag, page)
    img_arr_page_res = requests.get(url=url, headers=headers)
    img_arr_page_selector = parsel.Selector(img_arr_page_res.text)
    img_urls = img_arr_page_selector.css('#main a::attr(href)').getall()

    img_page_url = img_urls[random.randint(0, len(img_urls))]
    img_page_res = requests.get(url=img_page_url, headers=headers)

    img_selector = parsel.Selector(img_page_res.text)
    img = img_selector.xpath('/html/body/div[4]/img').getall()[0]

    return img.split('src="')[1].split('"')[0]


