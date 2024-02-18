# LLM-docker

## Requirements:

- Docker

## To run llm backend server run

```sh
./run_llm.sh
```

## To test llm backend server run

- For only llm initialization and running one inference

```sh
./test_llm.sh --test
```

- For interactive chat without memory try

```sh
./test_llm.sh --chat
```

## LLM usage

- inside docker LLM backend server run on port 9000, you can remap it by mapping to different host port eg:

```sh
./run_llm.sh 8000
```

- there are you HTTP POST endpoints:

  - _/initialize_
  - _/generate_

### Endpoint examples of usage:

```sh
curl -s -X POST http://localhost:<PORT>/initialize/ \
     -H "Content-Type: application/json" \
     -d '{
           "model": "Phi2",
           "max_total_tokens": 300,
           "quantization": "q8"
         }'
```

```sh
curl -X POST http://localhost:<PORT>/generate/ \
     -H "Content-Type: application/json" \
     -d '{"prompt": "<USER PROMPT>"}'
```

## NOTE:

- Initialization of LLM may take some time in the first run because of downloading up to 3GB of model data
