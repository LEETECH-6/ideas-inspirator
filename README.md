# ideas-inspirator
This project is an ideas generator designed to provide users with randomly generated diverse phrases from a database. (usually random, because one of the essence of creating is combination between 2 things)Users can choose from different fields, such as engineering, creation, or others, each containing a specially designed vocabulary library. These combination of words may inspire people as a guideline in brainstorming. But the 1st version is more creative content related. For the creative field, users can further choose between general creative or fictional, for example, the science fiction section collects niche science fiction concepts. When niche concepts are included in the generated phrases, users can view dedicated explanatory notes to understand the detailed meaning and context of those concepts. Users can also choose the combination (such as adjective + noun or noun + noun) and the number of phrases generated to get the inspiration they need.

FEATURES:
generate_idea(domain, subdomain, combo_type, count):
A database 
According to the domain, subcategory, combination method and number of generated words selected by the user, the words are randomly selected from the preset vocabulary, combined into creative phrases and returned to the phrase list.
main():
Responsible for receiving user input (domain, subclass, combination method and number of generates), calling generate_idea() and output the generated inspiration phrase; Also provide links or descriptions for phrases that contain niche concepts so that users can see detailed explanations.
Vocabulary module:
Predefined vocabulary for multiple fields, grouped by engineering, creation (including science fiction and general creation), and others (animals, plants, food, etc.), supporting random combinations to generate creative phrases.
