# CÓDIGO ORIGINAL (quebrado)

def interpolation_search_broken(A: list, v: int) -> int:
    # 1. ASSERÇÃO DE PRÉ-CONDICAO 
    assert all(A[i] < A[i+1] for i in range(len(A)-1)), "Erro: Pre-condicao violada! Array nao ordenado." 
    
    low, high = 0, len(A) - 1
    
    # 2. ASSERÇÃO DE INICIALIZAÇÃO (Caso Base)
    assert low <= high, "Erro: Invariante falhou na inicializacao!" 
    while low < high and A[low] <= v <= A[high]: 
        # Captura da Função Variante no início do passo 
        old_var = high - low
        assert old_var >= 0, "Erro: Variante violou o limite inferior!" 
        
        # Cálculo do ponto estimado de interpolação 
        pos = low + int(((float(high - low) / (A[high] - A[low])) * (v - A[low]))) 
        
        if A[pos] == v: 
            # 5. ASSERÇÃO DE PÓS-CONDICAO 
            assert A[pos] == v, "Erro: Pos-condicao falhou!" 
            return pos 
            
        elif A[pos] < v: 
            low = pos  # BUG: Não exclui o ponto estimado 
        else:
            high = pos # BUG: Não exclui o ponto estimado 
            
        # 4. ASSERÇÃO DE DECREMENTO (Progresso da Terminação)
        new_var = high - low
        assert new_var < old_var, "Erro: Loop em execucao infinita (sem progresso)!" 

    # Se saiu do loop, realiza a dedução final de ausência 
    idx = -1
    if idx == -1:
        # 5. ASSERÇÃO DE PÓS-CONDICAO 
        assert v not in A, "Erro: A pos-condicao falhou na terminacao!" 
    return idx



# CÓDIGO CORRIGIDO

def interpolation_search_verified(A: list, v: int) -> int:
    # 1. ASSERÇÃO DE PRÉ-CONDICAO: Array deve ser ordenado estritamente crescente
    assert all(A[i] < A[i+1] for i in range(len(A)-1)), "Erro: Pre-condicao violada! Array nao ordenado."
    
    low, high = 0, len(A) - 1
    
    # 2. ASSERÇÃO DE INICIALIZAÇÃO (Caso Base)
    assert low <= high, "Erro: Invariante falhou na inicializacao!"
    
    # Ajuste de segurança para verificar o extremo inicial antes do loop
    if len(A) > 0 and A[low] == v:
        return low
        
    while low < high and A[low] <= v <= A[high]:
        # Captura da Função Variante
        old_var = high - low
        assert old_var >= 0, "Erro: Variante violou o limite inferior!"
        
        pos = low + int(((float(high - low) / (A[high] - A[low])) * (v - A[low])))
        
        if A[pos] == v:
            # 5. ASSERÇÃO DE PÓS-CONDICAO
            assert A[pos] == v, "Erro: Pos-condicao falhou!"
            return pos
            
        elif A[pos] < v:
            low = pos + 1  # CORREÇÃO: Avança além do ponto estimado
        else:
            high = pos - 1 # CORREÇÃO: Recua aquém do ponto estimado
            
        # 4. ASSERÇÃO DE DECREMENTO (Progresso da Terminação)
        new_var = high - low
        assert new_var < old_var, "Erro: Loop em execucao infinita (sem progresso)!"

    # Ajuste final para checar se o ponteiro sobrou em cima do valor alvo
    if low == high and A[low] == v:
        assert A[low] == v, "Erro: Pos-condicao falhou!"
        return low

    idx = -1
    # 5. ASSERÇÃO DE PÓS-CONDICAO
    assert v not in A, "Erro: A pos-condicao falhou na terminacao!"
    return idx

