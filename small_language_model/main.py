from langchain.llms import CTransformers

def build_llm():
    try:
        MAX_NEW_TOKENS=1000
        TEMPERATURE=0.01
        MODEL_TYPE='llama'
        # Initialize the CTransformers model with specified configurations
        llm = CTransformers(
            model="TheBloke/Llama-2-7b-Chat-GGML",  # Ensure the model path or repo ID is correct
            model_type=MODEL_TYPE,  # Specify the type of model (e.g., "llama")
            config={
                'max_new_tokens': MAX_NEW_TOKENS,  # Maximum tokens to generate
                'temperature': TEMPERATURE  # Sampling temperature
            }
        )
        print("LLM loaded successfully!")
        return llm

    except RuntimeError as e:
        print(f"RuntimeError: {e}")
        print("Ensure the model file and model_type are compatible.")
        raise

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def ask_question(question: str):
    # Get the LLM instance
    print("hello world")
    llm = build_llm()
    # Ask the question to the LLM
    response = llm(question)  # Assuming `llm()` works as a callable interface for querying the model

    # Print the response from the LLM
    print(f"Response: {response}")

# Example of asking a question
ask_question("Please generate the json object of questions and answers from this Text: 'Multimodal generative AI represents a frontier in technological advancement that promises to reshape how we interact with and harness technology across various sectors. By understanding and utilizing this powerful tool, professionals and creatives alike can unlock unprecedented levels of innovation and efficiency. For those looking to delve deeper into the capabilities of generative AI and explore its transformative potential within the business landscape, the Generative AI for Business Transformation course offered by Simplilearn is an excellent resource. This course provides comprehensive insights and practical skills to leverage generative AI effectively in your organization. Embrace the future of AI and enhance your professional toolkit by enrolling today at Generative AI for Business Transformation. Unlock your creative potential and lead the charge in the AI-driven business revolution!'")





# https://github.com/kennethleungty/Llama-2-Open-Source-LLM-CPU-Inference.git