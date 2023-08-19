# Research-Assistant
Connecting AI to Arxiv to generate literature reviews in bulk

## Create 3 directories
* embeddings/
* pdfs/
* errors/

# How to use?
* Run generate_embeddings.py to embed the arxiv metadata snapshot using sentence transformers. Stored in embeddings/
* Make sure you have a Qdrant instance up, I recommend pulling down qdrant/qdrant and running with ports that work for you so you can get started quickly.
* Run weofi.py to upload the embeddings to a Qdrant Vector Database collection to be searched over from the search_server.py frontend
* Run search_server.py to spin up a simple Flask frontend where you can search for research papers and download them
* Once you've downloaded some papers you're interested in, copy them into the pdfs/ directory
* Run gen_literature_review.py and relax while you get a tailored report on every paper

  Note: You can explain how you want the literature review to be made in prompt_summary.txt

