# Sistema bancário em Python

## Descrição
Projeto desenvolvido no bootcamp de Ciência de Dados da DIO. É um sistema bancário simples que funciona apenas para um usuário, que realiza operações de depósito, saque e visualização de extrato.

## Funções

**Depósito:** o usuário digita o valor a ser depositado, o sistema verifica se o valor é positivo e,portanto, válido para depois incrementar no saldo. Ao fim da operação o sistema acrescenta uma linha na string "extrato" com as informações do depósito.

**Saque:** o usuário digita o valor a ser sacado em seguida o sistema faz as seguintes verificações:

    1) Valor digitado é válido?
    2) O cliente já fez a quantidade máxima de saques permitida por dia?
    3) O valor digitado é maior que o máximo permitido?
    4) O cliente tem saldo para sacar o valor digitado?

Se o valor digitado passar em todos os testes, o valor é decrementado do saldo e um contador de saques é incrementado por 1. Ao fim da operação o sistema acrescenta uma linha na string "extrato" com as informações do saque.

**Extrato:** todas as operções realizadas e o saldo atual são mostradas na tela.
