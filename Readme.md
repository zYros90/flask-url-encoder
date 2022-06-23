# Info
A backend in python for encoding and decoding urls

## Install Dependencies
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## See all available commands with:
```
python main.py -h
```

## Start App
i.e. in debug mode on default port 5000
```
python main.py --debug=True
```



## Requests
#### Encode
`POST localhost:5000/encode`

with json:
```
{
    "url": "https://my-long-url.de/abc/xyz"
}
```

#### Decode
`POST localhost:5000/decode`

with json:
```
{
    "url": "http://encode_domain.de/def"
}
```


# Run tests
## Unit Tests
dependency: `pytest`
```
python -m pytest
```
or with Makefile
```
make unit-tests
```

## Integration Test
```
python tests_integration.py
```
or with Makefile
```
make integration-test
```

## Performance Test
```
python python tests_performance.py
```
or with Makefile
```
make performance-test
```
on my machine it took 523 ms for 500 encoding + decoding requests that's around 0.5 ms/req


# Available Environment Variables
`APP_DEBUG` i.e. true

`APP_PORT` i.e. 5001

`APP_ENCODE_DOMAIN` the domain you want to encode to, i.e. http://encode.de/


# used tools
`black` for formatting

`pytest` for unit tests

`pylint` for linting

`docker`

`makefile`


