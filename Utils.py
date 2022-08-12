import json
# - `load_candidates_from_json(path)` – возвращает список всех кандидатов
# - `get_candidate(candidate_id)` – возвращает одного кандидата по его id
# - `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
# - `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку


def load_candidates_from_json(file_name):
    """Возвращает список всех кандидатов"""
    with open(file_name, encoding='utf-8') as json_file:
        py_list = json.load(json_file)
        return py_list


def get_candidate_by_id(id, py_list):
    """Возращает кандидата по id"""
    for item in py_list:
        if item['id'] == id:
            return item


def get_candidate_by_name(name, py_list):
    """Возращает кандидата по имени"""
    candidates = []
    for item in py_list:
        if name.lower().strip() in item['name'].lower().strip():
            candidates.append(item)
        return candidates



def get_candidates_by_skill(skill, py_list):
    """Возразщает список кандидатов по навыку"""
    candidates_w_skill = []
    for item in py_list:
        if skill.lower().strip() in item['skills'].lower().strip():
            candidates_w_skill.append(item)
    return candidates_w_skill









