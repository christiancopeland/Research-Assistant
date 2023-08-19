# Research-Assistant
Connecting AI to Arxiv to generate literature reviews in bulk

## Create 3 directories
* embeddings/
* pdfs/
* errors/

# How to use?
* Run generate_embeddings.py to embed the arxiv metadata snapshot using sentence transformers. Stored in embeddings/
* Run weofi.py to upload the embeddings to a Qdrant Vector Database collection to be searched over from the search_server.py frontend
* Run search_server.py to spin up a simple Flask frontend where you can search for research papers and download them
* Once you've downloaded some papers you're interested in, copy them into the pdfs/ directory
* Run gen_literature_review.py and relax while you get a tailored report on every paper

