FROM node:22-slim

# one-time system setup
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    rm -rf /var/lib/apt/lists/*

# create a venv owned by node user
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# install Python deps once
COPY requirements.txt execute-requirements.txt ./
RUN pip install uv && \
    uv pip install -r requirements.txt -r execute-requirements.txt

# install mystmd globally (via npm)
RUN npm install -g mystmd serve




WORKDIR /app

# Build site
RUN myst build --html

CMD ["npx", "serve", "-p", "3000", "_build/html"]
