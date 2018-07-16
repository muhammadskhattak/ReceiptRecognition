import requests


def extract_from_file(html_text: str, key: str, delimit: str, start_idx: str
                      ) -> list:
    """ Extracts all relevant information delimited by key and delimit after
    start_idx in the html text file.

    * WARNING: Really specific usage has made it work only under certain
    conditions.
    """
    idx_s = start_idx
    idx_e = start_idx + 1
    key_len = len(key)
    del_len = len(delimit)
    image_url_list = []
    not_eof = True
    while not_eof:
        idx_s = html_text.find(key, idx_s)
        idx_e = html_text.find(delimit, idx_s + 1)

        if idx_s == -1 or idx_e == -1:
            not_eof = False
        else:
            url = html_text[idx_s - 8 + (html_text.find('"', idx_s) - idx_s):
                            html_text.find('"', idx_e)]
            url = url.split()[1][5:]
            if url[-1] == '"':
                url = url[:-1]
            image_url_list.append(url)  # Magic numbers to create clean URLS
            idx_s = idx_s + key_len + 1
            idx_e = idx_e + del_len + 1
    return image_url_list


def try_load(url_file_path: str, start: int = 0) -> None:
    f = open(url_file_path, 'r')
    image_url_list = f.read().split('\n')
    f.close()
    for i in range(start, len(image_url_list)):
        numb = '0' * (4 - len(str(i))) + str(i)
        file_str = 'a{}.{}'.format(numb, 'jpg')
        try:
            with open(file_str, 'wb') as handle:
                response = requests.get(image_url_list[i], stream=True)
                if not response.ok:
                    print
                    response
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
        except:
            pass


if __name__ == '__main__':
    url_list = 'image_url.txt'
    try_load(url_list)