# =====================================================================
# VERSÃO 1: CÓDIGO COM BUG INSTRUMENTADO (Dispara a falha de terminação)
# =====================================================================
def interpolation_search_broken(A: list, v: int) -> int:
    # 1. ASSERÇÃO DE PRÉ-CONDICAO: Array deve ser ordenado estritamente crescente
    assert all(A[i] < A[i+1] for i in range(len(A)-1)), "Erro: Pre-condicao violada! Array nao ordenado."
    
    low, high = 0, len(A) - 1
    
    # 2. ASSERÇÃO DE INICIALIZAÇÃO (Caso Base)
    assert low <= high, "Erro: Invariante falhou na inicializacao!"
    
    while low < high and A[low] <= v <= A[high]:
        # Captura da Função Variante no início do passo
        old_var = high - low
        assert old_var >= 0, "Erro: Variante violou o limite inferior!"
        
        # Fórmula de interpolação linear
        pos = low + int(((float(high - low) / (A[high] - A[low])) * (v - A[low])))
        
        if A[pos] == v:
            # 5. ASSERÇÃO DE PÓS-CONDICAO
            assert A[pos] == v, "Erro: Pos-condicao falhou!"
            return pos
            
        elif A[pos] < v:
            low = pos  # BUG: Não exclui o ponto estimado
        else:
            high = pos # BUG: Não exclui o ponto estimado
            
        # 4. ASSERÇÃO DE DECREMENTO (Progresso da Terminação)
        new_var = high - low
        assert new_var < old_var, "Erro: Loop em execucao infinita (sem progresso)!"

    # Se saiu do loop, realiza a dedução final de ausência
    idx = -1
    if idx == -1:
        # 5. ASSERÇÃO DE PÓS-CONDICAO
        assert v not in A, "Erro: A pos-condicao falhou na terminacao!"
    return idx


# =====================================================================
# VERSÃO 2: CÓDIGO CORRIGIDO E VERIFICADO (Termina com sucesso)
# =====================================================================
def interpolation_search_verified(A: list, v: int) -> int:
    # 1. ASSERÇÃO DE PRÉ-CONDICAO: Array deve ser ordenado estritamente crescente
    assert all(A[i] < A[i+1] for i in range(len(A)-1)), "Erro: Pre-condicao violada! Array nao ordenado."
    
    low, high = 0, len(A) - 1
    
    # 2. ASSERÇÃO DE INICIALIZAÇÃO (Caso Base)
    assert low <= high, "Erro: Invariante falhou na inicializacao!"
    
    # Ajuste de segurança para verificar o extremo inicial antes do loop
    if len(A) > 0 and A[low] == v:
        return low
        
    while low < high and A[low] <= v <= A[high]:
        # Captura da Função Variante
        old_var = high - low
        assert old_var >= 0, "Erro: Variante violou o limite inferior!"
        
        pos = low + int(((float(high - low) / (A[high] - A[low])) * (v - A[low])))
        
        if A[pos] == v:
            # 5. ASSERÇÃO DE PÓS-CONDICAO
            assert A[pos] == v, "Erro: Pos-condicao falhou!"
            return pos
            
        elif A[pos] < v:
            low = pos + 1  # CORREÇÃO: Avança além do ponto estimado
        else:
            high = pos - 1 # CORREÇÃO: Recua aquém do ponto estimado
            
        # 4. ASSERÇÃO DE DECREMENTO (Progresso da Terminação)
        new_var = high - low
        assert new_var < old_var, "Erro: Loop em execucao infinita (sem progresso)!"

    # Ajuste final para checar se o ponteiro sobrou em cima do valor alvo
    if low == high and A[low] == v:
        assert A[low] == v, "Erro: Pos-condicao falhou!"
        return low

    idx = -1
    # 5. ASSERÇÃO DE PÓS-CONDICAO
    assert v not in A, "Erro: A pos-condicao falhou na terminacao!"
    return idx


# DATA SET PARA ANÁLISE DE FALHA

if __name__ == "__main__":
    # Data Set fornecido no enunciado do Problema 4
    dataset_A = [10, 20, 30, 40, 50]
    v = 25
    
    print("Executando Bloco de Testes (Problema 4)")
    
    # Testando o código quebrado dentro de um bloco try/except para capturar o estouro da asserção
    try:
        print("\nTentando rodar o código original com bug...")
        # Isso deve estourar a asserção do Passo 4 (Garantia de progresso da variante)
        result = interpolation_search_broken(dataset_A, v)
    except AssertionError as error:
        print(f" Sucesso no teste de falha! Asserção capturou o bug esperado:")
        print(f"   Mensagem do erro: {error}")
        
    print("\n-------------------------------------------------")
    
    # Testando o código corrigido
    try:
        print("Tentando rodar o código corrigido...")
        result_c = interpolation_search_verified(dataset_A, v)
        print(f" Sucesso! O código corrigido terminou sem estourar nenhuma asserção.")
        print(f"   Resultado retornado: {result_c} (Significa elemento ausente)")
        
        # Teste extra com um elemento existente para garantir o funcionamento completo
        result_pres = interpolation_search_verified(dataset_A, 40)
        print(f"   Buscando o valor 40: Retornou índice {result_pres}")
    except AssertionError as erro:
        print(f" Erro inesperado: O código corrigido falhou na asserção: {erro}")

