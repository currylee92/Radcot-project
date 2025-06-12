import os
import openai
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

class LLMInterface:
    """Interface for large language models."""
    
    def generate(self, prompt):
        """Generate text based on prompt."""
        raise NotImplementedError("Subclasses must implement generate()")

class GPT4oModel(LLMInterface):
    """Interface for OpenAI's GPT-4o model."""
    
    def __init__(self):
        """Initialize GPT-4o model."""
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
    def generate(self, prompt, temperature=0.7):
        """
        Generate text using GPT-4o.
        
        Args:
            prompt (str): Input prompt
            temperature (float): Sampling temperature
            
        Returns:
            str: Generated text
        """
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a radiological assistant specialized in detecting errors in radiology reports."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=2000
        )
        return response.choices[0].message.content

class LlamaModel(LLMInterface):
    """Interface for Meta's Llama 3 model."""
    
    def __init__(self, model_size="70b"):
        """
        Initialize Llama 3 model.
        
        Args:
            model_size (str): Size of the model (70b)
        """
        model_name = f"meta-llama/Llama-3-{model_size}"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype="auto"
        )
        
    def generate(self, prompt, temperature=0.7):
        """
        Generate text using Llama 3.
        
        Args:
            prompt (str): Input prompt
            temperature (float): Sampling temperature
            
        Returns:
            str: Generated text
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            inputs.input_ids,
            max_new_tokens=2000,
            temperature=temperature,
            do_sample=True
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)[len(prompt):]

class MixtralModel(LLMInterface):
    """Interface for Mistral AI's Mixtral 8x22b model."""
    
    def __init__(self):
        """Initialize Mixtral 8x22b model."""
        model_name = "mistralai/Mixtral-8x22B-v0.1"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype="auto"
        )
        
    def generate(self, prompt, temperature=0.7):
        """
        Generate text using Mixtral.
        
        Args:
            prompt (str): Input prompt
            temperature (float): Sampling temperature
            
        Returns:
            str: Generated text
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            inputs.input_ids,
            max_new_tokens=2000,
            temperature=temperature,
            do_sample=True
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)[len(prompt):]

def load_model(model_name):
    """
    Load a language model by name.
    
    Args:
        model_name (str): Name of the model to load
        
    Returns:
        LLMInterface: Model interface
    """
    if model_name.lower() == "gpt-4o":
        return GPT4oModel()
    elif model_name.lower() == "llama-3-70b":
        return LlamaModel(model_size="70b")
    elif model_name.lower() == "mixtral-8x22b":
        return MixtralModel()
    else:
        raise ValueError(f"Unsupported model: {model_name}")