# python-df-api-flask
To curl from a linux host
```
curl -X POST -F 'file=@test.csv' http://10.204.111.184:5000/upload
```
To curl from a windows host
```
curl -X POST -F file=@C:\Users\ambar_hassani\Downloads\test.csv "http://10.204.111.184:5000/upload" --output transformed.csv
```
Instead of docker compose you can also manually build the image using docker build command and then use the docker run command as shown below
```
docker run -dit --rm -p 5000:5000 --name cur_transform py-api-web:latest
```
