import cupom;

nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def test_exercicio1():
    assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_exercicio2_tudo_vazio():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    cupom.nome_loja = ""
    cupom.logradouro = ""
    cupom.numero = 0
    cupom.complemento = ""
    cupom.bairro = ""
    cupom.municipio = ""
    cupom.estado = ""
    cupom.cep = ""
    cupom.telefone = ""
    cupom.observacao = ""
    cupom.cnpj = ""
    cupom.inscricao_estadual = ""

    assert cupom.imprime_dados_loja() == '''
, 0 
 -  - 
CEP: Tel 

CNPJ: 
IE: 
'''

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "Magic Box"
    cupom.logradouro = "Baker St"
    cupom.numero = 221
    cupom.complemento = "EDA A24/25/26"
    cupom.bairro = "Marylebone"
    cupom.municipio = "Sunnydale"
    cupom.estado = "CA"
    cupom.cep = "79297"
    cupom.telefone = "(213) 70374-7092"
    cupom.observacao = "Loja TW (BTVS)"
    cupom.cnpj = "98.650.809/0001-63"
    cupom.inscricao_estadual = "55021852-1"

    #E atualize o texto esperado abaixo
    expected = "Magic Box\n"
    expected += "Baker St, 221 EDA A24/25/26\n"
    expected += "Marylebone - Sunnydale - CA\n"
    expected += "CEP:79297 Tel (213) 70374-7092\n"
    expected += "Loja TW (BTVS)\n"
    expected += "CNPJ: 98.650.809/0001-63\n"
    expected += "IE: 55021852-1\n"

    assert cupom.imprime_dados_loja() == expected
