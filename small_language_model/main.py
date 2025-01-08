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







def pdf_to_text(file_name):
        file_path = os.path.join(pdf_path, file_name)
        print("file_path : ", file_path)
        extracted_text = []
        all_text = ""
        if file_path:
            # ""
            # classifier_result = Get_Pdf_to_Text.classifier(file_path)
            # if 0 in classifier_result:
            print("before convert to ")
            images = convert_from_path(file_path)
            print("before convert from ")
            #     if images:
            #         for i in range(len(images)):
            #             text = pytesseract.image_to_string(images[i])
            #             extracted_text.append({"text": text, "page_no": i + 1})
            #         return extracted_text
            #     else:
            #         return extracted_text
            # else:
            #     with open(file_path, "rb") as f:
            #         pdf = pdftotext.PDF(f)
            #         if pdf:
            #             for i in range(len(pdf)):
            #                 extracted_text.append({"text": pdf[i], "page_no": i + 1})
            #             return extracted_text
            #         else:
            #             return extracted_text
            if images:

                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                for i in range(len(images)):
                    text = pytesseract.image_to_string(images[i], config=custom_config)
                    all_text = all_text + " "+ text
                    extracted_text.append({"text": text, "page_no": i + 1})
                    print("extracted text 1 : ", extracted_text)
                return extracted_text, all_text
            else:
                print("extracted text 2 : ",extracted_text)
                return extracted_text, all_text
        else:
            return extracted_text, all_text



# https://github.com/kennethleungty/Llama-2-Open-Source-LLM-CPU-Inference.git
