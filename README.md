# python-df-api-flask
To curl from a linux host
```
curl -X POST -F 'file=@test.csv' http://10.204.111.184:5000/upload
```
To curl from a windows host
```
curl -X POST -F file=@C:\Users\ambar_hassani\Downloads\test.csv "http://10.204.111.184:5000/upload" --output transformed.csv
```
