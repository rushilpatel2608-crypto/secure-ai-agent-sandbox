FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
git \
curl \
python3 \
python3-pip \
nodejs \
npm \
build-essential \
ca-certificates \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY agents /workspace/agents

CMD ["python3", "/workspace/agents/agent.py"]
