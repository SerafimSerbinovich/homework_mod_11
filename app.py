from flask import Flask, render_template
from Utils import *

# Создаем экземпляр класса Flask
app = Flask(__name__)

# Выгружаем данные из JSON файла
candidates = load_candidates_from_json('candidates.json')

# Создаем представление для /. Выводим всех кандидатов
@app.route('/')
def main():
    return render_template('list.html', items=candidates)


#Создаем представление для страницы /candidate/<x>
@app.route('/candidate/<x>')
def candidate_page(x):
    candidate_data = get_candidate_by_id(int(x), candidates)
    return render_template('card.html', candidate=candidate_data)


#Создаем представление для /search/<candidate_name>
@app.route('/search/<candidate_name>')
def search_by_name(candidate_name):
    suitable_candidates = get_candidate_by_name(candidate_name, candidates)
    amount = len(suitable_candidates)
    return render_template('search.html', amount=amount, candidates=suitable_candidates)


#Создаем представление для /skill/<skill_name>
@app.route('/skill/<skill_name>')
def search_by_skill(skill_name):
    suitable_candidates = get_candidates_by_skill(skill_name, candidates)
    amount = len(suitable_candidates)
    return render_template('skill.html', skill=skill_name, amount=amount, candidates=suitable_candidates)


app.run()
