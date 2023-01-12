title_of_article = input()
print(f"<h1>\n    {title_of_article}\n</h1>")

content_of_article = input()
print(f"<article>\n    {content_of_article}\n</article>")

next_line = input()

while not next_line == 'end of comments':
    print(f"<div>\n    {next_line}\n</div>")

    next_line = input()


