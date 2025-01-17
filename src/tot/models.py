# import os
# import openai
# import backoff
from genai.model import Model
from genai.schemas import GenerateParams
from genai import Credentials
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
creds = Credentials(api_key, api_endpoint="https://bam-api.res.ibm.com/v1")

# completion_tokens = prompt_tokens = 0

# api_key = os.getenv("OPENAI_API_KEY", "")
# if api_key != "":
#     openai.api_key = api_key
# else:
#     print("Warning: OPENAI_API_KEY is not set")

# api_base = os.getenv("OPENAI_API_BASE", "")
# if api_base != "":
#     print("Warning: OPENAI_API_BASE is set to {}".format(api_base))
#     openai.api_base = api_base

# @backoff.on_exception(backoff.expo, openai.error.OpenAIError)
# def completions_with_backoff(**kwargs):
#     return openai.ChatCompletion.create(**kwargs)

# def gpt(prompt, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
#     messages = [{"role": "user", "content": prompt}]
#     return chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)

# def chatgpt(messages, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
#     global completion_tokens, prompt_tokens
#     outputs = []
#     while n > 0:
#         cnt = min(n, 20)
#         n -= cnt
#         res = completions_with_backoff(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens, n=cnt, stop=stop)
#         outputs.extend([choice["message"]["content"] for choice in res["choices"]])
#         # log completion tokens
#         completion_tokens += res["usage"]["completion_tokens"]
#         prompt_tokens += res["usage"]["prompt_tokens"]
#     return outputs

# def gpt_usage(backend="gpt-4"):
#     global completion_tokens, prompt_tokens
#     if backend == "gpt-4":
#         cost = completion_tokens / 1000 * 0.06 + prompt_tokens / 1000 * 0.03
#     elif backend == "gpt-3.5-turbo":
#         cost = completion_tokens / 1000 * 0.002 + prompt_tokens / 1000 * 0.0015
#     return {"completion_tokens": completion_tokens, "prompt_tokens": prompt_tokens, "cost": cost}


def watsonx(
    prompt,
    model="meta-llama/llama-2-70b-chat",
    temperature=1,
    max_tokens=300,
    n=1,
    stop="[NOSTOP]",
    k=50,
) -> list:
    params = GenerateParams(
        decoding_method="sample",
        max_new_tokens=max_tokens,
        min_new_tokens=1,
        stream=False,
        temperature=temperature,
        top_k=k,
        top_p=1,
        stop_sequences=[stop],
    )
    llm = Model(model=model, params=params, credentials=creds)
    responses = llm.generate([prompt] * n)
    return [r.generated_text for r in responses]


if __name__ == "__main__":
    print(watsonx("Hello, ", n=2))
