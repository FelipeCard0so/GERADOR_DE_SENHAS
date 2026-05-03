# GERADOR_DE_SENHAS
Gerador de senhas de alta segurança desenvolvido em Python, utilizando o módulo secrets para entropia criptográfica (CSPRNG). Inclui detecção automática de ambiente para compatibilidade com IDEs (PyCharm/VS Code) e terminais nativos.

```markdown
# 🛡️ Secure Pass Generator PRO

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Security](https://img.shields.io/badge/security-CSPRNG-orange)

O **Secure Pass Generator PRO** é uma ferramenta robusta de linha de comando para geração de senhas resilientes. Diferente de geradores comuns que utilizam a biblioteca `random`, este projeto utiliza o módulo `secrets`, garantindo que as senhas geradas sejam criptograficamente seguras e adequadas para gerenciamento de segredos e senhas críticas.

## ✨ Funcionalidades

- **Criptografia de Elite:** Utiliza CSPRNG (Cryptographically Secure Pseudo-Random Number Generator).
- **Detecção de Ambiente:** Interface resiliente que se adapta automaticamente ao console do PyCharm, VS Code ou terminais nativos (TTY).
- **Garantia de Complexidade:** Assegura que cada senha contenha pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial.
- **Prevenção de Shoulder Surfing:** Mascaramento de entrada de dados sensíveis (Salt) em terminais compatíveis.

## 🚀 Como Executar

1. **Pré-requisitos:**
   - Possuir o Python 3.6 ou superior instalado.

2. **Instalação:**
   Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio
   ```

3. **Execução:**
   Execute o script diretamente:
   ```bash
   python main.py
   ```

## 🛠️ Detalhes Técnicos

O motor de geração (`PasswordEngine`) foi desenhado seguindo os princípios de **Solid** e as recomendações da **OWASP**:
- **Entropia:** O algoritmo de embaralhamento Fisher-Yates é aplicado via `secrets.SystemRandom` para eliminar qualquer padrão posicional.
- **Segurança de Memória:** Tratamento de inputs para evitar falhas de buffer e interrupções inesperadas.

## 📖 Exemplo de Uso

```text
[+] ID do Serviço/Usuário: Gmail_Principal
[+] Digite seu Salt Secreto: ********
[+] Comprimento desejado [Padrão 32]: 24

✅ ACESSO GERADO PARA: Gmail_Principal
🔑 CHAVE: Xo&UXhs#JX!ZGOynwne%L@5u
```

## 📄 Licença

FREE

---
Desenvolvido por: [FELIPE CARDOSO] - ESTUDANDO PARA SER UM Especialista em Segurança da Informação.
```

---
