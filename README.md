# 🧪 AI QA Test Case Generator

**An AI-powered web app that instantly generates high-quality Playwright test cases from plain-English requirements.**

Built as a portfolio project to demonstrate practical AI skills in Quality Engineering and Test Automation using **Amazon Bedrock** and **Claude Sonnet 4.5**.

![Demo Screenshot](screenshot.png)  
*(Replace this line with an actual screenshot of your running app after you take one)*

## ✨ Features

- Generate 6 structured Playwright test cases from any user story or requirement
- Balanced coverage: 2 positive/happy path, 2 negative/error, 2 edge/boundary cases
- Uses modern Playwright best practices (async/await, clear assertions, comments)
- Powered by **Claude Sonnet 4.5** on **Amazon Bedrock** (via Converse API)
- Simple, clean Streamlit interface — no frontend experience needed
- Ready-to-copy test code output

## 🛠️ Tech Stack

- **Python** 3.11+
- **Streamlit** – for the web UI
- **Amazon Bedrock** – with Claude Sonnet 4.5 (inference profile)
- **boto3** – AWS SDK for Python

## 🚀 Quick Start

### Prerequisites
- An AWS account with access to Amazon Bedrock (Claude models enabled)
- Python 3.11 or higher
- AWS credentials configured (`aws configure`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-qa-test-generator.git
   cd ai-qa-test-generator