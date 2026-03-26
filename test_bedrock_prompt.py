import boto3
from botocore.exceptions import ClientError

# Bedrock client
bedrock_runtime = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1'   # Try 'us-west-2' if this still fails
)

# Use the inference profile that worked for you earlier
WORKING_MODEL_ID = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"   # or "us.anthropic.claude-sonnet-4-5-20250929-v1:0"

def invoke_claude(prompt: str):
    try:
        response = bedrock_runtime.converse(
            modelId=WORKING_MODEL_ID,
            messages=[{"role": "user", "content": [{"text": prompt}]}],
            inferenceConfig={
                "maxTokens": 1000,
                "temperature": 0.7          # Only temperature — no topP
            }
        )
        output_text = response['output']['message']['content'][0]['text']
        return output_text
        
    except ClientError as e:
        print(f"ERROR: {e}")
        return None

# === Test ===
if __name__ == "__main__":
    test_prompt = """You are an expert QA engineer. 
    Given this requirement: "User can log in with email and password"
    Generate 5 detailed Playwright test cases (positive, negative, and edge cases).
    Output only clean, ready-to-run code in a markdown code block."""
    
    print(f"Sending prompt to Claude Sonnet 4.5...\n")
    result = invoke_claude(test_prompt)
    
    if result:
        print("SUCCESS! Claude's response:\n")
        print(result)