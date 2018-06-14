### Testing heroku application wth cURL

```bash
$ curl -X POST https://shortify-lezou.herokuapp.com/api/shortify  -d "destination=https://www.google.com/"

{"destination":"https://www.google.com/","slug":"QWPrDUx"}
```

- Visit `https://shortify-lezou.herokuapp.com/QWPrDUx` to be redireted to `https://www.google.com/`

### Installation and running dev server

- Install Python3 (using [Homebrew](http://docs.python-guide.org/en/latest/starting/install3/osx/))

- Make sure the Python3 bin directory is added to your PATH. 
- Example:
`$ export PATH=/Users/lezoudali/Library/Python/3.6/bin:$PATH`

- Install [pipenv](https://docs.pipenv.org/) using `pip`.

- Start the `pipenv` virtualenv

`$ pipenv shell`

- Install dependencies with `pipenv`

`$ pipenv install --dev`

- Install redis using homebrew
`$ brew install redis`

`$ brew services start redis`

- Add the `shortify` directory to your PYTHONPATH. Example:

`$ export PYTHONPATH='/Users/lezoudali/Dev/shortify`

- Run `$ make dev` to start dev server

- Run `$ make test` to run tests
