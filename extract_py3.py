# encoding: utf-8

from __future__ import unicode_literals, print_function

import os
import re
from html import unescape
from glob import glob
from io import open, BytesIO

import eatiht
from readability.readability import Document


def main():
    extractors = (
        ('eatiht', extract_by_eatiht),
        ('readability', extract_by_readability),
    )

    paths = glob('html/*.html')

    for path in paths:
        with open(path) as f:
            html = f.read()

        assert isinstance(html, str), type(html)

        common_title = unescape(
            re.search(r'<title>([^<]*)</title>', html, re.IGNORECASE).group(1).strip())
        assert isinstance(common_title, str), type(common_title)
        print(common_title)

        for extractor_name, extractor in extractors:
            content = extractor(html)

            if 'title' not in content:
                content['title'] = common_title

            assert isinstance(content['title'], str), type(content['title'])
            assert isinstance(content['body'], str), type(content['body'])

            output_dir = 'py3_content_{0}/'.format(extractor_name)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_path = path.replace('html/', output_dir + '/').replace('.html', '.txt')

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content['title'])
                f.write('\n\n')
                f.write(content['body'])


def extract_by_eatiht(html):
    f = BytesIO(html.encode('utf-8'))

    return {
        'body': ensure_unicode(eatiht.extract(f)),
    }


def extract_by_readability(html):
    document = Document(html)

    def strip_html(html):
        return re.sub(r'<[^<]+?>', '', html)

    return {
        'title': ensure_unicode(document.short_title()),
        'body': strip_html(ensure_unicode(document.summary())),
    }


def ensure_unicode(str_or_unicode):
    if isinstance(str_or_unicode, str):
        return str_or_unicode

    return str_or_unicode.decode('utf-8')

if __name__ == '__main__':
    main()
