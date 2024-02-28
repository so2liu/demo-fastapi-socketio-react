FROM node:20 as build
WORKDIR /app
COPY client/package.json .
COPY client/pnpm-lock.yaml .  
RUN npm install -g pnpm && pnpm install
COPY client/ .
RUN pnpm run build


FROM python:3.11-slim

WORKDIR /app
RUN apt-get update && apt-get install -y nginx curl gcc
COPY server/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY server /app/server
COPY ci/nginx.conf /etc/nginx/nginx.conf
COPY ci/app.conf /etc/nginx/conf.d

COPY --from=build /app/dist /usr/share/nginx/html

CMD service nginx start && uvicorn server.main:app --host 0.0.0.0 --port 8000