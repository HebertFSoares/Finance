# Finance - Gerenciamento Financeiro Web

O projeto Finance é uma plataforma web desenvolvida em Django, projetada para ajudar os usuários a gerenciar suas finanças de maneira eficaz. Com funcionalidades de acompanhamento de depósitos, organização de despesas e uma visão abrangente das finanças pessoais, o Finance é a sua solução completa para manter suas finanças sob controle.

## Funcionalidades Principais

- **Registro de Depósitos:** Registre suas entradas de dinheiro de maneira organizada e categorizada.

- **Gerenciamento de Despesas:** Mantenha o controle das suas despesas, categorize-as e acompanhe seus gastos.

- **Visão Geral Financeira:** Obtenha uma visão abrangente das suas finanças, incluindo saldo atual, histórico de transações e tendências.

- **Metas Financeiras:** Defina metas de economia e orçamento e rastreie seu progresso.


## Tecnologias Utilizadas
- Python
- Django
- Sqlite
- HTML/CSS
- Bootstrap

## Requisitos
### Para executar o projeto em sua máquina local, você precisará ter o Python 3 instalado. Além disso, recomendamos utilizar um ambiente virtual para instalar as dependências necessárias.

## Instalação

### Clone este repositório em sua máquina local.

- Crie um ambiente virtual:
```
python3 -m venv myenv
```
- Ative o ambiente virtual:
```
source myenv/bin/activate
```
- Instale as dependências:
```
pip install -r requirements.txt
```
- Execute as migrações do banco de dados:
```
python manage.py migrate
```
- Crie um superusuário:
```
python manage.py createsuperuser
```
- Execute o servidor:
```
python manage.py runserver
```

## Contribuição
Este projeto é de código aberto e contribuições são bem-vindas. Se você quiser contribuir com o projeto, por favor, abra uma issue ou um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
