from flask import Flask, render_template


app = Flask('Some site')
        

@app.route('/')
def hello():
    return '<H1>Hello! This is our main page</H1>'


@app.route('/list')
def show_full_list():
    with open('h3_textfile') as f:
        lines = f.readlines()
    return render_template('h3_template_general.html', lines=lines)


@app.route('/filter/<word>')
def show_lines_with_word(word):
    with open('h3_textfile') as f:
        lines = [line for line in f.readlines() if word in line]
    return render_template('h3_filter_list.html', lines=lines, word=word)


@app.route('/show/<int:number>')
def show_first_lines(number):
    with open('h3_textfile') as f:
        lines = f.readlines()[:number]
    return render_template('h3_list_first_lines.html', lines=lines, number=number)


if __name__ == '__main__':
    app.run()