import numpy as np

# Método adpatado de https://www.youtube.com/watch?v=-rUm7Lx5VbE
# Fonte = https://real-statistics.com/tests-normality-and-symmetry/statistical-tests-normality-symmetry/kolmogorov-smirnov-test/
# Fonte = https://real-statistics.com/statistics-tables/kolmogorov-smirnov-table/

'''
A função abaixo usa as informações da tabela de Dn,a e seus valores 
criticos de cada porcetagem de confiança para amostras maiores que 50
'''

def kolmogorov_smirnov_critico(n, ks_stats):

    alphas = [20, 15, 10, 5, 1] # 80% 85% 90% 95% 99%
    const = [1.07275, 1.13795, 1.22385, 1.35810, 1.62762]
    
    for i in range(len(alphas)):
        
        ks_critico = const[i] / (np.sqrt(n))

        if ks_critico > ks_stats:
            print(f"Com {(100 - alphas[i])}% de confiança, teve evidências para ACEITAR a hipótese nula, segundo o teste de Kolmogorov-Smirnov a distribuição  é Normal")
        else:
            print(f"Com {(100 - alphas[i])}% de confiança, teve evidências para REJEITAR a hipótese nula, segundo o teste de Kolmogorov-Smirnov a distribuição NÃO é Normal")

