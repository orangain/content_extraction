# encoding: utf-8

from __future__ import unicode_literals, print_function

import os
import re
import HTMLParser
from glob import glob
from io import open, BytesIO

from dragnet import content_extractor
import eatiht
import extractcontent
from goose import Goose
from readability.readability import Document


def main():
    extractors = (
        ('dragnet', extract_by_dragnet),
        ('eatiht', extract_by_eatiht),
        ('extractcontent', extract_by_extractcontent),
        ('goose', extract_by_goose),
        ('readability', extract_by_readability),
    )

    paths = glob('html/*.html')

    for path in paths:
        try:
            with open(path, encoding='utf-8') as f:
                html = f.read()
        except UnicodeDecodeError:
            with open(path, encoding='cp932') as f:
                html = f.read()

        assert isinstance(html, unicode), type(html)

        common_title = unescape_html_entities(
            re.search(r'<title>([^<]*)</title>', html, re.IGNORECASE).group(1).strip())
        assert isinstance(common_title, unicode), type(common_title)
        print(common_title)

        for extractor_name, extractor in extractors:
            content = extractor(html)

            if 'title' not in content:
                content['title'] = common_title

            assert isinstance(content['title'], unicode), type(content['title'])
            assert isinstance(content['body'], unicode), type(content['body'])

            output_dir = 'content_{0}/'.format(extractor_name)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_path = path.replace('html/', output_dir + '/').replace('.html', '.txt')

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content['title'])
                f.write('\n\n')
                f.write(content['body'])


def extract_by_dragnet(html):
    content = content_extractor.analyze(html)

    return {
        'body': content.decode('utf-8'),
    }


def extract_by_eatiht(html):
    f = BytesIO(html.encode('utf-8'))
    try:
        body = ensure_unicode(eatiht.extract(f))
    except IndexError:
        body = '!!ERROR!!'

    return {
        'body': body,
    }


def extract_by_extractcontent(html):
    extractor = extractcontent.ExtractContent()
    extractor.analyse(html)
    text, title = extractor.as_text()

    return {
        'title': title,
        'body': text,
    }


def extract_by_goose(html):
    g = Goose()
    article = g.extract(raw_html=html)

    return {
        'title': article.title,
        'body': article.cleaned_text,
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
    if isinstance(str_or_unicode, unicode):
        return str_or_unicode

    return str_or_unicode.decode('utf-8')


def unescape_html_entities(text):
    parser = HTMLParser.HTMLParser()
    return parser.unescape(text)


if __name__ == '__main__':
    main()
