from datetime import datetime
from xml.dom import minidom
import requests
import time

if __name__ == '__main__':
    doc = minidom.parse("conf.xml")

    settings = doc.getElementsByTagName('setting')
    setting_url = doc.getElementsByTagName('setting')[0]

    download_url = settings[0].firstChild.data.strip()
    destination_path = settings[1].firstChild.data.strip()

    print('Beginning file download with requests')
    downloaded_url = requests.get(download_url)

    file_name = time.strftime("%Y%m%d-%H%M%S")
    with open(f'%s\%s.xls' % (destination_path, file_name), 'wb') as f:
        f.write(downloaded_url.content)

    # Retrieve HTTP meta-data
    print(downloaded_url.status_code)
    print(downloaded_url.headers['content-type'])
    print(downloaded_url.encoding)



