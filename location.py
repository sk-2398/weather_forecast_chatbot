import locationtagger
import nltk

nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')
import spacy

def extract_location(text):
    input_text=text.title()
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)

    locations = []
    for ent in doc.ents:
        if ent.label_ == "GPE":  # GPE represents geopolitical entity (locations)
            locations.append(ent.text)
    
    if len(locations) < 1:
        place_entity = locationtagger.find_locations(text=input_text)
        if place_entity.cities:
            loc=' '.join(place_entity.cities)
            locations.append(loc)
        elif place_entity.countries:
            loc=' '.join(place_entity.countries)
            locations.append(loc)
        elif place_entity.regions:
                loc=' '.join(place_entity.regions)
                locations.append(loc)
    
 
    location=' '.join(locations)

    return location
