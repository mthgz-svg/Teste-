# Arquivo: main.py

# 2. from bot_logic import gen_pass - importa a função do arquivo bot_logic
from bot_logic import gen_pass

# 3. gen_pass(10) - essa linha permite que você gere uma senha em qualquer parte do seu bot!
# Vamos testar a função chamando-a e imprimindo o resultado:
senha_teste = gen_pass(10)
print(f"Senha de teste gerada: {senha_teste}")
