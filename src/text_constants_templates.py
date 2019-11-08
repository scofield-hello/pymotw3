# *-- coding:utf-8 -*

import string

if __name__ == '__main__':
    # capwords将每一个单词都转成大写
    print(string.capwords("hello python, hello world"))

    s = string.Template("""
    FirstName is $FirstName
    LastName is ${LastName}
    Escape $$
    """)
    template_data = {"FirstName": "尼克", "LastName": "W"}
    print(s.substitute(template_data))
    ms = string.Template("""
    FirstName is $FirstName
    LastName is ${LastName}
    Escape $$
    Missing $Missing will not throwing if use safe_substitude
    """)
    print(ms.safe_substitute(template_data))

    interpolation = """
    FirstName is %(FirstName)s
    LastName is %(LastName)s
    Escape %%
    """
    print(interpolation % template_data)

    fmt = """
    FirstName is {FirstName}
    LastName is {LastName}
    Escape {{}}
    """
    print(fmt.format(**template_data))
