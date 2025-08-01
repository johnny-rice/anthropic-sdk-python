import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=3200,
    thinking={"type": "enabled", "budget_tokens": 1600},
    messages=[{"role": "user", "content": "Create a haiku about Anthropic."}],
)

for block in response.content:
    if block.type == "thinking":
        print(f"Thinking: {block.thinking}")
    elif block.type == "text":
        print(f"Text: {block.text}")
