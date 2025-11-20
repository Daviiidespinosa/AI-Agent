from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

# Guardar archivo
def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"--- Resultado de la Investigación ---\nFecha: {timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return f"Archivo guardado en {filename}"

save_tool = Tool(
    name="save_file",
    func=save_to_txt,
    description="Guarda información en un archivo de texto."
)

# DuckDuckGo
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="web_search",
    func=search.run,
    description="Busca información en la web con DuckDuckGo."
)

# Wikipedia
wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=600)

wiki_tool = Tool(
    name="wikipedia",
    func=lambda q: wiki.run(q),
    description="Busca contenido en Wikipedia."
)
