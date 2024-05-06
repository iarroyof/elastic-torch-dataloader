# Elastic PyTorch Loader

A PyTorch DataLoader for interfacing with ElasticSearch to load documents in batches for training machine learning models.

## Installation

You can install the package using pip:

```bash
pip install git+https://github.com/yourusername/elastic_pytorch_loader.git
```
## Usage Examples

### Basic Usage

To use the `ElasticSearchDataset` with a PyTorch DataLoader, follow these steps:

```python
from elastic_pytorch_loader.dataset import ElasticSearchDataset
from torch.utils.data import DataLoader

# Initialize the dataset with your specific parameters
es_dataset = ElasticSearchDataset(
    index='your_index_name',
    es_page_size=1000,
    batch_size=10,
    async_loading=False,
    shuffle=True,
    seed=42
)

# Create a DataLoader
data_loader = DataLoader(es_dataset, batch_size=None)

# Iterate over the DataLoader in your training loop
for batch in data_loader:
    # Your training logic here
    pass
```

### Asynchronous Loading

To enable asynchronous loading of data:

```python
# Set async_loading to True when initializing the dataset
es_dataset = ElasticSearchDataset(
    index='your_index_name',
    es_page_size=1000,
    batch_size=10,
    async_loading=True,  # Enable asynchronous data loading
    shuffle=True,
    seed=42
)
# The rest is the same as the basic usage
```

### Shuffling Data

Shuffling the data can lead to better training performance:

```python
# Set shuffle to True and specify a seed for reproducibility
es_dataset = ElasticSearchDataset(
    index='your_index_name',
    es_page_size=1000,
    batch_size=10,
    async_loading=False,
    shuffle=True,  # Enable shuffling
    seed=42        # Seed for the random number generator
)

# The rest is the same as the basic usage
```

Make sure to replace `'your_index_name'` with the actual name of the ElasticSearch index you are using. These examples provide a clear guide on how to initialize the dataset with different options and use it with a PyTorch DataLoader.