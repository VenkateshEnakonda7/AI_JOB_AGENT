# import openai
# import config

# client = openai.OpenAI(
#     api_key=config.OPENROUTER_API_KEY,
#     base_url="https://openrouter.ai/api/v1"
# )

# def craft_resume(original_resume_text, job_description):
#     prompt = f"Here is my original resume:\n{original_resume_text}\n\nPlease modify it to match this job description:\n{job_description}"
#     response = client.chat.completions.create(
#         model="mistralai/mistral-7b-instruct",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['choices'][0]['message']['content']


