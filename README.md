# MSS

A repository for transcriptions of hand-written texts of various kinds 
(full or partial codices, letters, administrative documents, inscriptions).

## URI structure

Each object has a human-readable and machine-parsable URI.

The URI consists of 3 components:
1. Location ID: identifier for the institution/collection the object is located
2. Manuscript ID: identifier for the object. If an object contains more than one text,
    it is possible to make more than one URI for the object (see below)
3. Transcription ID: identifier for the transcription of the text in/on the object. 
    It is possible to have more than one transcription of the same object (e.g.,
    by different transcribers, or a diplomatic and normalized transcription)

Note that the transcription ID must be unique to a specific transcription!

### Components:  

#### 1. Location ID: f"MS{country_code}{city}{institution}"  
* prefix "MS" to clearly differentiate manuscript corpus URIs from main corpus URIs  
* country_code: [Country dialing code](https://en.wikipedia.org/wiki/List_of_telephone_country_codes#World_numbering_zones). Use "0000" if the country is unknown.
* city:   
  * in English if name exists, otherwise transcription  
  * only Latin-script letters a-z and A-Z  
  * Munich, Vienna, Prague, Cairo, Zurich, Gottingen, …  
* institution:   
  * Use commonly used abbreviation if it exists (BL, Bnf, SBB, …);  
  * otherwise: create abbreviation with Latin-script letters a-z and A-Z  
  * Full name of the institution should go into the YML file (in English and if possible Arabic-script transcription)  
* Regex: r"MSd{4}[A-Za-z]+"  
* Examples:   
  * MS0044LondonBL  
  * MS0047OsloSchoeyen  
  * MS0000Unknown  
#### 2. Manuscript ID: f"{collection?}{shelfmark}{part?}"  
* Use only Latin-script letters a-z and A-Z; transcribe using [transcription tables](https://docs.google.com/spreadsheets/d/1ROWI7W4UCG4H6AzyE1USx4qpCNdQN9QsZ-qAmYpKVpg/edit?usp=sharing)  
* collection: name of the collection within the institution (if applicable)
* shelfmark:  
  * Omit abbreviations like Ms./Hs./Cod./No. (to keep the URIs short)  
  * Omit all non-alphanumeric characters in the shelfmark; replace any non-alphanumeric characters that serve to divide two numbers with underscore 
  * Use capitalization to distinguish between words
  * Full human-readable shelfmark should go into the YML file!  
* part (optional): multi-text manuscripts / objects can be split into different parts during the annotation process:  
  * Infix: **P**  
  * Manuscripts: 
    * start page/folio of the part (use A for recto, B for verso): P120, P80A, P30B  
      ![recto-verso][https://en.wikipedia.org/wiki/File:Recto_and_verso_RTL.svg]
    * If necessary (e.g., when two texts start on the same page), add the line number where the part starts after A/B (P80A1, P80A12) or number the parts sequentially (P80A1, P80A2)
  * Other types of objects: number the different parts (P1, P2, …)  
* Regex: r"[A-Za-z0-9_]+"  
* Examples (only the bold part of the URI is the manuscript ID):   
  * MS0044LondonBL.**Or8212_166**  
  * MS0047OsloSchoeyen.**4580**  
  * MS0049MunichBSB.**Arab230P040B** : the part of the manuscript that starts at folio 40 verso  
  * MS0049MunichBSB.**Arab230P082A** : the part of the manuscript that starts at folio 82 recto  

#### 3. Transcription ID: f"{contributor}{number}{margin?}-{language}{transcr_type}"
* contributor: abbreviation/initials of transcriber/contributor/project  
* number: 
  * Either internal ID number of the contributing project;  
  * Or running numbers like 001, 002, …  
  * Or timestamp: YYYYMMDD(HHMMSS)  
  * Or a combination: YYYYMMDD001, YYYYMMDD002, …  
* Margin (optional): marginal texts can be split off into separate files:  
  * Infix: **Mar**  
  * By default, all marginal text in a document is in one text file.  
  * Full text in the margin of another text (e.g., sharḥ): use the page number of the start page of the marginal text in the manuscript ID in combination with the Mar infix: e.g., MS0049MunichBSB.Arab230**P040B**.PV202501027**Mar**-ara1: The marginal text in this manuscript that starts at folio 40 (verso)  
* language(s):   
  * Language code(s) for the language(s) (+scripts) of the text
    * Language codes are based on [iso639-3](https://iso639-3.sil.org/code_tables/639/data). However, we created additional codes for languages written in different scripts (e.g., 'jua' for "Judaeo-Arabic", Arabic written in Hebrew script). All language codes used in the OpenITI corpus are listed in the [annotation repo](https://github.com/OpenITI/Annotation/blob/master/language_codes.tsv). 
    * For multilingual texts: combine language codes for each language (-ara1per1)  
* transcr_type:  
  * 1: undefined transcription type  
  * 2: normalized transcription  
  * 3: diplomatic transcription  
* Regex: r"[A-Za-z0-9]+-(?:[a-z]{3}[0-9])+"  
* Examples (only the bold part of the URI is the manuscript ID):   
  * MS0001NewYorkNYPL.SpencerPersian9.**LMN20250402001-per1**  
  * MS0044LondonBL.EAP1285_1_12_2.**PV20250402001-ara2** ([url](https://eap.bl.uk/collection/EAP1285-1-12-2))  
  * MS0049BerlinSBB.Landberg2_71.**AOCP20250402001-ara3per1**  
  * MS0047OsloSchoeyen.4580.**IEDC0009-bac1**  
  * MS0001NewYorkNYPL.SpencerPersian9.**LMN20250402001Mar-per1**: all marginal texts in this document  
  * MS0049MunichBSB.Arab230P040B.**PV202501027Mar-ara1**: the marginal text in this manuscript that starts at folio 40 (verso)  
 4. **File extension:** (as in the main OpenITI corpus) :  
* (no extension) : automatically converted into OpenITI mARkdown  
* .completed : structural annotation manually added  
* .mARkdown : second person has vetted the structural annotation

### Edge cases:  
1. Unknown city, known institution: MS0000UnknownMosque  
2. Unknown city, unknown institution: MS0000Unknown  
3. city known, Unknown institution: MS0049BerlinUnknown.456231  
4. Unknown shelfmark “NN” + random number: MS0049BerlinSBB.NN123456789  

## FAQ:  

###  1. What if there is more than one shelf mark?   

Use only one shelfmark in the URI. List all shelf marks in the metadata file  

### 2. What if the digital file is in one collection, and the physical document in another one?  

Use the shelfmark of the collection where we got the images from (manuscript, microfilm or digitization). write all shelfmarks in the yml file

### 3. What if the manuscript contains multiple texts (e.g., majmūʿa manuscript, stone with multiple inscriptions)? 

* During ingestion process: 
  * a single file for each physical object (unless the source library already divides the file up into parts, of course)  
  * If metadata specifies the authors + titles of the different parts: add information about the parts in the yml file (with page/folio numbers if known)
* During the structural annotation process:  
  * Split the text file into parts, each with their own URI. Use start page/folio of each part as modifier (use A/B for Recto/Verso):   
    * MS0049MunichBSB.Arab230**P040B** : the part of the manuscript that starts at folio 40 verso  
    * MS0049MunichBSB.Arab230**P082A** : the part of the manuscript that starts at folio 82 recto  

### 4. What if you only transcribed part of a manuscript?   

* Ideally, we have a full HTR transcription of the entire manuscript and a manually transcribed part of the manuscript;
* If only the transcribed manuscript is available, so be it  

### 5. How do we avoid having multiple location IDs for the same city/collection?  
Please check existing the list of existing location IDs in this repo before coining a new one.

### 6. How do we make sure the third part of the URI is unique?

### 7. What do we do with marginal text?  

* On ingestion: Inside the same file:  
  * Page always starts with main region  
  * `### |MARGIN|` marks the start of marginal text  
  * Insert multiple `### |MARGIN|` tags if there are multiple segments in the margin  
  * Use paragraph (`#`) and line (`~~`) markers as in normal text  
  * During/after annotation process: split the marginal text into a separate file:  
    * MS0001NewYorkNYPL.SpencerPersian9.LMN20250402001**Mar**-per1: all marginal texts in this document  
    * MS0049MunichBSB.Arab230**P040B**.PV202501027**Mar**-ara1: The marginal text in this manuscript that starts at folio 40 (verso)

## Metadata files

NB: some remarks about specifications in the YML files:

- Specification fields in YML keys:  
  - Language codes (e.g., 10#LOC#CITY#**AR**###): add a key, replacing the 2-letter language code ([ISO 639.1](https://www.loc.gov/standards/iso639-2/php/code_list.php)) if relevant. Language codes help conversion of the transcriptions in these YML fields into original scripts.  
  - Era (e.g., 30#MS#DATE#**AH**####:): add a key, replacing the 2-letter era code, if necessary ("CE" for Common Era, "SH" for Solar Hijri, "YE" for Yazdgerd Era, "AM" for Jewish Anno Mundi calendar)  
  - Measurements (e.g., 40#MS#HEIGHT#**MM**##:): replace the 2-letter measurement code if necessary ("MM" for milimeter, "CM" for centimeter, "IN" for inches)  
- page :   
  - foliated ms.: use folio numbers as written on the page:  
    FolioV01P001A (recto), FolioV01P010B (verso)   
  - Non-foliated ms.: use PDF page numbers:  
    - single-page images: PageV01P001, PageV01P020  
    - double page spread images: PageV01P001A (right page in image), PageV01P001B (left page in image)  
- page_range :  
  - foliated pages: 1A-20B  
  - page numbers: 1-42

### Location yml:

```
00#LOC#URI#######: 
10#LOC#CITY#AR###: name of the city, in Arabic [one-to-one transcription]
10#LOC#CITY#EN###: name of the city, in English
10#LOC#INST#AR###: name of the institution, in Arabic [one-to-one transcription]
10#LOC#INST#EN###: name of the institution, in English
70#LOC#EXTID#####: wikidata@id, src@id
80#LOC#CATALOGS##: permalink, permalink, permalink [worldcat or other]
80#LOC#LINKS#####: WEBSITE@permalink, CATALOGUE@permalink, permalink
90#LOC#COMMENT###: a free running comment here; you can add as many
    lines as you see fit; the main goal of this comment section is to have a
    place to record valuable information, which is difficult to formalize
    into the above given categories.
```

### Manuscript yml:

```
00#MS#URI########: 
10#MS#SHELFM#####: shelfmark; shelfmark 
    [in one-to-one transcription]
10#MS#GENRES#####: src@keyword, src@keyword, src@keyword
10#MS#AUTHOR#AR##: author(s) on the front page and/or of parts
    [in one-to-one transcription; replace language code if needed;
    semicolon-separated]
10#MS#TITLE#AR###: title(s) on the front page and/or of parts
    [in one-to-one transcription; replace language code if needed;
    semicolon-separated]
30#MS#DATE#AH####: date of copy in hijri era: DD-MM-YYYY, 
    DD-MM-YYYY@page, DD-MM-YYYY@page_range
30#MS#PLACE######: place of copy: place, URI@page
30#MS#PERSONS####: COPYIST@URI, AUTHOR@URI, PATRON@URI, READER@URI
30#MS#INSTITUT###: institutions mentioned
30#MS#SCRIPT#####: Maghribi/Naskh/Nastacliq/Hebrew/...
40#MS#INCIPIT####: first 5 lines (max.) of transcription
40#MS#EXPLICIT###: last 5 lines (max.) of transcription
40#MS#COLOPHON###: transcription of colophon
40#MS#HEIGHT#MM##: height, in mm (if needed replace MM by CM/IN/...)
40#MS#WIDTH#MM###: width, in mm (if needed replace MM by CM/IN/...)
40#MS#INK########: color, color
40#MS#LINESPP####: lines per page: n, n@page_range
40#MS#BINDING####: description of the binding
40#MS#STAMPS#####: seals and stamps: URI@page
40#MS#HANDS######: description of the different hands in the ms.
40#MS#DECO#######: description of the decorations in the ms.
40#MS#COLUMNS####: number of columns in the manuscript: n, n@page_range
40#MS#PARTS######: URI@page_range, URI@page_range
40#MS#VOLS#######: X of Y
70#MS#EXTID######: wikidata@id, src@id
80#MS#LINKS######: SOURCE@permalink, IIIF@permalink, PDF@permalink, 
    IMAGES@permalink, BIBTEX@permalink
80#MS#CATREF#####: reference to a manuscript catalogue 
90#MS#COMMENT####: a free running comment here; you can add as many
    lines as you see fit; the main goal of this comment section is 
    to have a place to record valuable information, which is 
    difficult to formalize into the above given categories.
90#MS#ISSUES#####: comma-separated list of issues:
    INCORRECT_FOLIO_ORDER, CORRECTED_FOLIO_ORDER,
    NO_FOLIO_NUMBERS, INCOMPLETE, FRAGMENT
```

* Transcription yml:

```
00#TRNS#CLENGTH##: number of characters
00#TRNS#LENGTH###: number of tokens
00#TRNS#URI######: 
40#TRNS#PAGES####: pages transcribed: page_range
80#TRNS#BASED####: permalink, permalink, permalink
80#TRNS#LINKS####: SOURCE@permalink, IIIF@permalink, PDF@permalink, 
    BIBTEX@permalink
80#TRNS#LINMODEL#: segmentation model used for line segmentation
    (name and/or URL)
80#TRNS#RECMODEL#: recognition model used for transcription
    (name and/or URL)
80#TRNS#REGMODEL#: segmentation model used for region segmentation
    (name and/or URL)
90#TRNS#CONTRIB##: TRANSCRIPTION@name, CORRECTION@name
   (latin characters; please use consistently)
90#TRNS#COMMENT##: a free running comment here; you can add as many
    lines as you see fit; the main goal of this comment section is to have a
    place to record valuable information, which is difficult to formalize
    into the above given categories.
90#TRNS#DATE#####: YYYY-MM-DD
90#TRNS#ISSUES###: comma-separated list of issues: UNCORRECTED_OCR, 
    TRANSCRIPTION_ERRORS, INCOMPLETE_TRANSCRIPTION
```

## Markdown issues:

* Reference to the image file names at the top of the page:  
  ![page image](./0620ZahiriSamarqandi.SindbadNama_0014.png)  
* Column marker? 

# Miscellaneous problems

* Double pages  
* Where on a page does a page start/end?   
* How do we indicate letter without dots even if we know what the dots should be?   
  * Prefix character to show that the next letter does not have dots (even though it’s transcribed with a dotted letter)?
