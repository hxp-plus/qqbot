# Instructions #

To use this robot, you need to deploy coolq, install 2 python modules below.

## Deploy CoolQ on Linux ##

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

## Configure the http plugin to use WebSocket ##

Delete `app/io.github.richardchien.coolqhttpapi/config/<your-qq-number.ini>`. Create `<your-qq-number.json>`, and write this configuration into JSON file.

```
{
    "ws_reverse_api_url": "ws://127.0.0.1:8080/ws/api/",
    "ws_reverse_event_url": "ws://127.0.0.1:8080/ws/event/",
    "use_ws_reverse": true
}
```

See <https://nonebot.cqp.moe/guide/getting-started.html>

## Install python 3.8 form source ##

`Python 3.7` or later is needed for nonebot.

## Install python modules ##

These 2 following modules is needed:

- nonebot
- openpyxl

## Run the robot ##

To run this robot, login on CoolQ with your QQ number and password, and run `qqbot.py`. `qqbot.py` will record the date, time and card whenever a group member upload a thing in the group's album. It will be recorded in `data.txt`

`froms.py` is used to write the data in `data.txt` into xlsx forms, to use it, remember to edit the variables in this script according to your own situations. Note that `student_number_offset` and `date_offset` defines the row number of student ids and date to be recorded in your xlsx. `row_start` defines which row your data starts, since the form has headings.
