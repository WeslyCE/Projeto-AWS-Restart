from flask import Flask, render_template

app = Flask(__name__)

# Lista de integrantes
integrantes = [
    {
        "nome": "Adriana Gutierrez", 
        "slug": "adriana-gutierrez", 
        "descricao": "Desenvolvedora 40+ apaixonada por tecnologia e inovação.",
        "detalhada": "Experiência de 9 meses como front-end Jr",
        "objetivo": "Em busca de uma função de nível inicial no setor da nuvem.",
        "softskills": ["Trabalho em equipe", "Comunicação", "Proatividade", "Aprendizado contínuo"],
        "hard skill": ["HTML", "CSS", "React", "JavaScript", "Cloud AWS"],
        "ferramentas": ["VSCode", "Figma", "GitHub"],
        "linkedin": "https://www.linkedin.com/in/adri-ana-gutierrez/",
        "github": "https://www.linkedin.com/in/adri-ana-gutierrez/"
    },
    {"nome": "Assis Vasconcelos", "slug": "assis-vasconcelos", "descricao": "Voltado para ciência de dados e análise preditiva."},
    
    {
        "nome": "Danilo Morais",
        "slug": "danilo-morais",
        "descricao": "Focado em qualidade de software e desenvolvimento Java.",
        "detalhada": "Tenho experiência com teste de sistemas, investigação de bugs e desenvolvimento backend em Java e Spring Boot.",
        "objetivo": "Atuar como Desenvolvedor Backend Júnior, com foco em crescimento técnico e entrega de valor.",
        "stack": ["Java", "Spring Boot", "SQL", "Flask", "Git"],
        "softskills": ["Trabalho em equipe", "Comunicação", "Proatividade", "Aprendizado contínuo"],
        "ferramentas": ["IntelliJ IDEA", "Pycharm", "VSCode", "Colab", "DBeaver", "GitHub"],
        "linkedin": "https://www.linkedin.com/in/danilomoraisdev/",
        "github": "https://github.com/Morais453"
    },    

    {"nome": "Diego Santos", "slug": "diego-santos", "descricao": "Entusiasta de backend e banco de dados."},
    {"nome": "Frank Melo", "slug": "frank-melo", "descricao": "Atuante em DevOps e práticas ágeis."},
    {
        "nome": "Nauani Cortonesi", 
        "slug": "nauani-cortonesi", 
        "descrição":"Interessada em desenvolvimento full stack java.",
        "detalhada":"Tenho experiência com trafégo pago e analise de mídias digitais."
        "objetivo":"Estou estudando para atuar como Desenvolvedora Full stack java TechLead."
        "Hard skill": ["Trafégo pago", "Design", "Cybersecurity", "Cloud AWS", "Marketing inbound e outbound"],
        "Soft skill":"["resolução de conflitos", "observação e decisão", "pensamentos estratégicos", "autodidatismo", "empatia, "competitividade"],
        "Linkedin":"http://www.linkedin.com/in/nauani-cortonesi/",
        "Github":"https://github.com/nauani-cortonesi"
    },
    
    {"nome": "Wesly Costa", 
    "slug": "wesly-costa", 
    "descrição": "Apaixonado por Inteligência artifical e automação.",
    "detalhada":"Ampla experiência no atendimento ao cliente, infraestrutrura, suporte local e remoto, etc."
    "objetivo":"Estudando para fornecer soluções, usando IA, automação e nuvem."
    "Hard skill": ["Suporte Técnico", "IA", "Cloud AWS"],
    "softskills": ["Trabalho em equipe", "Comunicação clara e objetiva", "Proatividade", "Aprendizado contínuo", "Resolução de Conflitos", "Paciência e Empatia", "Resolução de Problemas", "Documantação Técnica" ],
    "ferramentas": ["Jira Service", "AnyDesk", "VNC", "Microsoft Office 365", "windows", "Linux", "MacOS"],
    "linkedin": "https://www.linkedin.com/in/weslycosta/",
    "github": "https://github.com/WeslyCE"},
    
    {"nome": "Yuri Magalhães", "slug": "yuri-magalhaes", "descricao": "Curioso por cloud computing e automação."},
]

@app.route("/")
def index():
    return render_template("index.html", integrantes=integrantes)

@app.route("/portifolio/<slug>")
def portifolio(slug):
    integrante = next((i for i in integrantes if i["slug"] == slug), None)
    if integrante:
        return render_template("portifolio.html", integrante=integrante, integrantes=integrantes)
    return "Integrante não encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)
