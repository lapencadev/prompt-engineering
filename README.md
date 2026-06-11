# PROMPT ENGINEERING 

In this project I am seeking to learn and practice about computational linguistics.

![Frontend Demo](demo.gif)

## 1. Environment and libraries
- spaCy
```powershell
python3 -m pip install spacy
```
- English linguistic model
```powershell
python3 -m pip install click && python3 -m spacy download en_core_web_sm
````

## 2. Linguistic Analysis Script
Creation of the [analyzer script](analyzer.py) to process text tokens, parts of speech (POS), morphology, and named entities (NER).

```python
# Execution command
python3 analyzer.py
```

### Output Result
Below is the execution output showing a full linguistic profile (including verbs, nouns, and entities like dates, people, places, and organizations):

```text
Tokens and their parts of speech:
---GRAMMAR AND MORPHOLOGY ANALYSIS---
Word: 'Yesterday      ' | Category: ADV       , Morphology details: 
Word: ',              ' | Category: PUNCT     , Morphology details: PunctType=Comm
Word: 'Alice          ' | Category: PROPN     , Morphology details: Number=Sing
Word: 'and            ' | Category: CCONJ     , Morphology details: 
Word: 'Bob            ' | Category: PROPN     , Morphology details: Number=Sing
Word: 'visited        ' | Category: VERB      , Morphology details: Tense=Past|VerbForm=Fin
Word: 'Paris          ' | Category: PROPN     , Morphology details: Number=Sing
Word: 'to             ' | Category: PART      , Morphology details: 
Word: 'buy            ' | Category: VERB      , Morphology details: VerbForm=Inf
Word: 'a              ' | Category: DET       , Morphology details: Definite=Ind|PronType=Art
Word: 'new            ' | Category: ADJ       , Morphology details: Degree=Pos
Word: 'smartphone     ' | Category: NOUN      , Morphology details: Number=Sing
Word: 'from           ' | Category: ADP       , Morphology details: 
Word: 'Apple          ' | Category: PROPN     , Morphology details: Number=Sing
Word: '.              ' | Category: PUNCT     , Morphology details: PunctType=Peri

---ENTITY ANALYSIS (NAMED ENTITY RECOGNITION)---
Entity: 'Yesterday      ' | Label: DATE
Entity: 'Alice          ' | Label: PERSON
Entity: 'Bob            ' | Label: PERSON
Entity: 'Paris          ' | Label: GPE
Entity: 'Apple          ' | Label: ORG
```

![Terminal Analysis Output](output1.png)

## 3. FastAPI Implementation
Exposing the computational linguistics engine through an HTTP REST API using FastAPI.

### Installation & Execution
```powershell
# Install dependencies
python3 -m pip install fastapi uvicorn

