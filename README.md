
# Distinção de # image-sorter-covid 

## 1. O que é o projeto?
O projeto tem como objetivo agilizar e dar uma um segunda opinião aos profissionais de saúde, pois imagens de raio-x são bem complicada es difíceis de compreender


## 2. O dataset

Um grande conjunto de dados pode ser considerado um _dataset_. O _dataset_ deste projeto conta com imagens de raio-x, contidos na pasta de treino e pasta de test, dividios em 3 pastas, COVID, Peneumonia e Normal(nenhum dos dois resultados )

Como umas das formas de diagnosticar paciente com covid e fazer um raio-x o corre que pacientes que apresentem o mesmo sintoma. E as vezes os medidos apresentaram dificuldades para determinar pela imagen de raio-x

## 3. O uso de _deep learning_ no projeto

_Deep Learning_ é conhecido como uma área dentro do aprendizado de máquina (também conhecido como _machine learning_) que faz o uso de algoritmos de redes neurais para encontrar padrões, previsões e identificação de imagens.

A rede neural é uma sequência de camadas e podemos usar o modelo sequencial oferecido pelo Keras, que possui as funções necessárias para construir cada camada de uma rede neural convolucional.

### 3.1 Construção da rede neural

A primeira camada de Convolução utiliza 32 features para o array 2D e o array no formato 3x3, As imagens de 64x64px serão armazenadas em um array .

Após a aplicação da primeira camada de Convolução é realizado um agrupamento para reduzir o mapa de features decorrente da primeira camada, reduzindo o tamanho dele.

Logo após o primeiro pooling, é adicionado outra camada de Convolução para tornar a rede mais profunda, após isso é realizado o segundo Pooling (Agrupamento).

Depois da segunda camada de convolução estar preparada é realizado o achatamento (Flatten), que converte a estrutura de dados 2D resultantes da segunda camada em 1D, ou seja, um vetor.

No próximo passo todas as camadas são conectadas utilizando uma função de ativação retificadora (relu). Também é utilizado então uma função de ativação sigmóide para obter as probabilidades de cada imagem conter um cachorro normal ou um vira-lata caramelo. O modelo raramente terá 100% de certeza e o que ele gera como um resultado é uma probabilidade.

Para compilar a rede, é utilizado o otimizador "Adam" e uma função log loss com "entropia binária cruzada". A métrica utilizada será a acurácia, pois essa é a maior preocupação no treinamento deste tipo de modelo.

## 5.0 Como rodar o projeto

Para rodar o projeto basta execultar o jupyter notebook no diretorio do projeto.

##

# 5.0 Resultados

Como resultado do treino e da predição temos que o treino realizou todas as etapas a acuracia acima de 80%, porém a predição falhou na imagem escolhida, indicando que a foto de um de covid tem peneumonia
O notebook da execução pode ser encontrado [aqui](https://github.com/deeplearningunb/image-sorter-covid/blob/main/classificador.ipynb).

## Desenvolvedores do projeto

160125910
- Itallo Cavalcante Gravina - 16/0125910

Referências

[1][deep learning - o que é e qual é a sua importância?](https://www.sas.com/pt_br/insights/analytics/deep-learning.html)

[2][afinal, o que é deep learning?](https://gaea.com.br/afinal-o-que-e-deep-learning/)

[3][redes neurais - o que são e qual é a sua importância?](https://www.sas.com/pt_br/insights/analytics/neural-networks.html)

[4] VARGAS, Ana Caroline Gomes; PAES, Aline; VASCONCELOS, Cristina Nader. Um estudo sobre redes neurais convolucionais e sua aplicação em detecção de pedestres. In: Proceedings of the XXIX Conference on Graphics, Patterns and Images. 2016. p. 1-4.

[5] KOVÁCS, Zsolt László. Redes neurais artificiais. Editora Livraria da Fisica, 2002.

[6][capítulo 47 – reconhecimento de imagens com redes neurais convolucionais em python – parte 4](http://deeplearningbook.com.br/reconhecimento-de-imagens-com-redes-neurais-convolucionais-em-python-parte-4/)
