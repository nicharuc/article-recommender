from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)


@app.route("/")
def articles():
    """Show a list of article titles"""
    titles = [a[1] for a in articles]
    links = [a[0] for a in articles]
    htmltxt = render_template('articles.html', titles = titles, links = links)
    return htmltxt


@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    mapped_vals = map(lambda x: x[0], articles)

    index = mapped_vals.index(topic+'/'+filename)

    title = articles[index][1]
    text = articles[index][2]
    rec = recommended(topic+'/'+filename, articles, 5)
    rectitle = [r[1] for r in rec]
    reclinks = [r[0] for r in rec]

    htmltxt = render_template('article.html', title = title, text = text, rectitle = rectitle, reclinks = reclinks)
    return htmltxt


if __name__ == "__main__":
    i = sys.argv.index('server:app')
    glove_filename = sys.argv[i + 1]
    articles_dirname = sys.argv[i + 2]

    gloves = load_glove(glove_filename)
    articles = load_articles(articles_dirname, gloves)
    app.run(host='0.0,0,0', port=8080)