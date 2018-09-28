# Automated tests basics

## Requirements:

1. Linux
2. Google Chrome
3. Python 2.7
4. [pip](https://pip.pypa.io/en/stable/installing/)


## Environment setup

#### 1. Setup virtualenv
[https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)


Install virtualenv package:
```bash
$ pip install virtualenv
```

Create virtualenv:
```bash
$ virtualenv .env
```

Activate virtualenv:
```bash
$ source .env/bin/activate
```

#### 2. Install Python Libraries

```bash
$ pip install -r requirements.txt
```

#### 3. Install Chromedriver

Dowanload latest Chromedriver from: [http://chromedriver.chromium.org/downloads](http://chromedriver.chromium.org/downloads)<br>
Unzip package and move `chromedriver` binary to `.env/bin`


## Python testing frameworks


#### unittest

Introduction: [http://pythontesting.net/framework/unittest/unittest-introduction/](http://pythontesting.net/framework/unittest/unittest-introduction/)

Documentation: [http://docs.python.org/2/library/unittest.html](http://docs.python.org/2/library/unittest.html)

Assertions methods: [https://docs.python.org/2/library/unittest.html#unittest.TestCase](https://docs.python.org/2/library/unittest.html#unittest.TestCase)

###### Execute examples:

```
$ python -m unittest discover test
```


#### PyTest
Introduction: [http://pythontesting.net/framework/pytest/pytest-introduction/](http://pythontesting.net/framework/pytest/pytest-introduction/)

###### Execute examples:

```
$ pytest -s test
```

Note that `pytest` auto-detects also unittest-based test cases.


## Selenium

Introduction: [https://selenium-python.readthedocs.io/getting-started.html](https://selenium-python.readthedocs.io/getting-started.html)

Documentation: [https://seleniumhq.github.io/selenium/docs/api/py/api.html](https://seleniumhq.github.io/selenium/docs/api/py/api.html)

#### 1. Start demoapp

```
$ python demoapp/server.py
```

Open [http://localhost:7272/](http://localhost:7272/)

Try to login with username `demo` and password `mode` and with invalid credentials.


#### 2. Run sample test

```
$ cd selenium && python test_login.py
```

Take a look at screeenshots in `selenium/reports` folder.


#### 3. Create automated test cases for valid and invalid login

```Python
    def test_valid_login(self):
        """TODO: valid login scenario"""
        pass

    def test_invalid_login(self):
        """TODO: invalid login scenario"""
        pass
```

## Flask test client

Doc: [http://flask.pocoo.org/docs/1.0/testing/](http://flask.pocoo.org/docs/1.0/testing/)


#### 1. Start sample RestAPI

```
$ python test_client/app.py
```

Open [http://localhost:5000/ui](http://localhost:5000/ui) and try out sample Rest API

#### 2. Run sample tests

```
$ pytest test_client
```

#### 3. Create automated test for new Pet creation

```
def test_get_pets_on_empty_db(client):
    result = client.get('/pets')
    assert result.status_code == 200
    assert result.json == []


def test_put_pet(client):
    # TODO: Pet creation scenario
    pass
```

## Robot Framework

Website: [http://robotframework.org/](http://robotframework.org/)

User guide and standard libraries docs: [http://robotframework.org/robotframework/](http://robotframework.org/robotframework/)

Selenium library: [http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html](http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)

#### 1. Start demoapp

```
$ python demoapp/server.py
```

#### 2. Run sample tests

```
$ pybot -d robot/results robot
```

#### 3. Open log: `robot/results/log.html`
