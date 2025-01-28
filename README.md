# TruthCheck
## Theme: Misinformation Detection and Fact Checking on Social Media
## Idea: Adaptive Knowledge Graph and Multi-Model AI Framework for Misinformation Detection and Fact-Checking

### Problem Statement:
The widespread misinformation on networked platforms poses significant challenges to information integrity, public trust, and societal well-being. Current systems fail to effectively detect and verify misinformation in real time across text, images, videos, and deep fakes, while struggling with linguistic and cultural diversity. Additionally, issues like unreliable data sources, lack of transparency, and privacy concerns hinder their effectiveness. A progressive solution is needed to address misinformation proactively, ensuring accuracy, transparency, and compliance with privacy regulations.

### Video Demonstration:


### Methodology:
##### Knowledge Graph Construction: 
The knowledge graph will integrate credible data sources (e.g., Wikidata, Kaggle, scientific journals) through web scraping or APIs to continuously update verified information. Neo4j will be used for storing and querying nodes (e.g., people, events, organizations) and edges (relationships) in real-time.

##### Claim Detection: 
A hybrid ensemble of NLP models (BERT, RoBERTa, T5) will be used to detect and classify claims from social media streams and news articles. Text preprocessing, including tokenization, will clean the data, improving the accuracy and coverage of claim identification.

##### Semantic Matching and Verification: 
Named Entity Recognition (NER) will extract entities from claims, generating structured queries for verification using the knowledge graph. Semantic matching techniques, like Sentence-BERT and BiLSTM models, will be employed to verify claims, with aggregated results providing a credibility score based on entity match and source reliability.

##### Feedback to Users: 
Users will receive results about the truthfulness of claims (true, false, or unverifiable), with explanations derived from explainable AI techniques (e.g., SHAP, LIME) to clarify the model’s decision-making process.

##### Adaptation and Scalability: 
The system will incorporate dynamic web scraping and partnerships with fact-checking organizations to update the knowledge graph. Using deep learning models like mBERT, the system will support multiple languages and adapt to different linguistic and cultural contexts, ensuring scalability.

### Technology Used:
React.js, Tailwind CSS, Flask, Python, JavaScript

### How to execute locally:
-> Install Node.JS version 18.20.6 (LTS) to avoid any compatibility issue <br>
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
