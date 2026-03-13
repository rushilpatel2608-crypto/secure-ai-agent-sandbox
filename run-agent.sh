#!/bin/bash

docker run -it \
--network agent-net \
--cpus="1" \
--memory="2g" \
--pids-limit=200 \
--security-opt=no-new-privileges \
--cap-drop=ALL \
--user 1001:1001 \
--tmpfs /tmp \
--read-only \
-e HTTP_PROXY=http://agent-proxy:3128 \
-e HTTPS_PROXY=http://agent-proxy:3128 \
-v ~/projects/clawbot/repos:/workspace/repos \
-v ~/projects/clawbot/builds:/workspace/builds \
-v ~/projects/clawbot/logs:/workspace/logs \
clawbot-agent
