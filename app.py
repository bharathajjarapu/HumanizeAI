import streamlit as st
from dotenv import load_dotenv
from microagent import Microagent, Agent

load_dotenv()
client = Microagent(llm_type='groq')

def detectai(text):
    agent = Agent(
        name="Detector",
        instructions="Classify the input as 'AI-generated' or 'Human-written'.",
        model="llama3-groq-70b-8192-tool-use-preview"
    )
    response = client.run(
        agent=agent,
        messages=[{"role": "user", "content": text}],
    )
    return response.messages[-1]["content"].strip() == "AI-generated"

def rephrase(text):
    agent = Agent(
        name="Rephraser",
        instructions="Rephrase the input to make it indistinguishable from human-written text.",
        model="llama3-groq-70b-8192-tool-use-preview"
    )
    response = client.run(
        agent=agent,
        messages=[{"role": "user", "content": text}],
    )
    return response.messages[-1]["content"].strip()

def validate(text):
    agent = Agent(
        name="Validator",
        instructions="Re-check the input and classify it as 'AI-generated' or 'Human-written'.",
        model="llama3-groq-70b-8192-tool-use-preview"
    )
    response = client.run(
        agent=agent,
        messages=[{"role": "user", "content": text}],
    )
    return response.messages[-1]["content"].strip() == "Human-written"

def main():
    st.title("AI Text Humanizer")
    input_text = st.text_area("Enter text to humanize:")
    if st.button("Humanize Text"):
        if detectai(input_text):
            rephrased = rephrase(input_text)
            if validate(rephrased):
                st.markdown("### Humanized Text")
                st.write(rephrased)
            else:
                st.error("Failed to humanize the text. Try again.")
        else:
            st.success("The text is already human-written.")

if __name__ == "__main__":
    main()