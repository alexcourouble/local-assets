def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    with open("function/views/index.html") as f:
        return f.read()
