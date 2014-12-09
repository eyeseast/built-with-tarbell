Built With Tarbell
==================

This is a public catalog of projects built with [Tarbell](https://github.com/tarbell-project/tarbell). 


Quickstart
----------

Assuming you're using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv builtwithtarbell && cdvirtualenv
    $ tarbell install <repo>
    $ cd <repo>
    $ pip install -r requirements.txt
    $ tarbell serve


Adding projects:
----------------

1. Fork the repo
2. Add a post under `_posts`. Make sure it has the necessary fields (see below)
3. Send a pull request


### Post format

Posts are written in Markdown using YAML Frontmatter. Here's a complete example:

    ---
    title: Crime and Punishment in Chicago
    link: http://crime-punishment.smartchicagoapps.org/
    repo: https://github.com/sc3/crime-punishment
    date: "July 18, 2014"
    credit: Smart Chicago Collaborative
    ---

    Crime and Punishment in Chicago is an index of data sources surrounding this criminal justice system as it is in Chicago. We track data sources from the commission of the crime all the way to prison. We aggregate sources of data, provide insight into how this data is generated, discuss how to get it, and expose what data is unavailable.

The only required fields are `title`, `date` and `link`. If the project doesn't have an obvious publish date, just use the date you're adding the project here.

