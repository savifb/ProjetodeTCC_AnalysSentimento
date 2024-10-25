# ProjetodeTCC_AnalysSentimento
 Projeto de TCC --- Análise de sentimento utilizando api da X para coletar dados e transformá-los, servindo como apoio às decisões públicas.   
markdown
Copiar código
# Análise de Sentimentos como Suporte às Decisões Públicas: Transformando Opiniões em Ações

## Descrição
Este projeto tem como objetivo desenvolver uma plataforma de análise de sentimentos utilizando dados de redes sociais, com foco em fornecer suporte às decisões na gestão pública. Através da coleta de tweets e da análise de sentimentos, os gestores públicos podem entender melhor a percepção da população sobre serviços essenciais como saúde, educação, transporte e segurança.

## Tecnologias que serão Utilizadas no projeto (pode mudar)
- **Python**: Linguagem de programação principal.
- **Tweepy**: Biblioteca para interação com a API do Twitter.
- **NLTK / TextBlob**: Para processamento de linguagem natural e análise de sentimentos.
- **Flask**: Para desenvolvimento do backend e criação do dashboard interativo.

## Estrutura do Projeto
```plaintext
analise_sentimentos/
│
├── coleta_dados/                # Scripts para coletar dados
│   └── coleta_tweets.py         # Script de coleta de tweets
│
├── processamento/                # Scripts para processamento de dados
│   ├── limpeza_dados.py         # Script para limpeza e pré-processamento
│   └── analise_sentimentos.py   # Script para análise de sentimentos
│
├── modelo/                       # Scripts para treinamento de modelo
│   └── treinar_modelo.py        # Script para treinar redes neurais
│
├── dashboard/                    # Scripts para o dashboard
│   └── app.py                   # Script principal para o dashboard
│
├── requisitos.txt                # Dependências do projeto
├── main.py                       # Script principal para execução
└── README.md                     # Documentação do projeto
Como Usar
Clone este repositório:

bash
Copiar código
git clone https://github.com/savifb/ProjetodeTCC_AnalysSentimento.git
cd ProjetodeTCC_AnalysSentimento

Licença
Este projeto está licenciado sob a Licença MIT.

Contato
Para mais informações, entre em contato:

Nome: Sávio Vinícius de Sousa
Email: savio.vinw@gmail.com
markdown







