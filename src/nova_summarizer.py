import boto3
import json

def summarize_with_nova(text):
    client = boto3.client(
        "bedrock-runtime",
        region_name="us-east-1"
    )

    prompt = f"""
    Summarize the following transcript clearly and concisely:

    {text}
    """

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = client.invoke_model(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]
