from sdg_hub import FlowRegistry,Flow
from datasets import Dataset, load_dataset
#FlowRegistry.discover_flows()

flow_path = FlowRegistry.get_flow_path("green-clay-812")
flow = Flow.from_yaml(flow_path)

recs = flow.get_model_recommendations()
print(f"Default model: {recs['default']}")
print(f"Other 'compatible' models: {recs['compatible']}")
print(f"Experimental models: {recs['experimental']}")

print("But I don't have the memory for any of these. So let's try something smaller!")

flow.set_model_config(
    model=f"ollama/ministral-3:3b", #Using ministral here, but this can be set to any other model that allows the generate API
    api_base="http://localhost:11434", #Change this if your ollama server is running somewhere else
    api_key="my_api_key" #Technically you don't need an API key for local Ollama, but this seems to help stop some connection errors
)

requirements = flow.get_dataset_requirements()
if requirements:
    print(f"Required columns: {requirements.required_columns}")

dataset = load_dataset("danidanou/Bloomberg_Financial_News", split="train") #This is the dataset used in one of SDG Hub's examples, so I will use it here for comparison.

datasubset = dataset.shuffle(42).select(range(10)).rename_column("Article","text")

data_pd = datasubset.to_pandas()
results = flow.generate(data_pd)