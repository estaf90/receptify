from urllib.request import urlopen
from .xml_parser import xml2dict


def api_url(date='20170101'):
    url = f'http://www7.slv.se/apilivsmedel/LivsmedelService.svc/Livsmedel'\
          f'/Naringsvarde/{date}'
    return url


def load_xml(url=None):
    if url is None:
        url = api_url()
    response = urlopen(url)
    xml_bytes = response.read()
    xml = xml_bytes.decode('utf-8')
    return xml


def load_dict_from_url(url=None):
    xml = load_xml(url=url)
    d = xml2dict(xml, is_file=False)
    return d


def load_dict_from_file(filename):
    d = xml2dict(filename, is_file=True)
    return d


if __name__ == '__main__':
    data = load_dict_from_url()
    print(data.keys())
