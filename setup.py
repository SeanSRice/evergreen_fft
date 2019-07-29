import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='evergreen_fft',  
     version='1.071',
     author="Rice",
     author_email="mrseanrice@gmail.com",
     description="A python fft package based on evergreenforest",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/SeanSRice/evergreen_fft.git",
     packages=['evergreen_fft'],
     pacage_data = {'evergreen_fft' : evergreen_fft.py, _evergreen_fft.so},
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "License :: OSI Approved :: MIT License",
     ],
 )
