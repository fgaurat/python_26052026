import requests
from bs4 import BeautifulSoup


def main():
    url = "https://logs.eolem.com/"
    r = requests.get(url,verify=False)
    
    print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')

    url_log = [url+a['href'] for a in soup.find_all('a') if '.log' in a['href']]
    # all_a = soup.find_all('a')
    # for a in all_a:
    #     if '.log' in a['href']:
    #         url_log.append(url+a['href'])

    print(url_log)
    for url in url_log:
        r = requests.get(url,verify=False)


if __name__=='__main__':
    main()




d = {"x":1}
print(d) # {"x":1}
print(d['x']) # 1
d['x'] +=4 # d['x'] = d['x'] + 4 # 1+4 => 5

print(d) # {"x":5}
print(d['x']) # 5


a = "toto" 
b = int(a) # 3