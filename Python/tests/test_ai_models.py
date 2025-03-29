from src.ai_models.qwen_model import QwenModel

def test_generate_content():
    model = QwenModel()
    content = model.generate_content("Explain gravity", language="en")
    assert "gravity" in content

def test_reasoning_mode():
    model = QwenModel()
    reasoning = model.reasoning_mode("What is the capital of Algeria?")
    assert "reasoning_steps" in reasoning
