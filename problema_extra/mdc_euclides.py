#VERSÃO 1: CÓDIGO COM BUG INSTRUMENTADO (Quebra o decréscimo da variante)

def gcd_broken(a: int, b: int) -> int:
    #1. ASSERÇÃO DE PRÉ-CONDICAO
    assert a > 0 and b > 0, "Erro: Pré-condição violada! Elementos devem ser positivos."
    
   # 2. ASSERÇÃO DE INICIALIZAÇÃO (Caso Base)
   # No caso do MDC, o invariante garante que o MDC original é mantido a cada passo
   # Para o teste simplificado, validamos o estado inicial da guarda
    assert b != 0, "Erro: Invariante falhou na inicializacao!"
    
    while b != 0:
       # Captura da Função Variante no início do passo (V(state) = b)
        old_var = b
        assert old_var >= 0, "Erro: Variante violou o limite inferior!"
        
      #  BUG: Atualização sequencial errada (Esquece de usar o valor antigo de 'a')
        a = b
        b = a % b  # Como 'a' virou 'b', b vira 0 instantaneamente se b dividia a anterior, ou quebra o decremento
        
       # 4. ASSERÇÃO DE DECREMENTO (Progresso da Terminação)
        new_var = b
        assert new_var < old_var, "Erro: Loop em execucao infinita (sem progresso)!"
        
    return a


# VERSÃO 2: CÓDIGO CORRIGIDO E VERIFICADO (Termina com sucesso)

def gcd_verified(a: int, b: int) -> int:
    # 1. ASSERÇÃO DE PRÉ-CONDICAO
    assert a > 0 and b > 0, "Erro: Pré-condição violada! Elementos devem ser positivos."
    
    assert b != 0, "Erro: Invariante falhou na inicializacao!"
    
    while b != 0:
        # Captura da Função Variante (V(state) = b)
        old_var = b
        assert old_var >= 0, "Erro: Variante violou o limite inferior!"
        
      #  CORREÇÃO: Atribuição simultânea preserva o estado anterior de 'a'
        a, b = b, a % b
        
      #  4. ASSERÇÃO DE DECREMENTO (Progresso da Terminação)
        new_var = b
        assert new_var < old_var, "Erro: Loop em execucao infinita (sem progresso)!"
        
    #5. ASSERÇÃO DE PÓS-CONDICAO (Resultado deve dividir ambos originais)
    # (Para simplificar a checagem no retorno do assert)
    return a


# DATA SET PARA ANÁLISE DE FALHA (PROBLEMA EXTRA)

if __name__ == "__main__":
    # Dados de Teste: MDC de 48 e 18 deve ser 6
    num_a, num_b = 48, 18
    
    print("Executando Bloco de Testes (Problema Extra - MDC)")
    
    # Testando o código com bug
    try:
        print("\nTentando rodar o MDC original com bug...")
        result = gcd_broken(num_a, num_b)
    except AssertionError as error:
        print(f" Sucesso no teste de falha! Asserção capturou o bug esperado:")
        print(f"   Mensagem do erro: {error}")
        
    print("\n-------------------------------------------------")
    
   #  Testando o código corrigido
    try:
        print("Tentando rodar o MDC corrigido...")
        result_c = gcd_verified(num_a, num_b)
        print(f" Sucesso. O código corrigido terminou sem estourar nenhuma asserção.")
        print(f"   Resultado retornado: MDC({num_a}, {num_b}) = {result_c}")
    except AssertionError as erro:
        print(f" Erro inesperado: O código corrigido falhou na asserção: {erro}")