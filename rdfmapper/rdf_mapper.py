
from rdflib import Graph, URIRef, Literal, Namespace

def generate_rdf(data, namespace_uri="http://example.org/"):
    ns = Namespace(namespace_uri)
    g = Graph()
    
    for idx, item in enumerate(data):
        subject = URIRef(f"{ns}item{idx}")
        for key, value in item.items():
            g.add((subject, ns[key], Literal(value)))

    return g.serialize(format="turtle")
