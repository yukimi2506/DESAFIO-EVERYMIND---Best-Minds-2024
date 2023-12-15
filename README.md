README.md
Nunes Sports Product Management System

Este é um sistema simples de gerenciamento de produtos para a empresa fictícia Nunes Sports. A aplicação é construída usando Python e Flask para o backend, e HTML para o frontend. Utiliza SQLAlchemy para interação com o banco de dados SQLite.

Requisitos
Certifique-se de ter Python instalado em seu sistema. Caso não tenha, você pode baixá-lo em python.org.

Instalação
Clone este repositório para o seu ambiente local:
git clone https://github.com/seu-usuario/nunes-sports-product-management.git

Navegue até o diretório do projeto:
cd nunes-sports-product-management

Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv

Ative o ambiente virtual:
No Windows: venv\Scripts\activate
No macOS e Linux: source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Configuração do Banco de Dados
Abra o arquivo app.py e altere a configuração do banco de dados conforme necessário. Por padrão, está configurado para usar SQLite.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

Crie o banco de dados e as tabelas executando o seguinte comando no terminal:
python app.py

Executando a Aplicação
Certifique-se de que o ambiente virtual está ativado.

Execute o aplicativo Flask:
python app.py

Abra um navegador e acesse http://localhost:5000.

Agora você pode visualizar, adicionar, editar e excluir produtos através da interface web.








