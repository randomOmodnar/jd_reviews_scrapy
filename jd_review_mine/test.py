import requests

headers = {
    # 'authority': 'club.jd.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    # 'accept': '*/*',
    # 'sec-fetch-site': 'same-site',
    # 'sec-fetch-mode': 'no-cors',
    # 'sec-fetch-dest': 'script',
    # 'referer': 'https://item.jd.com/69125734031.html',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'areaId=18; PCSYCityID=CN_430000_430100_0; shshshfpa=cdceecc4-b80d-6a12-641d-db196f1b9032-1595497530; shshshfpb=ujuDrzaLBxWErDfyibHoADg%3D%3D; ipLoc-djd=18-1482-48942-49058; jwotest_product=99; user-key=35b9b8bc-15a8-49bd-bac8-02debb3a4d1e; pinId=Q6nDONe3u4l0dfjyNquB5LV9-x-f3wj7; pin=jd_7c3170395462a; unick=jd_136712dgw; _tp=irawMSzJ8Y1fRBpl17zCwdARx0EngenTEy7YoM%2FXWRU%3D; _pst=jd_7c3170395462a; cn=81; TrackID=1KvVhN2e4FKmaWKqm87ppoVYWNxJvMdbuaYuxHl-iPe7D1JMiX3Q8AtmV2fzKezMIpeazMzgUhHHUGTFZi4YBn-yP7VykTyq-9w2PgY5FKKgHL5GkR7g9Ig80aQh0RmOf; ceshi3.com=103; unpl=V2_ZzNtbUoFFEUiXUEDexsPB2JQFQ0RVhBBJV1CVn0eVQMzA0cNclRCFnQUR1JnGloUZwUZX0ZcQBFFCEdkeB5fA2AFEFlBZxVLK14bADlNDEY1WnwHBAJfF3ILQFJ8HlQMZAEUbXJUQyV1CXZUcxhfBWMDE19CZ3MSRTh2V30dXQBuMxNtQ2cBQSkKQVF%2bHFVIZwsTXkJTQxR3CHZVSxo%3d; __jdv=122270672|baidu|-|organic|not set|1595864645614; __jdc=122270672; 3AB9D23F7A4B3C9B=KGQPOR64XJN54XQQEQPQQHFP43E7GPQXOP7LWOCFAC6N3GEKDLN6TZB7Q74DQTHO33D7SRTHV3G2ZQQAZW3UCPKBDI; wlfstk_smdl=97pmk7m33vgvj9g3qg17jp0fpke2jxkt; __jdu=1902151031; shshshfp=82aa88db0946ac7ff0c226d19ba7623b; __jda=122270672.1902151031.1595497527.1595943167.1595946222.17; JSESSIONID=2A80322E67C6A1663AE62B2C069A541F.s1; shshshsID=d436ac5b08bb534ac7f3e6a714c349d3_5_1595946663596; __jdb=122270672.5.1902151031|17.1595946222',
}

params = (
    ('callback', 'fetchJSON_comment98'),
    ('productId', '69125734031'),
    ('score', '0'),
    ('sortType', '5'),
    ('page', '0'),
    ('pageSize', '10'),
    ('isShadowSku', '0'),
    ('fold', '1'),
)


response = requests.get('https://club.jd.com/comment/productPageComments.action', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=69125734031&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1', headers=headers)
# print(response.text)

if '到快递就评' in response.text:
    print('sucess')