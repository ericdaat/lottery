from flask import render_template


def page_not_found(e):
    """ Renders template for 404 error

    Args:
        e: Error

    Returns: 404 error template

    """
    return render_template('errors/404.html', error=e), 404