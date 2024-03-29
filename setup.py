import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='evergreenfft',  
     version='1.0.1',
     author="Rice",
     author_email="mrseanrice@gmail.com",
     description="A python fft package based on evergreenforest",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/SeanSRice/evergreen_fft.git",
     modules=["evergreen_fft.py", "_evergreen_fft.so"],
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "License :: OSI Approved :: MIT License",
     ],
 )