# Start the local server
python3 -m uvicorn main:app --reload
```

### API Interactive Documentation
Once the server is running, navigate to:
* **Interactive UI (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Alternative Docs (ReDoc):** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoint Analysis (`POST /analyze`)
The API handles automated text analysis via data payloads. Sending a direct browser URL request triggers a `405 Method Not Allowed` because it requires a `POST` method with a proper JSON body.

#### Sample Request Body
```json
{
  "text": "Yesterday, Alice and Bob visited Paris to buy a new smartphone from Apple."
}
```

#### Sample Response Body
```json
{
  "text": "Yesterday, Alice and Bob visited Paris to buy a new smartphone from Apple.",
  "tokens": [
    {
      "word": "Yesterday",
      "category": "NOUN",
      "morphology": "Number=Sing"
    },
    {
      "word": ",",
      "category": "PUNCT",
      "morphology": "PunctType=Comm"
    },
    {
      "word": "Alice",
      "category": "PROPN",
      "morphology": "Number=Sing"
    },
    {
      "word": "and",
      "category": "CCONJ",
      "morphology": "ConjType=Cmp"
    },
    {
      "word": "Bob",
      "category": "PROPN",
      "morphology": "Number=Sing"
    },
    {
      "word": "visited",
      "category": "VERB",
      "morphology": "Tense=Past|VerbForm=Fin"
    },
    {
      "word": "Paris",
      "category": "PROPN",
      "morphology": "Number=Sing"
    },
    {
      "word": "to",
      "category": "PART",
      "morphology": "None"
    },
    {
      "word": "buy",
      "category": "VERB",
      "morphology": "VerbForm=Inf"
    },
    {
      "word": "a",
      "category": "DET",
      "morphology": "Definite=Ind|PronType=Art"
    },
    {
      "word": "new",
      "category": "ADJ",
      "morphology": "Degree=Pos"
    },
    {
      "word": "smartphone",
      "category": "NOUN",
      "morphology": "Number=Sing"
    },
    {
      "word": "from",
      "category": "ADP",
      "morphology": "None"
    },
    {
      "word": "Apple",
      "category": "PROPN",
      "morphology": "Number=Sing"
    },
    {
      "word": ".",
      "category": "PUNCT",
      "morphology": "PunctType=Peri"
    }
  ],
  "entities": [
    {
      "entity": "Yesterday",
      "type": "DATE"
    },
    {
      "entity": "Alice",
      "type": "PERSON"
    },
    {
      "entity": "Bob",
      "type": "PERSON"
    },
    {
      "entity": "Paris",
      "type": "GPE"
    },
    {
      "entity": "Apple",
      "type": "ORG"
    }
  ]
}
```

![FastAPI Interactive Documentation](output2.png)

## 4. Web Frontend

An interactive [`index.html`](index.html) connects the FastAPI backend to a browser UI — no page reloads, no framework dependencies.

### How to run

```powershell
# Start the server (serves both the API and the UI)
python3 -m uvicorn main:app --reload
```

Then open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.

> **Note:** Opening `index.html` directly as a local file (`file://`) will fail — the browser blocks cross-origin requests from the filesystem. Always access the UI through the FastAPI server URL above.

### Features
- **Text input** — large textarea with `Cmd/Ctrl + Enter` shortcut to submit.
- **Grammar & Morphology panel** — each token rendered as a colored badge showing the word, POS category, and morphological features (tense, number, case…).
- **Named Entity panel** — pill badges color-coded by entity type (PERSON, GPE, ORG, DATE, LOC…).
- **Error handling** — clear message if the API server is not reachable.

### POS color legend
| Color | Categories |
|-------|-----------|
| Blue | NOUN |
| Purple | PROPN (proper noun) |
| Green | VERB |
| Yellow | ADJ |
| Pink | ADV |
| Orange | ADP (preposition) |
| Teal | DET |
| Cyan | CCONJ / SCONJ |
| Gray | PUNCT / other |

### Sample sentences to test

Try these to cover a wide range of POS tags and entity types:

```
Yesterday, Alice and Bob visited Paris to buy a new smartphone from Apple.
```
> Covers: DATE, PERSON ×2, GPE, ORG — the classic baseline.

```
Elon Musk announced that Tesla will launch a new electric vehicle in Berlin next Monday.
```
> Covers: PERSON, ORG ×2, GPE, DATE — good for multi-entity sentences.

```
The quick brown fox jumps over the lazy dog.
```
> Covers: ADJ ×3, NOUN ×2, VERB — no entities, pure grammar/morphology check.

```
She quickly ran to the nearest hospital after the accident on Fifth Avenue.
```
> Covers: PRON, ADV, VERB, LOC — tests location entities and adverbs.

```
In 1969, NASA sent Neil Armstrong to the Moon during the Apollo 11 mission.
```
> Covers: DATE, ORG, PERSON, LOC, EVENT — rich entity mix.

```
The European Central Bank raised interest rates by 0.5% on Thursday.
```
> Covers: ORG, MONEY/PERCENT, DATE — financial/economic domain.