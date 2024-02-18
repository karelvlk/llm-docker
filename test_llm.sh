#!/bin/bash

# Initial setup - Send initialization request to the server
echo "Initializing chat session..."
init_response=$(curl -s -X POST http://localhost:9000/initialize/ \
     -H "Content-Type: application/json" \
     -d '{
           "model": "Phi2",
           "max_total_tokens": 300,
           "quantization": "q8"
         }')

echo "Initialization response: $init_response"


# Check if initialization was successful
if [[ $init_response != *"LLM initialized"* ]]; then
    echo "Failed to initialize. Exiting."
    exit 1
fi



if [ "$1" = "--chat" ]; then
    # Chat loop
    while true; do
        printf "You: "
        read user_input

        # Exit condition
        if [[ $user_input == "exit" ]]; then
            echo "Exiting chat..."
            break
        fi

        # Send user input to the server and get response
        ai_response=$(curl -s -X POST http://localhost:9000/generate/ \
            -H "Content-Type: application/json" \
            -d "{\"prompt\": \"Human: $user_input AI:\"}")

        stripped_ai_response="${ai_response#AI: }"

        echo ""
        echo "AI: $stripped_ai_response"
        echo ""
    done

    echo "Chat session ended."
elif [ "$1" = "--test" ]; then
    curl -X POST http://localhost:9000/generate/ \
        -H "Content-Type: application/json" \
        -d '{"prompt": "Human: How are you? AI:"}'

else
    echo "Invalid argument. Please use --chat or --test. ❌"
fi
