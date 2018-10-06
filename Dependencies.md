# Dependencies 

Before running the scripts presented in this repository, make sure you have downloaded and set paths to some variables. 

## NLTK

Scripts that verify the co-occurrence between terms use [Natural Language Toolkit](https://www.nltk.org/) (NLTK) to wrapper tokenizer, tagger and parser. 
Scripts are tested with NLTK version 3.3.

```
$ sudo pip install nltk
```



## Stanford CoreNLP

Some scripts depend on [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) software. 
Scripts are tested using the stanford-corenlp-full-2018-02-27.zip version.

```
$ wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
$ unzip stanford-corenlp-full-2018-02-27.zip
```

After downloading it, you have to edit *settings.conf* setting the path of the "stanford-corenlp-full-2018-02-27" folder to *PARSER* and of the "stanford-corenlp-3.9.1.jar" file to *SNLP_TAGGER_JAR*.

In case of setting SERVER=yes in *settings.conf*, you should keep Stanford CoreNLP running in a separated terminal by typing:

```
$ java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,parse,depparse -status_port 9000 -port 9000 -timeout 15000 
```

The wrapper in NLTK of CoreNLP also use *requests* library, which you can install as

```
$ sudo pip install requests
```



