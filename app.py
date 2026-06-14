from flask import Flask, render_template, request
import spacy
import networkx as nx
from pyvis.network import Network

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

relationships = []

def extract_relationships(text):
    doc = nlp(text)
    rels = []

    for sent in doc.sents:
        entities = list(sent.ents)

        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                rels.append({
                    "source": entities[i].text,
                    "target": entities[j].text,
                    "relationship": "related_to",
                    "sentence": sent.text
                })

    return rels

def build_graph(rels):
    G = nx.Graph()

    for rel in rels:
        G.add_node(rel["source"])
        G.add_node(rel["target"])
        G.add_edge(rel["source"], rel["target"], title=rel["sentence"])

    net = Network(height="600px", width="100%", bgcolor="#111827", font_color="white")
    net.from_nx(G)
    net.save_graph("static/graph.html")

def answer_question(question, rels):
    question = question.lower()

    matches = []

    for rel in rels:
        if rel["source"].lower() in question or rel["target"].lower() in question:
            matches.append(rel)

    if matches:
        return matches

    return "No direct relationship found."

@app.route("/", methods=["GET", "POST"])
def index():
    global relationships

    answer = None
    graph_ready = False

    if request.method == "POST":
        text = request.form.get("document_text")
        question = request.form.get("question")

        if text:
            relationships = extract_relationships(text)
            build_graph(relationships)
            graph_ready = True

        if question:
            answer = answer_question(question, relationships)
            graph_ready = True

    return render_template(
        "index.html",
        relationships=relationships,
        answer=answer,
        graph_ready=graph_ready
    )

if __name__ == "__main__":
    app.run()