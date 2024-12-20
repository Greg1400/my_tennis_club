from django.http import HttpResponse
from django.template import loader
from .models import Member
"""
The details view does the following:

Gets the slug as an argument.
Uses the slug to locate the correct record in the Member table.
loads the details.html template.
Creates an object containing the member.
Sends the object to the template.
Outputs the HTML that is rendered by the template.

"""
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    """Retrieves a specific Member b slug and renders the details in a template

    Args:
        request (HttpRequest): Django object containing all information about the request (method, headers, cookies, ...)
        slug (int): Representation of the Member's slug to be retrieved from the DB.

    Returns:
        HttpResponse: Rendered HML from the template with the object passed in the context
    """
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    """This function loads and outputs HTML rendered template

    Args:
        request (HttpRequest): Object containing metadata about the request

    Returns:
        HttpResponse: Object contains the rendered html template
    """
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    """Function that loads a template and the HTML render receives a context

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    template = loader.get_template('template.html')
    return HttpResponse(template.render())
