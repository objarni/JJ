import markdown2


def render_html(md):
    return markdown2.markdown(md)


if __name__ == '__main__':
    import webbrowser

    with open('tmp.html') as f:
        html = f.read()

    with open('jj.html', 'w') as f:
        md = """
    Searched for "git" found these entries:
    =======================================

    Onsdag 20e mars 2019
    --------------------

    **git co -b branch_name** - skapa och checka ut ny branch.

    Ett Python kodexempel:

        def fn(x, y):
            return 2


    """
        content = markdown2.markdown(md)
        f.write(html.replace('{{ content }}', content))

    webbrowser.open('jj.html')

