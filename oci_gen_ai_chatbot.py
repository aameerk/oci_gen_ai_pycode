import oci
compartment_id = "ocid1.compartment.oc1..<...>"
CONFIG_PROFILE = "DEFAULT"
config = oci.config.from_file('/Users/danimmar/.oci/config', CONFIG_PROFILE)
# Service endpoint
endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))
generate_text_detail = oci.generative_ai_inference.models.GenerateTextDetails()
llm_inference_request = oci.generative_ai_inference.models.CohereLlmInferenceRequest()
llm_inference_request.prompt = "Create a good blog post title for OCI Generative AI with Python SDK"
llm_inference_request.max_tokens = 100
llm_inference_request.temperature = 1
llm_inference_request.frequency_penalty = 0
llm_inference_request.top_p = 0.75
generate_text_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id="ocid1.generativeaimodel.oc1.us-chicago-1.amaaaaaask7dceyafhwal37hxwylnpbcncidimbwteff4xha77n5xz4m7p6a")
generate_text_detail.inference_request = llm_inference_request
generate_text_detail.compartment_id = compartment_id
generate_text_response = generative_ai_inference_client.generate_text(generate_text_detail)
# Print result
print("**************************Generate Texts Result**************************")
print(generate_text_response.data)