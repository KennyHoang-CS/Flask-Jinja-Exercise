from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lol'

debug = DebugToolbarExtension(app)


@app.route('/')
def ask_story():
    """Show list of stories options. """
    return render_template('select-story.html', stories=stories.values())


@app.route('/questions')
def ask_questions():
    """ Generate and show form to ask words. """
    
    story_id = request.args["story_id"]
    story = stories[story_id]
    
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts,
                            story_id=story_id, title=story.title)

@app.route('/story')
def show_story():
    """ Get words and add them to the story template. """
    story_id = request.args["story_id"]
    story = stories[story_id]
    
    text = story.generate(request.args)
    return render_template('story.html', text=text, title=story.title)