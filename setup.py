import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='generator3', 
    url='https://github.com/themysticsavages/generator3',                    
    version='0.0.5',                        
    author='themysticsavages',
    license='MIT',        
    description='Scratch API wrapper',
    long_description=long_description,      
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],                                      
    python_requires='>=3.6',                 
    install_requires=['requests', 'flask']                    
)