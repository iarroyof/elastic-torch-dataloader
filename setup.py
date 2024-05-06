from setuptools import setup, find_packages

setup(
    name='elastic_pytorch_loader',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'elasticsearch',
        'numpy',
        'torch',
        'torchvision'
    ],
    python_requires='>=3.6',
    author='Your Name',
    author_email='your.email@example.com',
    description='A PyTorch DataLoader for ElasticSearch.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
