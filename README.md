# Rijksapi
Simple search webapp using the Rijksmuseum API



## To get started

Create a config.ini file in root containing:
```
[api]
api_key = <YOUR-API-KEY>
```
Get your own api key at: https://data.rijksmuseum.nl/

On linux run these commands:

```
virtualenv ./venv -p python3.9
source ./venv/bin/activate
pip install -r requirements.txt
python main.py
```

Then open the browser at http://127.0.0.1:5000

## TODO
* todo-list :-)