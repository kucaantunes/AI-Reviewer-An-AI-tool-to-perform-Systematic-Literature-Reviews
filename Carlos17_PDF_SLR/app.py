import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

# Set up for file upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if file type is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load the model and tokenizer
MODEL_NAME = "facebook/bart-large-cnn"  # BART model for text generation
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Use the pipeline for question answering
generator = pipeline('summarization', model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the research question from the form
    question = request.form.get('question')
    pdf_text = request.form.get('pdf_text')
    uploaded_file = request.files.get('file')

    # Check if both question and pdf_text are provided
    if not question or not (pdf_text or uploaded_file):
        return jsonify({"error": "Both question and PDF text are required"}), 400

    # If a file is uploaded, read the text from the PDF
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(filepath)

        # For simplicity, simulate PDF-to-text extraction here
        # Implement PDF-to-text extraction based on your preferred library (e.g., PyMuPDF or pdfplumber)
        pdf_text = "Extracted text from PDF will appear here."  # Simulated extraction

    # Generate answer based on the text
    answer = generate_answer(pdf_text, question)

    # Render result page with the answer
    return render_template('result.html', question=question, answer=answer)

def generate_answer(pdf_text, question):
    # Preprocess the input for generation
    input_text = f"Research Question: {question}\n\nContext: {pdf_text}"

    # Tokenize the input text
    inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=1024)

    # Generate the answer (ensure it's long enough)
    outputs = model.generate(inputs, max_length=600, min_length=200, max_new_tokens=200, num_beams=4, length_penalty=2.0, early_stopping=True)

    # Decode the generated output and return the answer
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Ensure the answer is broken into paragraphs for readability
    paragraphs = answer.split("\n")
    formatted_answer = "\n\n".join(paragraphs)  # Ensure the answer has paragraph breaks
    return formatted_answer

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3007)
