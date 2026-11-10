import httpx
import xml.etree.ElementTree as ET

ARXIV_SEARCH_URL = "https://export.arxiv.org/api/query"

def search_arxiv(query: str, limit: int):
    search_parameters = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": limit
    }

    response = httpx.get(
        ARXIV_SEARCH_URL,
        params=search_parameters,
        timeout=15.0
    )

    response.raise_for_status()

    
  
    print(response.status_code)
    print(response.text[:500])

   # Define the XML namespaces used in the response
    namespaces = {
        "atom": "http://www.w3.org/2005/Atom",
    }
    
     # Parse the XML response and extract the paper title
    root = ET.fromstring(response.text) # parse the XML response
    entries = root.findall("atom:entry", namespaces) # find all entries in the XML response

    for entry in entries:
      
     # URL extraction
     id_element = entry.find("atom:id", namespaces)
     paper_url = None
    
     if id_element is not None and id_element.text:
        paper_url = id_element.text.strip()

     if not paper_url:
         continue
            
     print("Paper URL:", paper_url)

     # title extraction
     title_element = entry.find("atom:title", namespaces)
     title = "No title"
     
     if title_element is not None and title_element.text:
        cleaned_title = title_element.text.strip() 

        if cleaned_title:
          title = cleaned_title 
        
     print("Paper title:", title)
     
    # Author(s) extraction
     author_elements = entry.findall("atom:author", namespaces)
     authors = []

     for author in author_elements:
        name = None
        name_element = author.find("atom:name", namespaces)

        if name_element is not None and name_element.text:
            name = name_element.text.strip() #  change xml into string and strip whitespace from the author's name

        if name:       
             authors.append(name)

     if not authors:
         authors = ["Unknown"]

     print("Authors:", authors)

     # published date
     published_element = entry.find("atom:published", namespaces)
     published_date = None

     if published_element is not None and published_element.text:
        cleaned_date = published_element.text.strip()

        if cleaned_date:
           published_date = cleaned_date
           print("Published On:", published_date)
     else:
           print("No Date")
        
# search_arxiv("machine learning", 1)


test_xml = """
<feed xmlns="http://www.w3.org/2005/Atom">
    <entry>
        <id>https://arxiv.org/abs/1234.56789</id>
    </entry>
    <entry>
        <id>   </id>
    </entry>
     <entry>
       
  </entry>
    <entry>
        <id>https://arxiv.org/abs/9876.54321</id>
    </entry>

</feed>
"""

test_entry = ET.fromstring(test_xml) 

test_namespaces = {
    "atom": "http://www.w3.org/2005/Atom"
}

for entry in test_entry.findall("atom:entry", test_namespaces):
    paper_url = None
    id_element = entry.find("atom:id", test_namespaces)
    
    if id_element is not None and id_element.text:
        paper_url = id_element.text.strip()

    if not paper_url:
         continue
        
    print("Test Paper URL:", paper_url)
