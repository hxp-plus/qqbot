docker run -ti --rm --network="host" --name cqhttp-test \
             -v $(pwd)/coolq:/home/user/coolq \
             -p 9000:9000 \
             -p 5700:5700 \
             -e COOLQ_ACCOUNT=2529223739 \
             -e CQHTTP_POST_URL=http://localhost:8080 \
             -e CQHTTP_SERVE_DATA_FILES=yes \
             -e CQHTTP_USE_WS=yes \
             richardchien/cqhttp:latest
