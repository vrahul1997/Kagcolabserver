from setuptools import setup, Extension

with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(
        name="kagcolabserver",
        version="0.9.1",
        description="Automate the kaggle data import portion and run codeserver in that directory",
        long_description=long_description,
        long_description_content_type='text/markdown',
        author="Vijay Rahul",
        author_email="vijayvenu1997@gmail.com",
        url="",
        license="MIT",
        py_modules=['kagcolabserver'],
        package_dir={'': 'src'},
        install_requires=["pyngrok>=4.1.12", "kaggle>=1.5.7"],
    )
