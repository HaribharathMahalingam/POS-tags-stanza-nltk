# Generate pos tags on pre-tokenized sentences using the Stanza tool and NLTK
This project deals with generating pos-tags on pre-tokenized sentences using the NLTK and Stanza tool. 

Step1: Import nltk and stanza

Step2: Get all sentences from brown corpus and convert to list type

Step3: Define any 3 genres from brown corpus. For this assignment, I have considered ["learned", "government", "reviews"] genres.

Step4: Define get_pos_from_stanza_output(output) function to convert Stanza output into a list of list of universal pos tags compatible with Brown corpus.

Step5: Define get_pos_from_nltk_tagged_sents(o) function to convert NLTK's tagged sentences into list of list of universal pos tags.

Step6: Define accuracy (gold, output) function to find the accuracy by counting matches between gold-standard list of list and the output.

Step7: Define convert_pos(Stanza_Tagset_Final) to convert universal pos tag from stanza to a compatible universal pos inn Brown corpus.

Step8: Define a for loop to loop through the whole code block of finding accuracy for all the three genres.

Step9: Get all sentences with their universal pos tags from a genre using nltk in sent_pos.

Step10: Pre-tokenize all the sentences in a list from the Brown corpus.

Step11: Get the final pos tag set using stanza in Stanza_Tagset_Final.

Step12: Get the final pos tag set using nltk in NLTK_Tagset_Final.

Step13: Compute all 3 accuracies using the accuracy() function with NLTK_Tagset_Final and Stanza_Tagset_Final.

![image](https://user-images.githubusercontent.com/54590466/142268064-cced62e9-410c-4bac-99a8-5e949c280340.png)

![image](https://user-images.githubusercontent.com/54590466/142268137-e483d520-acf3-4a61-96ef-e8df50d78ce2.png)
