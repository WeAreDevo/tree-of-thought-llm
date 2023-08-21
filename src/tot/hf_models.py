import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig


class Beluga:
    def __init__(self, name) -> None:
        self.name = name
        self.text_generartion_pipeline()

    def _gptq_text_generation_pipeline(self):
        tokenizer = AutoTokenizer.from_pretrained(self.name, use_fast=True)
        model_basename = "model"
        model = AutoGPTQForCausalLM.from_quantized(
            self.name,
            model_basename=model_basename,
            quantize_config=None,
            use_safetensors=True,
            trust_remote_code=True,
        )

        self.pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            return_full_text=False,
            device="cuda:0",
            quantize_config=None,
        )

    def text_generartion_pipeline(self):
        self.pipe = pipeline("text-generation", model=self.name,
            return_full_text=False,
            device="cuda:0",)

    def generate(
        self,
        prompt,
        temperature=0.7,
        max_tokens=500,
        n=1,
        k=50,
    ) -> list:
        responses = self.pipe(
            prompt,
            num_return_sequences=n,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=temperature,
            top_k=k,
        )
        return [r['generated_text'] for r in responses]


if __name__ == "__main__":
    model = Beluga("Open-Orca/OpenOrca-Platypus2-13B")
    r = model.generate("Hello, ", n=2, max_tokens=10)
    print(r)
