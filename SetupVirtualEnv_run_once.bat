TITLE Setting up virtual env
:: Running it once is fine, this just sets up virtual env >> install all modules there 
py -m venv env && env\scripts\activate.bat && pip install -r requirements.txt

:: Running this multiple time will not make a mess of your setup, dont worry about that a bit.
