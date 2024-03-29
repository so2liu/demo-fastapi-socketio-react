# A demo for FastAPI, SocketIO(v4), React, and Docker

This is an example of a full stack application using FastAPI, SocketIO, React, and Docker. I hope this demo can save you some time when you are trying to build a similar application.

## Screenshot

The webpage will connect to the server and display the current time to a new line every second.

![Screenshot](assets/screenshot.png)

## Running the application in development

1. Clone the repository
2. Install the dependencies

```bash
# in server folder
pip install -r requirements.txt
```

```bash
# in react-client folder
pnpm install
```

3. Run the application

```bash
# in the root folder
uvicorn server.main:app --reload
```

You can also press F5 in VSCode to run the server in debug mode.

```bash
# in react-client folder
pnpm dev
```

## Docker

1. Build the image

```bash
docker build -t demo-fastapi-socketio-react .
```

2. Run the container

```bash
docker run -p 8000:80 -d demo-fastapi-socketio-react
```
