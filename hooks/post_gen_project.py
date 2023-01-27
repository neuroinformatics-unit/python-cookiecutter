import shutil
create_docs = '{{ cookiecutter.create_docs }}'

if __name__ == "__main__":
    if create_docs != "yes":
        shutil.rmtree("docs", ignore_errors=True)
    shutil.rmtree("licenses", ignore_errors=True)
