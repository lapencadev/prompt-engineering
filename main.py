from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import spacy

# Load the English language model
app = FastAPI(
    title="Linguistic Analysis API",
    description="An API that performs linguistic analysis on English text using spaCy.",
    version="1.0.0"
)
nlp = spacy.load("en_core_web_sm")

# Allow CORS for testing purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for the input data
class TextInput(BaseModel):
    text: str

# Endpoints
@app.get("/")
def home():
    return {"message": "Welcome to the Linguistic Analysis API! Use the /analyze endpoint to analyze your text."}

@app.post("/analyze") 
def analyze_text(input: TextInput):
    # Validate empty input
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    # Process the text
    doc = nlp(input.text)

    # Grammar and Morphology Analysis
    tokens_analysis = []
    for token in doc:
        tokens_analysis.append({
            "word": token.text,
            "category": token.pos_,
            "morphology": str(token.morph) if token.morph else "None"
        })
    
    # Entity Analysis (Named Entity Recognition)
    entities_analysis = []
    for ent in doc.ents:
        entities_analysis.append({
            "entity": ent.text,
            "type": ent.label_
        })
    
    # Return the analysis results
    return {
        "text": input.text,
        "tokens": tokens_analysis,
        "entities": entities_analysis
    }