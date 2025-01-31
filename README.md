# TruthCheck
## Theme: Misinformation Detection and Fact Checking on Social Media
## Idea: Adaptive Knowledge Graph and Multi-Model AI Framework for Misinformation Detection and Fact-Checking

### Problem Statement:
The sheer volume of misinformation on networked platforms has created serious threats to information integrity, public trust, and ultimately public health and society. Text, images, videos, deep fakes, and a lack of linguistic and sociocultural diversity all contribute to current systems’ inability to detect and verify misinformation effectively in real time. Moreover, the absent transparency, unreliable data sources, and privacy concerns plagued their operation. Misinformation is still a pervasive issue; we need a progressive solution that can proactively combat false information while maintaining accuracy, transparency, and privacy compliance.

### Video Demonstration: https://www.youtube.com/watch?v=GhO7RPcDxIM


### Methodology:
##### Knowledge Graph Construction: 
Using web scraping or APIs, the knowledge graph is going to link trustworthy data sources (such as Wikidata, Kaggle, scientific journals) into consistent data streams that are going to help keep the verified information up to date. For fast real-time storage and query of nodes (people, events, organizations) and edges (relationships), we will use Neo4j.

##### Claim Detection: 
Hybrid ensemble NLP approach(BERT, RoBERTa, T5) and subsequent combination into a hybrid architecture for Identifying & classifying Claims from Social media streams and news articles. To make the data clean and, thus, increase the precision and the recall of claims detection, pre-treating the text like tokenization would work.

##### Semantic Matching and Verification: 
Knowledge Graph Component can be used for feeding claims into our Named Entity Recognition (NER) which can help us extract the entities from the input claims and generates structured queries we can use to verify information with the knowledge graph. Semantic matching techniques, especially, Sentence-BERT and BiLSTM models, will be used to validate the claims, followed by aggregating the results per entity match and source reliability to attain a credibility score.

##### Feedback to Users: 
Indicates of claims (true, false or unverifiable) will be shown to users with explanations using explainable AI techniques (e.g. SHAP, LIME) to help understand the model.

##### Adaptation and Scalability: 
Dynamic web scraping and partnerships with fact-checking entities will ensure the knowledge graph is updated. The utilization of a multi-generational pre-trained language model such as mBERT ensures that the system will be multi-lingual and adaptable to various linguistic and cultural contexts and patterns, guaranteeing scalability.

### Technology Used:
React.js, Tailwind CSS, Flask, Python, JavaScript, GenAI

### How to execute locally:
-> Install Node.JS version 18.20.6 (LTS) to avoid any version incompatibility issue <br>
-> Generate Gemini API Key and place the key .env file in backend folder <br>
-> Open terminal <br>
-> Spilt the terminal <br>
-> In one part of the terminal go to Backend folder 
```
cd Backend
```
-> Run the command, to install all libraries
```
pip install -r requirements.txt
```
-> Start the backend server
```
python run.py
```
-> I another part of terminal go to Frontend folder
```
cd Frontend
```
-> Run the command, to install all dependencies
```
npm install
```
-> Start the frontend server
```
npm run start
```
-> In the localhost frontend server the website will be executed
