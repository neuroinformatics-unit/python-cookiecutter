import shutil

if __name__ == "__main__":
    { % if cookiecutter.create_docs == "yes" - %}
    shutil.rmtree("docs", ignore_errors=True)
    { % - endif %}
    shutil.rmtree("licenses", ignore_errors=True)
