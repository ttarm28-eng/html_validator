#!/bin/python3

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the stack.py file.
    # The main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags.
    if "<" in html and ">" not in html:
        return False
    all_tags = _extract_tags(html)
    stack = []
    for tag in all_tags:
        if tag.startswith("</"):
            name = tag[2:-1]
            if len(stack) == 0:
                return False
            if stack[-1] == name:
                stack.pop()
            else:
                return False
        else:
            name = tag[1:-1]
            stack.append(name)
    return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    is_inside = False
    char_in_tag = ""
    for char in html:
        if char == "<":
            is_inside = True
        elif char == ">":
            is_inside = False
            only_tag = char_in_tag.split()[0]
            tags.append("<" + only_tag + ">")
            char_in_tag = ""
        elif is_inside:
            char_in_tag += char
    if is_inside:
        raise ValueError("found < without matching >")
    return tags
