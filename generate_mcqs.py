import json

def fetch_mcqs():
    # Placeholder for actual scraping. Sample question below.
    mcqs = [
        {
            "question": "What is the capital of Bhutan?",
            "options": ["Thimphu", "Kathmandu", "Dhaka", "Lhasa"],
            "answer": "Thimphu"
        },
        {
            "question": "Which river originates from Amarkantak Plateau?",
            "options": ["Narmada", "Godavari", "Krishna", "Mahanadi"],
            "answer": "Narmada"
        }
    ]
    return mcqs

def update_questions_js(mcqs):
    with open('questions.js', 'w', encoding='utf-8') as f:
        f.write('const questions = ')
        json.dump(mcqs, f, indent=2)
        f.write(';')

if __name__ == "__main__":
    mcqs = fetch_mcqs()
    update_questions_js(mcqs)
