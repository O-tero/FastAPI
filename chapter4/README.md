# Templating in FastAPI

Templating is the process of displaying the data gotten from the API in various formats.
Acst as a frontend component in web applications.

## Jinja2

Jinja is a templating engine written in Python designed to help the rendering process of
API responses.
The Jinja templating engine makes use of curly brackets { } to distinguish its expressions
and syntax from regular HTML, text and any other variable in the template file.
The {{ }} syntax is called a variable block. The {% %} syntax houses control structures
such as if/else, loops, and macros.
The three common syntax blocks used in the Jinja templating language include
the following:

- `{% … %}` – This syntax is used for statements such as control structures.
- `{{ todo.item }}` – This syntax is used to print out the values of the expressions
  passed to it.
- `{# This is a great API book! #}` – This syntax is used when writing
  comments and is not displayed on the web page.

### Filters

A filter is separated from the variable by a pipe symbol (|) and may entertain optional arguments in parentheses.
Defined in this formats:
`{{ variable | filter_name(*args) }}`

If there are no arguments, the definition becomes the following:
`{{ variable | filter_name }}`

#### Commonly used filters

- The default filter
  The default filter variable is used to replace the output of the passed value if it turns out
  to be None:
  `{{ todo.item | default('This is a default todo item') }}`
  This is a default todo item

- The escape filter
  This filter is used to render raw HTML output:
  `{{ "<title>Todo Application</title>" | escape }}`
  `<title>Todo Application</title>`

- The conversion filters
  These filters include int and float filters used to convert from one data type to another:
  `{{ 3.142 | int }}`
  3

`{{ 31 | float }}`
31.0

- The join filter
  This filter is used to join elements in a list into a string as in Python:
  `{{ ['Packt', 'produces', 'great', 'books!'] | join(' ') }}`
  Packt produces great books!

The length filter
This filter is used to return the length of the object passed. It fulfills the same role as len() in Python:
Todo count: `{{ todos | length }}`
Todo count: 4

#### Using if statements

The usage of if statements in Jinja is similar to their usage in Python. if statements are
used in the {% %} control blocks. Let’s look at an example:
`{% if todo | length < 5 %}`
You don't have much items on your todo list!
`{% else %}`
You have a busy day it seems!
`{% endif %}`

#### Loops

We can also iterate through variables in Jinja. This could be a list or a general function, such as the following, for example:
`{% for todo in todos %}`
<b> `{{ todo.item }} </b>`
`{% endfor %}`
You can access special variables inside a for loop, such as loop.index, which gives the index of the current iteration

### Macros

A macro in Jinja is a function that return an HTML string. The main use case for macros is to avoid the repetition of code and instead use a single function call.
For example, an input macro is defined to reduce the continuous definition of input tags in an HTML form:
`{% macro input(name, value='', type='text', size=20 %}`
`<div class="form">`
`<input type="{{ type }}" name="{{ name }}"`
`value="{{ value|escape }}" size="{{ size }}">`
`</div>`
`{% endmacro %}`

Now, to quickly create an input in your form, the macro is called:
`{{ input('item') }}`

This will return the following:
`<div class="form">`
`<input type="text" name="item" value="" size="20">`
`</div>`
