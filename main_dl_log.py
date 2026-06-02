import requests
from bs4 import BeautifulSoup
from glob import glob


def main():
    all_log = glob('*.log')
    print(all_log)

    for log_file in all_log:
        with open(log_file) as f:
            lines = f.readlines()
            print(len(lines))


def main_dl():
    url = "https://logs.eolem.com/"
    r = requests.get(url,verify=False)
    
    print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')

    url_log = [url+a['href'] for a in soup.find_all('a') if '.log' in a['href']]
    # all_a = soup.find_all('a')
    # for a in all_a:
    #     if '.log' in a['href']:
    #         url_log.append(url+a['href'])

    for url in url_log:
        r = requests.get(url,verify=False)
        url_log_file = url.split('/')[-1]
        print(url_log_file)
        with open(url_log_file,'w') as f:
            f.write(r.text)
        

if __name__=='__main__':
    main()



