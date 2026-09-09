# File Integrity Monitor (SHA-256)

Script simples em Python que monitora a integridade de um arquivo, avisando quando ele é alterado ou deletado. Feito como projeto de estudo sobre hashing e conceitos básicos de segurança da informação.

## Como funciona

O script calcula o hash SHA-256 do arquivo e fica verificando a cada 3 segundos se algo mudou:

- Se o arquivo for alterado, mostra o hash antigo e o novo.
- Se o arquivo for deletado, avisa e encerra a execução.
- Se nada mudar, apenas mostra `[OK] Arquivo intocado...` na mesma linha.

## Como usar

Só precisa ter o Python 3 instalado. Não usa nenhuma dependência externa — só as bibliotecas nativas (`hashlib`, `os` e `time`).

Clone o repositório e rode:

```bash
git clone https://github.com/gabriellebonet/file-integrity-monitor.git
cd file-integrity-monitor
python monitor.py
```

Por padrão, o script cria um arquivo `secret.txt` caso ele não exista.

## Testando

Com o script rodando:

- **Alterar:** edite e salve o `secret.txt` → o terminal mostra o alerta com o novo hash.
- **Deletar:** apague o arquivo → o terminal avisa a exclusão e encerra.
- **Parar:** pressione `Ctrl + C`.

## Sobre

Projeto feito para estudos, para entender na prática como hashes SHA-256 funcionam e como ferramentas de monitoramento de integridade de arquivos se comportam.

## Licença

MIT
