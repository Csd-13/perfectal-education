from src.services.content_generator import ContentGenerator, EducationalContentType

def test_generate_summary():
    generator = ContentGenerator()
    summary = generator.generate_content("Physics", EducationalContentType.SUMMARY, language="en")
    assert "Physics" in summary["generated_content"]

def test_generate_quiz():
    generator = ContentGenerator()
    quiz = generator.generate_content("Math", EducationalContentType.QUIZ, language="en")
    assert "questions" in quiz
