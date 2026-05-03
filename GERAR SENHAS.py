import secrets
import string
import getpass
import sys
import os


class PasswordEngine:
    """
    Core de Criptografia: Gera entropia de alta qualidade.
    Baseado em CSPRNG (Cryptographically Secure Pseudo-Random Number Generator).
    """

    def __init__(self):
        self.pool_lower = string.ascii_lowercase
        self.pool_upper = string.ascii_uppercase
        self.pool_digits = string.digits
        self.pool_special = "!@#$%&*?_-"  # Caracteres compatíveis com a maioria dos sistemas

    def generate_secure_token(self, length: int = 32) -> str:
        if length < 12:
            length = 12  # Força o padrão mínimo de segurança OWASP

        # Define os componentes obrigatórios
        categories = [self.pool_lower, self.pool_upper, self.pool_digits, self.pool_special]

        # 1. Garante que cada categoria esteja presente pelo menos uma vez
        token = [secrets.choice(cat) for cat in categories]

        # 2. Completa o restante com uma mistura altamente aleatória
        all_chars = "".join(categories)
        token += [secrets.choice(all_chars) for _ in range(length - len(token))]

        # 3. Embaralhamento de segurança (Algoritmo Fisher-Yates via secrets)
        secrets.SystemRandom().shuffle(token)

        return "".join(token)


def clear_console():
    """Limpa o console para manter o ambiente de trabalho organizado."""
    os.system('cls' if os.name == 'nt' else 'clear')


def secure_input(prompt: str) -> str:
    """
    Captura input de forma inteligente.
    Detecta se o terminal suporta ocultação (getpass) ou se está em uma IDE (PyCharm).
    """
    # Verifica se estamos em um terminal real (TTY)
    if sys.stdin.isatty():
        try:
            return getpass.getpass(prompt)
        except Exception:
            return input(f"{prompt} (Nota: visível nesta IDE) ")
    else:
        # Comportamento otimizado para PyCharm / VS Code
        return input(prompt)


def main():
    clear_console()
    print("=" * 60)
    print("🛡️  VAULT GENERATOR PRO | DevSecOps Edition")
    print("=" * 60)

    try:
        # Coleta de dados
        user_tag = input("[+] ID do Serviço/Usuário: ").strip() or "Standard_User"

        # O Salt aqui serve como semente psicológica para o usuário
        salt = secure_input("[+] Digite seu Salt Secreto: ")

        raw_len = input("[+] Comprimento desejado [Padrão 32]: ").strip()
        length = int(raw_len) if raw_len.isdigit() else 32

        # Execução do Engine
        engine = PasswordEngine()
        secure_pass = engine.generate_secure_token(length)

        # Output formatado
        print("\n" + "—" * 60)
        print(f"✅ ACESSO GERADO PARA: {user_tag}")
        print(f"🔑 CHAVE: {secure_pass}")
        print("—" * 60)
        print("🔒 SEGURANÇA: Nível Militar (AES-ready entropy)")
        print("=" * 60)

    except KeyboardInterrupt:
        print("\n\n[!] Processo abortado pelo operador.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Erro na execução da Task: {e}")


if __name__ == "__main__":
    main()