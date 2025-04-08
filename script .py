Vocabulary Module:

Description: Contains predefined vocabulary lists for different domains (engineering, creative [general and sci‑fi], others).

Pending: I plan to import an external database later to replace the hardcoding; the external source is still pending.

Function: generate_idea(domain, subdomain, combo_type, count):

Description: Randomly selects words from the appropriate vocabulary lists based on the user’s domain choice and combination type (adj+noun or noun+noun), then returns a list of generated inspiration phrases.

Function: view_explanation(term):

Description: Retrieves a detailed explanation for niche terms from a predefined dictionary.

Main Function (main):

Description: Serves as the user interface by prompting for input (domain, subdomain, combination type, phrase count), invoking generate_idea, and displaying the output. It also offers an option to view explanations for specific terms.
