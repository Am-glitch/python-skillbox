import regex
import requests


def search_content_in_tags(source: str, tag: str):
    return regex.findall(rf'(?<=<{tag}.+>\s*)\b.+\b(?=\s*</{tag}>)', source)

if __name__=='__main__':
    source = requests.get('http://www.columbia.edu/~fdc/sample.html').text
    print(search_content_in_tags(source, 'h3'))
