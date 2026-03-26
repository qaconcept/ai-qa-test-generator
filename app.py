import streamlit as st
import boto3
from botocore.exceptions import ClientError

# === Configuration ===
bedrock_runtime = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1'   # Change to 'us-west-2' if you prefer
)

# Use the inference profile that worked in your test script
MODEL_ID = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"   # ← Change if you used a different one (e.g. us.anthropic...)

def generate_test_cases(requirement: str):
    prompt = f"""You are a senior QA automation engineer with 20+ years of experience in enterprise systems.

Requirement / User Story:
"{requirement}"

Generate **6 high-quality Playwright test cases** (Python syntax):
- 2 positive / happy path tests
- 2 negative / error handling tests  
- 2 edge / boundary cases

Rules:
- Use modern Playwright best practices (async/await where appropriate)
- Include clear test names, comments, and assertions
- Make tests realistic for web applications
- Output **ONLY** the test code inside one markdown code block (```python ... ```)
- Do not add extra explanations outside the code block."""

    try:
        response = bedrock_runtime.converse(
            modelId=MODEL_ID,
            messages=[{"role": "user", "content": [{"text": prompt}]}],
            inferenceConfig={
                "maxTokens": 1500,
                "temperature": 0.5          # Only temperature for Sonnet 4.5
            }
        )
        return response['output']['message']['content'][0]['text']
    except ClientError as e:
        return f"**Error calling Bedrock:** {str(e)}\n\nTip: Make sure your AWS credentials are correct and the model is accessible."
    except Exception as e:
        return f"**Unexpected error:** {str(e)}"

# === Streamlit App ===
st.set_page_config(page_title="AI QA Test Generator", page_icon="🧪")
st.title("🧪 AI QA Test Case Generator")
st.markdown("**Powered by Claude Sonnet 4.5 on Amazon Bedrock** | Portfolio Project")

st.write("Paste a requirement or user story below. The AI will generate ready-to-use Playwright tests.")

requirement = st.text_area(
    "Requirement / User Story",
    height=120,
    placeholder="Example: Users can successfully log in with valid email and password. The system should show an error for invalid credentials."
)

if st.button("🚀 Generate Test Cases", type="primary"):
    if requirement.strip():
        with st.spinner("Claude is thinking and generating test cases..."):
            tests = generate_test_cases(requirement)
            st.markdown(tests)
    else:
        st.warning("Please enter a requirement first.")

st.caption("Built as part of AI QA Portfolio | AWS Bedrock + Streamlit | March 2026")
st.markdown("---")
st.info("Tip: Copy the generated code directly into your Playwright test files. Try different requirements to see how the AI adapts.")