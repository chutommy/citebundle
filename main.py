import jinja2 as jj

environment = jj.Environment(loader=jj.FileSystemLoader("templates"))
template = environment.get_template("list.html")

papers = [
    {"title": "Paper 1", "authors": "Author 1", "doi": "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css"},
    {"title": "Paper 2", "authors": "Author 1", "doi": "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css"},
    {"title": "Paper 3", "authors": "Author 1", "doi": "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css"},
    {"title": "Paper 4", "authors": "Author 1", "doi": "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css"},
    {"title": "Paper 5", "authors": "Author 1", "doi": "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css"},
]

filename = "output.html"
content = template.render(papers=papers)

with open(filename, mode="w", encoding="utf-8") as file:
    file.write(content)
