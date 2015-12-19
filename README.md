# content_extraction
Comparison of libraries to extract content from HTML

## Libraries to Compare

* [dragnet](https://pypi.python.org/pypi/dragnet)
* [eatiht](https://pypi.python.org/pypi/eatiht)
* [extractcontent](https://github.com/yono/python-extractcontent)
* [goose](https://pypi.python.org/pypi/goose-extractor/)
* [readability](https://pypi.python.org/pypi/readability-lxml)

## Usage

### Setup

```
$ ./download.sh
```

This will store html files in `html` dir.

### For Python 2

```
$ pip install -r requirements.txt
$ python extract.py
```

This will extract contents in `content_*` dir.

### For Python 3

```
$ pip install -r requirements.py3.txt
$ python extract_py3.py
```

This will extract contents in `py3_content_*` dir.
