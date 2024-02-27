import asyncio
import requests
from bs4 import BeautifulSoup

class Loader:
    
    def youtube(url):
        cookies = {
            '_gid': 'GA1.2.1669625502.1698176432',
            '_gat_gtag_UA_147320166_8': '1',
            'XSRF-TOKEN': 'eyJpdiI6ImErVDk0VnhpbXV5NTFpNk5ITDJFQWc9PSIsInZhbHVlIjoiUVViUjJLU2g4aFpJZlU2MFZQeGtUcnMrWXcrWEdYQnVpQVU4SENVdmNoRFI1eU1vcDVEMnJEZFphZWFPdnZhdnBZeXIzb3czcGVqd0FzcVY1NkY1V2RmR0JXbzVVQ3dTRGJnT29OdWZrMytxR2FtZHE0UGd4N1o5LzBSU1hSV1UiLCJtYWMiOiI2NGZjNmViNTczZGNhMDAzN2RlNTEwNWU1YmE1ZGU2ZDFhM2Q5MTllYzM1YmMwYmE5NGI5OTU5NWYxYTE3NDk1IiwidGFnIjoiIn0%3D',
            '10downloader_session': 'eyJpdiI6Ik1LYUIrZDdmMXRybDd5UDhtL2JmU1E9PSIsInZhbHVlIjoibU1qV0lJRkR2QXFlaEp3V3dOSHB3MmdKU0JkbTZjTGg2QkZyTDk2R09ySGVyMG5tbWlpd2J4NnRvaEhiTDFVSlNEcWUxajBCb1NJdnI3WnhMK0JPa291V0JmN1MrUEdzemVOVm1jOHNxWjVhVTZIY0lZTWFSZUtIMFZIYXhwaEoiLCJtYWMiOiJhNzc3ZDhiZTgzZTg3OWVhNmI5N2FkYzkxMTM1Y2U0NTVjYmZiMWFkZTkyNzkxNjg0NmJmM2U2YTc0ZDZmY2FlIiwidGFnIjoiIn0%3D',
            'pp_main_cc84f951a8961fb5d4f0646dd679c0db': '1',
            'dom3ic8zudi28v8lr6fgphwffqoz0j6c': '6a4ab436-dfe5-4d72-ac4c-eaf672d40ac2%3A3%3A1',
            '_ga_F6DZTE36HB': 'GS1.1.1698176430.1.1.1698176458.0.0.0',
            '_ga': 'GA1.2.1519360924.1698176431',
        }

        headers = {
            'authority': '10downloader.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uz;q=0.6',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_gid=GA1.2.1669625502.1698176432; _gat_gtag_UA_147320166_8=1; XSRF-TOKEN=eyJpdiI6ImErVDk0VnhpbXV5NTFpNk5ITDJFQWc9PSIsInZhbHVlIjoiUVViUjJLU2g4aFpJZlU2MFZQeGtUcnMrWXcrWEdYQnVpQVU4SENVdmNoRFI1eU1vcDVEMnJEZFphZWFPdnZhdnBZeXIzb3czcGVqd0FzcVY1NkY1V2RmR0JXbzVVQ3dTRGJnT29OdWZrMytxR2FtZHE0UGd4N1o5LzBSU1hSV1UiLCJtYWMiOiI2NGZjNmViNTczZGNhMDAzN2RlNTEwNWU1YmE1ZGU2ZDFhM2Q5MTllYzM1YmMwYmE5NGI5OTU5NWYxYTE3NDk1IiwidGFnIjoiIn0%3D; 10downloader_session=eyJpdiI6Ik1LYUIrZDdmMXRybDd5UDhtL2JmU1E9PSIsInZhbHVlIjoibU1qV0lJRkR2QXFlaEp3V3dOSHB3MmdKU0JkbTZjTGg2QkZyTDk2R09ySGVyMG5tbWlpd2J4NnRvaEhiTDFVSlNEcWUxajBCb1NJdnI3WnhMK0JPa291V0JmN1MrUEdzemVOVm1jOHNxWjVhVTZIY0lZTWFSZUtIMFZIYXhwaEoiLCJtYWMiOiJhNzc3ZDhiZTgzZTg3OWVhNmI5N2FkYzkxMTM1Y2U0NTVjYmZiMWFkZTkyNzkxNjg0NmJmM2U2YTc0ZDZmY2FlIiwidGFnIjoiIn0%3D; pp_main_cc84f951a8961fb5d4f0646dd679c0db=1; dom3ic8zudi28v8lr6fgphwffqoz0j6c=6a4ab436-dfe5-4d72-ac4c-eaf672d40ac2%3A3%3A1; _ga_F6DZTE36HB=GS1.1.1698176430.1.1.1698176458.0.0.0; _ga=GA1.2.1519360924.1698176431',
            'referer': 'https://10downloader.com/en/111',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        }

        params = {
            'v': url,
            'lang': 'en',
            'type': 'video',
        }

        response = requests.get('https://10downloader.com/download', params=params, cookies=cookies, headers=headers)

        soup = BeautifulSoup(response.content, 'lxml')

        
        metas = soup.find('div', {'class':'info col-md-4'})
        if not metas:
            return {
                'status':False,
                'message':"⭕️ Siz bergan url manzili bo'yicha hechnarsa topilmadi"
            }
        
        data = {
            'status':True,
            'urls':[],
            'title':metas.find('span').text,
            'img': metas.find('img')['src']
        }

        data_table = soup.find('tbody').find_all('tr')
        for i in data_table:
            tds = i.find_all('td')
            url = i.find('a')['href']

            data['urls'].append({
                'quality':tds[0].text,
                'url':url,
                "ftype":tds[1].text
            })

        return data


