Django `for` Tags
=================

In this part, we will essentially looks at examples which will be clear to understands the concepts of `for` Loops


For Loops
---------
The following example shows a loop through items of a list

.. code-block:: HTML
    :linenos:
    <!DOCTYPE html>
    <html>
    <body>
    {% for x in fruits %}
        <h1>{{ x }}</h1>
    {% endfor %}
    </body>
    </html>

Here, through a list of dictionaries : 

.. example-code::
    .. code-block:: Python
        :caption:: views.py

        from django.http import HttpResponse
        from django.template import loader

        def testing(request):
            template = loader.get_template('template.html')    
            context = {
                'cars': [
                    {
                        'brand': 'Ford',
                        'model': 'Mustang',
                        'year': '1964',
                    },
                    {
                        'brand': 'Ford',
                        'model': 'Bronco',
                        'year': '1970',
                    },
                    {
                        'brand': 'Volvo',
                        'model': 'P1800',
                        'year': '1964',
                    }]
                }
            return HttpResponse(template.render(context, request))

    .. code-block:: HTML
        :caption: template.html

        <!DOCTYPE html>
        <html>
        <body>

        {% for x in cars %}
            <h1>{{ x.brand }}</h1>
            <p>{{ x.model }}</p>
            <p>{{ x.year }}</p>
        {% endfor %}

        <p>In views.py you can see what the cars variable looks like.</p>

        
        </body>
        </html>