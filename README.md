# Deploy CoolQ #

``` shell
$ sudo docker pull richardchien/cqhttp:latest
$ mkdir coolq
```
Create `run.sh` and add the following lines without comment:
```
$ docker run -ti --rm --network="host" --name cqhttp-test \
             -v $(pwd)/coolq:/home/user/coolq \
             -p 9000:9000 \
             -p 5700:5700 \
             -e COOLQ_ACCOUNT=<your_qq_number> \
             -e CQHTTP_POST_URL=http://example.com:8080 \ # Post Url,Optional
             -e CQHTTP_SERVE_DATA_FILES=yes \
             richardchien/cqhttp:latest
```
Make it executable by `chmod +x run.sh` and run.

``` shell
$ sudo ./run.sh
```

Visit `http://localhost:9000/` and use the password `MAX8char` to login.

If it asks you to download chrome, just hit `Reject veirfy`






