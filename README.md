 <header>
        <h1>Assistente de Agendamento de Barbearia</h1>
        <p>Projeto usando Python, LangChain e Google GenAI</p>
    </header>
    <main>
        <h2>🚀 Funcionalidades</h2>
        <ul>
            <li>Conversa interativa com o cliente via terminal.</li>
            <li>Solicita informações para o agendamento (nome, dia e horário).</li>
            <li>Retorna a confirmação caso o horário esteja disponível.</li>
            <li>Utiliza o modelo <strong>gemini-2.5-flash</strong> da Google GenAI via LangChain.</li>
            <li>Carrega variáveis de ambiente com segurança usando <code>python-dotenv</code>.</li>
        </ul>
        <h2>🛠️ Tecnologias utilizadas</h2>
        <ul>
            <li>Python 3.10+</li>
            <li>LangChain</li>
            <li>Google GenAI (Gemini)</li>
            <li>python-dotenv</li>
        </ul>
        <h2>📦 Instalação</h2>
        <ol>
            <li><strong>Clone o repositório</strong>
                <pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio</code></pre>
            </li>
            <li><strong>Crie e ative um ambiente virtual</strong>
                <pre><code>python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows</code></pre>
            </li>
            <li><strong>Instale as dependências</strong>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Configure a variável de ambiente da API Key</strong>
                <p>Crie um arquivo <code>.env</code> na raiz do projeto:</p>
                <pre><code>GOOGLE_API_KEY=sua_chave_aqui</code></pre>
            </li>
        </ol>
        <h2>▶️ Como executar</h2>
        <pre><code>python main.py</code></pre>
        <p>Para sair do chat, digite:</p>
        <pre><code>sair</code></pre>
        <h2>📂 Estrutura do projeto</h2>
        <pre><code>.
            ├── chatbot.py           # Código principal do assistente
            ├── .env              # Variáveis de ambiente (não subir para o GitHub)
            ├── requirements.txt  # Dependências do projeto
            └── README.md       # Documentação</code></pre>
        <h2>📜 Exemplo de uso</h2>
        <pre><code>Bem-vindo ao assistente de agendamento de barbearia!
            Você: Bom dia, quero marcar um horário
            Assistente: Claro! Qual o seu nome, dia e horário desejado?
            Você: Roberto, amanhã às 15:00
            Assistente: Ótimo, Roberto! Verificando disponibilidade...
            Assistente: Sim, temos disponibilidade. Seu horário está agendado!</code></pre>
        <h2>⚠️ Observações</h2>
        <ul>
            <li>Não compartilhe sua <strong>GOOGLE_API_KEY</strong> em repositórios públicos.</li>
            <li>Este projeto está configurado para rodar no terminal, mas pode ser adaptado para interfaces web ou APIs.</li>
        </ul>
    </main>
