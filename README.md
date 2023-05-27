#the repo has a demo to write functions from scratch in python, use cli, CI/CD IN GIT, using fastapi and gives a introduction to docker
# functions-from-zero
live training

[![Python application test with Github Actions](https://github.com/anuj672/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/anuj672/functions-from-zero/actions/workflows/main.yml)


### to call microservice 
```bash
curl -X 'POST' \
  'https://anuj672-cautious-doodle-vwjrvxp6qwvfjvr-8080.preview.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "microsoft"
}'

```

### container

`docker build .`