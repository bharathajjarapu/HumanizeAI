# HumanizeAI
Humanize AI Text using AI Agents

HumanizeAI is a Python-based program designed to detect AI-generated text, rephrase it to make it indistinguishable from human-written text, and validate the results. The tool leverages multiple agents to ensure the rephrased text passes AI detection and appears authentically human-written.

---

## Features
1. **AI Detection:** Identifies whether the input text is AI-generated.
2. **Rephrasing:** Rewrites AI-generated text while preserving the original meaning and key information.
3. **Validation:** Confirms that the rephrased text passes AI detection and is classified as human-written.
4. **Future-ready:** Built to integrate additional agents for enhanced AI detection or iterative checks.

---

## How It Works
The application uses the following **agents** powered by the `microagent` library:

1. **Detector Agent:**
   - Role: Identifies if the input text is AI-generated.
   - Output: Classifies text as either "AI-generated" or "Human-written."

2. **Rephraser Agent:**
   - Role: Rephrases the detected AI-generated text to make it appear human-written.
   - Process:
     - Retains key information and the original intent of the text.
     - Ensures the rephrased version avoids detection as AI-generated.

3. **Validator Agent:**
   - Role: Rechecks the rephrased text to confirm it is classified as "Human-written."
   - Ensures robustness by validating the output.

4. **Future Plans:**
   - Introduce an **API Agent** to call external AI detection APIs.
   - Implement iterative checks for further refinement.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bharathajjarapu/HumanizeAI.git
   cd HumanizeAI
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file:
   - Add your API keys or environment-specific settings required for `microagent`.

---

## Usage
1. Run the program:
   ```bash
   streamlit run app.py
   ```

2. Enter the text you want to analyze when prompted.

3. Follow the workflow:
   - If the text is detected as **AI-generated**, it will be rephrased.
   - The rephrased text will then be validated.
   - If successful, the humanized text will be displayed.

---

## Example Workflow
### Input
```
The weather today is sunny with a high of 75°F. AI systems are revolutionizing how we perceive daily forecasts.
```

### Output
If detected as AI-generated, the rephrased output might look like:
```
Today’s weather will be sunny with temperatures reaching 75°F. Innovations in AI are transforming how we interpret daily weather updates.
```

---

## Future Development
### Planned Features
- **API Agent:** 
  - Integrate external AI detection APIs for additional verification.
  - Iterate the detection-rephrase-validate process to ensure robustness.
- **Enhanced Rephrasing:** 
  - Incorporate more nuanced adjustments for domain-specific text.
- **Logging:** 
  - Add detailed logs for better debugging and transparency.

---

## Contributions
We welcome contributions! Here’s how you can help:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature
   ```
3. Submit a pull request with a detailed explanation of your changes.

---

## License
This project is licensed under the [MIT License](LICENSE).
