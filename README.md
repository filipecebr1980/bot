# bot

## Bot simples desenvolvido em python 3.8 para uso no tweeter com a biblioteca tweepy.

### Uso: 

1. Atualize o arquivo matriz.csv com elementos da frase em cada linha, separado por ";" . As linhas podem ter qualquer quantidade argumentos e não é necessário que tenham os mesmos numeros em cada linha. Entretanto deve ter um numero fixo de linhas: 6 linhas. O arquivo deve estar codificado em UTF-8.

2. O arquivo apikeys.txt deve conter em cada linha as chaves credencias da API do tweeter na seguinte sequencia: api_key, api_secret_key, acess_key 
acess_key e acess_secret, respectivamente uma por linha.

3. O arquivo last_seen.txt contém um ID da última mensagem destinada ao bot e nao pode ser deixado em branco, pois uma das funções do programa retornaria um valor nulo e isto gera um erro que faz abortar a execução do programa. Portanto não é necessário editar esse arquivo.

4. Para rodar o bot: phyton3 robertobabot.py 
Esse arquivo em python pode ser renomeado sem problemas. Se você não tem instalada a biblioteca tweepy deve intalar com o seguinte comando: pip install tweepy

5. O bot responderá com uma frase aleatoria a todos que mandarem um twitt endereçado a ele. 

Agradecimentos ao Felipe Menegotto, que deu uma pequena classe de python e disponibilizou o código fonte que serviu de base para esse bot.
