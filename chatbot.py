from dotenv import load_dotenv # Variáveis de ambiente
import os # Manipulação de arquivos e diretórios

from langchain.chat_models import init_chat_model # Inicialização do modelo de chat
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage # Mensagens do usuário, IA e sistema

load_dotenv()# Carrega as variáveis de ambiente do arquivo .env

os.environ.get("GOOGLE_API_KEY")# Obtém a variável de ambiente GOOGLE_API_KEY

if not os.environ.get("GOOGLE_API_KEY"):# Verifica se a variável de ambiente GOOGLE_API_KEY está definida
  os.environ["GOOGLE_API_KEY"] = input("Digite sua chave de API do Google: ") # Se não estiver definida, solicita ao usuário que insira a chave de API

# Inicializa a lista de mensagens com um exemplo de conversa, uma forma de treinar o modelo
messages =[
        SystemMessage("Você é um assistente de reservas de horários de barbearia. \
            Você questiona qual o nome, horário e dia que o cliente deseja agendar e informa \
            se há disponibilidade. Ao final do atendimento, diga ao cliente digitar 'sair', para sair do chat."),
    HumanMessage("Bom dia, gostaria de agendar um horário na barbearia."),
    AIMessage("Bom dia! Claro! Por favor informe o seu nome, dia e horário para que eu possa agendar."),
    HumanMessage("Meu nome é Roberto, quero agendar para amanhã às 15:00."),
    AIMessage("Ótimo, Roberto! Deixe-me verificar a disponibilidade para amanhã às 15:00."),
    AIMessage("Sim, temos disponibilidade para amanhã às 15:00. Seu horário está agendado!"),
]
# Inicializa o modelo de chat com o modelo "gemini-2.5-flash" da Google GenAI
model = init_chat_model("gemini-2.5-flash", model_provider="google-genai")
# Inicia um loop para receber entradas do usuário e gerar respostas do modelo
print("Bem-vindo ao assistente de agendamento de barbearia!")
while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Saindo do chat.")
        break
    messages.append(HumanMessage(user_input))
    response = model.invoke(messages)
    messages.append(response)
    print(response.content)
