Django `for` Tags
=================

In this part, we will essentially looks at examples which will be clear to understands the concepts of `for` Loops


For Loops
---------
The following example shows a loop through items of a list

.. code-block:: HTML
    
    <!DOCTYPE html>
    <html>
    <body>
    {% for x in fruits %}
        <h1>{{ x }}</h1>
    {% endfor %}
    </body>
    </html>

Here, through a list of dictionaries : 


.. code-block:: Python
    :caption: views.py

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

Data From a Model
-----------------

Data in a model is like a table with rows and columns. The `Member` 
model we created earlier has five rows, and each row has three columna

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

.. list-table:: 
    :widths: 20 20 20 20 20
    :header-rows: 1

    * - id
      - firstname
      - lastname
      - phone
      - joined_date
    * - 1
      - Stalikken
      - Refsnes
      - 555987
      - 2024-11-01
    * - 2
      - Lene
      - Refnes
      - 555654
      - 2024-11-20
    * - 3 
      - Linus
      - Refnes
      - 555789
      - 2023-01-01
    * - 4
      - Tobias
      - Refnes
      - 555555
      - 2021-01-01
    * - 5 
      - Emil
      - Refnes
      - 5551234
      - 2022-01-05 

When we fetch data from the model, it comes as a 
QuerySet object, with a similar format as the cars 
example above: a list with dictorionaires:

.. code-block:: JavaScript
    :caption: QureySet of Member

    <QuerySet [
        {
            'id': 1,
            'firstname': 'Emil',
            'lastname': 'Refsnes',
            'phone': 5551234,
            'joined_date': datetime.date(2022, 1, 5)
        },
        {
            'id': 2,
            'firstname': 'Tobias',
            'lastname': 'Refsnes'
            'phone': 5557777,
            'joined_date': datetime.date(2021, 4, 1)
        },
        {
            'id': 3,
            'firstname': 'Linus',
            'lastname': 'Refsnes'
            'phone': 5554321,
            'joined_date': datetime.date(2021, 12, 24)
        },
        {
            'id': 4,
            'firstname': 'Lene',
            'lastname': 'Refsnes'
            'phone': 5551234,
            'joined_date': datetime.date(2021, 5, 1)
        },
        {
            'id': 5,
            'firstname': 'Stalikken',
            'lastname': 'Refsnes'
            'phone': 5559876,
            'joined_date': datetime.date(2022, 9, 29)
        }
    ]>