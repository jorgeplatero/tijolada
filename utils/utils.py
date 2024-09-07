import streamlit as st
import pandas as pd
import plotly.express as px
import controllers.controllers as controllers
import models.models as models


#consultas
#---------------------------------------------------------------

#clientes
def consulta_clientes():
    clientes = []
    try:
        for item in controllers.select_clientes():
            clientes.append(
                [
                    item.id_cliente, item.nome_cliente, item.tipo_cliente, item.cpf_cnpj_cliente,
                    item.endereco_cliente, item.bairro_cliente, item.telefone_cliente, 
                    item.referencia_cliente, item.situacao_cliente
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return clientes


#fornecedores
def consulta_fornecedores():
    fornecedores = []
    try:
        for item in controllers.select_fornecedores():
            fornecedores.append(
                [
                    item.id_fornecedor, item.nome_fornecedor, item.cnpj_fornecedor,
                    item.endereco_fornecedor, item.bairro_fornecedor, item.telefone_fornecedor
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return fornecedores


#produtos
def consulta_produtos():
    produtos = []
    try:
        for item in controllers.select_produtos():
            produtos.append([item.id_produto, item.nome_produto, item.unidade_medida_produto])
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return produtos


#compras
def consulta_compras():
    compras = []
    try:
        for item in controllers.select_compras():
            compras.append(
                [
                    item.id_compra, item.data_compra, item.fornecedor_id_fornecedor, item.preco_total_compra, 
                    item.situacao_pagamento_compra, item.situacao_entrega_compra, item.forma_pagamento_compra
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return compras


#itens de compras
def consulta_compras_produtos():
    compras_produtos = []
    try:
        for item in controllers.select_compras_produtos():
            compras_produtos.append(
                [
                    item.id_compra_produto, item.compra_id_compra, item.produto_id_produto, 
                    item.preco_unitario_produto_compra, item.quantidade_produto_compra
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return compras_produtos


#vendas
def consulta_vendas():
    vendas = []
    try:
        for item in controllers.select_vendas():
            vendas.append(
                [
                    item.id_venda, item.data_venda, item.cliente_id_cliente,
                    item.endereco_entrega_venda, item.bairro_entrega_venda, item.observacoes_venda,
                    item.preco_total_venda, item.situacao_pagamento_venda, item.situacao_entrega_venda,
                    item.forma_pagamento_venda
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return vendas


#itens de vendas
def consulta_vendas_produtos():
    vendas_produtos = []
    try:
        for item in controllers.select_vendas_produtos():
            vendas_produtos.append(
                [
                    item.id_venda_produto, item.venda_id_venda, item.produto_id_produto, 
                    item.preco_unitario_produto_venda, item.quantidade_produto_venda
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return vendas_produtos


#estoque
def consulta_estoques():
    estoques = []
    try:
        for item in controllers.select_estoques():
            estoques.append(
                [
                    item.id_estoque, item.produto_id_produto, item.quantidade_estoque
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return estoques


#inserts
#---------------------------------------------------------------

#clientes
def insert_clientes():
    with st.form(key='insert_clientes'):
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**Nome**')
            input_nome_cliente = st.text_input(label='Nome', max_chars=100, label_visibility='collapsed')
        with col2:
            st.write('**Telefone**')
            input_telefone_cliente = st.text_input(label='Telefone', max_chars=15, label_visibility='collapsed')
        st.write('**Tipo**')
        input_tipo_cliente = st.selectbox(label='Tipo', options=['Pessoa Física', 'Pessoa Jurídica'], placeholder='Selecione o tipo de cliente', index=None, label_visibility='collapsed')
        st.write('**CPF/CNPJ**')
        input_cpf_cnpj_cliente = st.text_input(label='CPF/CNPJ', max_chars=18, label_visibility='collapsed')
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**Endereço**')
            input_endereco_cliente = st.text_input(label='Endereço', max_chars=100, label_visibility='collapsed')
        with col2:
            st.write('**Bairro**')
            input_bairro_cliente = st.text_input(label='Bairro', max_chars=50, label_visibility='collapsed')
        st.write('**Referência**')
        input_referencia_cliente = st.text_input(label='Referência', max_chars=255, label_visibility='collapsed')
        st.write('**Situação**')
        input_situacao_cliente = st.selectbox(label='Situação', options=['Adimplente', 'Inadimplente'], placeholder='Selecione a situação do cliente', index=None, label_visibility='collapsed')
        input_botao_inserir_cliente = st.form_submit_button('**Inserir**')
    if input_botao_inserir_cliente:
        try:
            controllers.insert_clientes(
                models.Cliente(
                    0, input_nome_cliente, input_tipo_cliente, input_cpf_cnpj_cliente, input_endereco_cliente, 
                    input_bairro_cliente, input_telefone_cliente, input_referencia_cliente, input_situacao_cliente
                )
            )
        except Exception as e:
            st.error(f'Erro durante inserção: {e}')
    else:
        pass


#fornecedores
def insert_fornecedores():
    with st.form(key='insert_fornecedores'):
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**Nome**')
            input_nome_fornecedor = st.text_input(label='Nome', max_chars=100, label_visibility='collapsed')
        with col2:
            st.write('**Telefone**')
            input_telefone_fornecedor = st.text_input(label='Telefone', max_chars=15, label_visibility='collapsed')
        st.write('**CNPJ**')
        input_cnpj_fornecedor = st.text_input(label='CNPJ', max_chars=18, label_visibility='collapsed')
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**Endereço**')
            input_endereco_fornecedor = st.text_input(label='Endereço', max_chars=100, label_visibility='collapsed')
        with col2:
            st.write('**Bairro**')
            input_bairro_fornecedor = st.text_input(label='Bairro', max_chars=50, label_visibility='collapsed')
        input_botao_inserir_fornecedor = st.form_submit_button('**Inserir**')
    if input_botao_inserir_fornecedor:
        try:
            controllers.insert_fornecedores(
                models.Fornecedor(0, input_nome_fornecedor, input_cnpj_fornecedor, input_endereco_fornecedor, input_bairro_fornecedor, input_telefone_fornecedor)
            )
        except Exception as e:
            st.error(f'Erro durante inserção: {e}')
    else:
        pass


#produtos
def insert_produtos():
    with st.form(key='insert_produtos'):
        opcoes_unidade_medida = ['un', 'm', 'm²', 'm³', 'l', 'kg', 'lata', 'caminhão']
        st.write('**Nome**')
        input_nome_produto = st.text_input(label='Nome', max_chars=255, label_visibility='collapsed')
        st.write('**Unidade de Medida**')
        input_unidade_medida_produto = st.selectbox(label='Unidade de Medida', placeholder='Selecione a unidade de medida', index=None, options=opcoes_unidade_medida, label_visibility='collapsed')
        input_botao_inserir_produto = st.form_submit_button('**Inserir**')
    if input_botao_inserir_produto:
        try:
            controllers.insert_produtos(
                models.Produto(0, input_nome_produto, input_unidade_medida_produto)
            )
        except Exception as e:
            st.error(f'Erro durante inserção: {e}')
    else:
        pass
    

#compras
def insert_compras():
    with st.form(key='insert_compras'):
        opcoes_pagamento = ['Crédito', 'Débito', 'Dinheiro', 'PIX']
        df_compra_produto = pd.DataFrame(columns=['ID Produto', 'Preço Unitário', 'Quantidade'])
        #compra
        st.write('**ID do Fornecedor**')
        input_fornecedor_id_fornecedor = st.selectbox(label='ID Fornecedor', options=[row[0] for row in consulta_fornecedores()], placeholder='Selecione o ID do cliente', index=None, label_visibility='collapsed')
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Situação do Pagamento**')
            input_situacao_pagamento_compra = st.selectbox(label='Situação do Pagamento', options=['Não realizada', 'Realizado'], placeholder='Selecione a situação do pagamento', index=None, label_visibility='collapsed')
        with col2:
            st.write('**Situação da Entrega**')
            input_situacao_entrega_compra = st.selectbox(label='Situação da Entrega', options=['Não realizada', 'Realizado'], placeholder='Selecione a situação da entrega', index=None, label_visibility='collapsed')
        st.write('**Forma de pagamento**')
        input_forma_pagamento_compra = st.selectbox(label='Forma de pagamento', options=opcoes_pagamento, placeholder='Selecione a forma de pagamento', index=None, label_visibility='collapsed')
        #itens de venda
        st.write('**Itens de Compra**')
        df_compra_produto = st.data_editor(
            df_compra_produto,
            column_config={
                'ID Produto': st.column_config.SelectboxColumn(
                    label='ID do Fornecedor',
                    help='Selecione o codigo do produto',
                    options=[row[0] for row in consulta_produtos()],
                    required=True
                ),
                'Preço Unitário': st.column_config.NumberColumn(
                    label='Preço Unitário (R$)',
                    help='Insira o preço unitário do produto',
                    format='R$ %.2f',
                    required=True,
                ),
                'Quantidade': st.column_config.NumberColumn(
                    help='Insira a quantidade',
                    format='%d',
                    required=True
                )
            },
            num_rows='dynamic', 
            use_container_width=False
        )
        input_botao_inserir_compra = st.form_submit_button('**Inserir**')
    if input_botao_inserir_compra:
        try:
            id_compra = controllers.insert_compras(
                models.Compra(
                        0, 0, input_fornecedor_id_fornecedor, 0, 
                        input_situacao_pagamento_compra, input_situacao_entrega_compra, input_forma_pagamento_compra
                    )
            )
            for _, row in df_compra_produto.iterrows():
                input_compra_id_compra = id_compra
                input_produto_id_produto = row[0]
                input_preco_unitario_produto_compra = row[1]
                input_quantidade_produto_compra = row[2]
                controllers.insert_produtos_compras(
                        models.CompraProduto(
                                0, input_compra_id_compra, input_produto_id_produto, input_preco_unitario_produto_compra,
                                input_quantidade_produto_compra
                            )
                    )
        except Exception as e:
            st.error(f'Erro durante inserção: {e}')
    else:
        pass
    
    
#vendas
def insert_vendas():
    with st.form(key='insert_vendas'):
        opcoes_pagamento = ['Crédito', 'Débito', 'Dinheiro', 'PIX']
        df_venda_produto = pd.DataFrame(columns=['ID Produto', 'Quantidade'])
        #venda
        st.write('**ID do Cliente**')
        input_cliente_id_cliente = st.selectbox(label='ID Cliente', options=[row[0] for row in consulta_clientes()], placeholder='Selecione o ID cliente', index=None, label_visibility= 'collapsed')
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**Endereço de Entrega**')
            input_endereco_entrega_venda = st.text_input(label='Endereço de entrega', label_visibility='collapsed')
        with col2:
            st.write('**Bairro de Entrega**')
            input_bairro_entrega_venda = st.text_input(label='Bairro de entrega', label_visibility='collapsed')
        st.write('**Observações**')
        input_observacoes_venda = st.text_input(label='Observações', label_visibility='collapsed')
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Situação do Pagamento**')
            input_situacao_pagamento_venda = st.selectbox(label='Situação do Pagamento', options=['Não realizada', 'Realizado'], placeholder='Selecione a situação do pagamento', index=None, label_visibility='collapsed')
        with col2:
            st.write('**Situação da Entrega**')
            input_situacao_entrega_venda = st.selectbox(label='Situação da Entrega', options=['Não realizada', 'Realizado'], placeholder='Selecione a situação da entrega', index=None, label_visibility='collapsed')
        st.write('**Forma de pagamento**')
        input_forma_pagamento_venda = st.selectbox(label='Forma de pagamento', options=opcoes_pagamento, placeholder='Selecione a forma de pagamento', index=None, label_visibility='collapsed')
        #itens de venda
        df_venda_produto = st.data_editor(
            df_venda_produto,
            column_config={
                'ID Produto': st.column_config.SelectboxColumn(
                    label='ID do Produto',
                    help='Selecione o ID do produto',
                    options=[row[0] for row in consulta_produtos()],
                    required=True
                ),
                'Quantidade': st.column_config.NumberColumn(
                    help='Insira a quantidade',
                    format='%d',
                    required=True
                )
            },
            num_rows='dynamic', 
            use_container_width=False
        )
        input_botao_inserir_venda = st.form_submit_button('**Inserir**')
    if input_botao_inserir_venda:
        try:
            id_venda = controllers.insert_vendas(
                models.Venda(
                        0, 0, input_cliente_id_cliente, input_endereco_entrega_venda, input_bairro_entrega_venda, 
                        input_observacoes_venda, 0, input_situacao_pagamento_venda, input_situacao_entrega_venda, 
                        input_forma_pagamento_venda
                    )
            )
            for _, row in df_venda_produto.iterrows():
                input_venda_id_venda = id_venda
                input_produto_id_produto = row[0]
                input_quantidade_produto_venda = row[1]
                controllers.insert_produtos_vendas(
                    models.VendaProduto(
                            0, input_venda_id_venda, input_produto_id_produto, 0,
                            input_quantidade_produto_venda
                        )
                )
        except Exception as e:
            st.error(f'Erro durante inserção: {e}')
    else:
        pass


#updates
#---------------------------------------------------------------

#clientes
def update_clientes():
    with st.form(key='update_clientes'):
        #formulário
        col1, col2 = st.columns([.3, .7])
        with col1:
            st.write('**ID do Cliente**')
            input_id_cliente = st.selectbox(label='ID Cliente', options=[row[0] for row in consulta_clientes()], placeholder='Selecione o ID do cliente', index=None, label_visibility='collapsed')
        with col2:
            st.write('**Nome**')
            input_nome_cliente = st.text_input(label='Nome', max_chars=100, label_visibility='collapsed')
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**CPF/CNPJ**')
            input_cpf_cnpj_cliente = st.text_input(label='CPF/CNPJ', max_chars=18, label_visibility='collapsed')
        with col2:
            st.write('**CPF/CNPJ**')
            input_telefone_cliente = st.text_input(label='Telefone', max_chars=15, label_visibility='collapsed')
        st.write('**Tipo**')
        input_tipo_cliente = st.selectbox(label='Tipo', options=['Pessoa Física', 'Pessoa Jurídica'], placeholder='Selecione o tipo de cliente', index=None, label_visibility='collapsed')
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**Endereço**')
            input_endereco_cliente = st.text_input(label='Endereço', max_chars=100, label_visibility='collapsed')
        with col2:
            st.write('**Bairro**')
            input_bairro_cliente = st.text_input(label='Bairro', max_chars=50, label_visibility='collapsed')
        st.write('**Referência**')
        input_referencia_cliente = st.text_input(label='Referência', max_chars=255, label_visibility='collapsed')
        st.write('**Situação**')
        input_situacao_cliente = st.selectbox(label='Situação', options=['Adimplente', 'Inadimplente'], placeholder='Selecione a situação do cliente', index=None, label_visibility='collapsed')
        input_botao_alterar_cliente = st.form_submit_button('**Atualizar**')
    if input_botao_alterar_cliente:
        try:
            controllers.update_clientes(
                models.Cliente(
                    input_id_cliente, input_nome_cliente, input_tipo_cliente, input_cpf_cnpj_cliente, input_endereco_cliente, 
                    input_bairro_cliente, input_telefone_cliente, input_referencia_cliente, input_situacao_cliente
                )
            )
        except Exception as e:
            st.error(f'Erro durante update: {e}')
    else:
        pass
    
    
#fornecedores
def update_fornecedores():
    with st.form(key='update_fornedores'):
        #formulário
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**ID do Fornecedor**')
            input_id_fornecedor = st.selectbox(label='ID Fornecedor', options=[row[0] for row in consulta_fornecedores()], placeholder='Selecione o ID do fornecedor', index=None, label_visibility='collapsed')
        with col2:
            st.write('**Nome**')
            input_nome_fornecedor = st.text_input(label='Nome', max_chars=100, label_visibility='collapsed')
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**CNPJ**')
            input_cnpj_fornecedor = st.text_input(label='CNPJ', max_chars=18, label_visibility='collapsed')
        with col2:
            st.write('**Telefone**')
            input_telefone_fornecedor = st.text_input(label='Telefone', max_chars=15, label_visibility='collapsed')
        col1, col2 = st.columns([.6, .4])
        with col1:
            st.write('**Endereço**')
            input_endereco_fornecedor = st.text_input(label='Endereço', max_chars=100, label_visibility='collapsed')
        with col2:
            st.write('**Bairro**')
            input_bairro_fornecedor = st.text_input(label='Bairro', max_chars=50, label_visibility='collapsed')
        input_botao_alterar_fornecedor = st.form_submit_button('**Atualizar**')
    if input_botao_alterar_fornecedor:
        try:
            controllers.update_fornecedores(
                models.Fornecedor(
                    input_id_fornecedor, input_nome_fornecedor, input_cnpj_fornecedor, 
                    input_endereco_fornecedor, input_bairro_fornecedor, input_telefone_fornecedor)
            )
        except Exception as e:
            st.error(f'Erro durante update: {e}')
    else:
        pass


#produtos
def update_produtos():
    with st.form(key='update_produtos'):
        opcoes_unidade_medida = ['un', 'm', 'm²', 'm³', 'l', 'kg', 'lata', 'caminhão']
        #formulário
        col1, col2 = st.columns([.3, .7])
        with col1:
            st.write('**ID do Produto**')
            input_id_produto = st.selectbox(label='ID Produto', options=[row[0] for row in consulta_produtos()], placeholder='Selecione o ID do produto', index=None, label_visibility='collapsed')
        with col2:
            st.write('**Nome**')
            input_nome_produto = st.text_input(label='Nome', max_chars=255, label_visibility='collapsed')
        col1, _ = st.columns([.3, .7])
        with col1:
            st.write('**Unidade de Medida**')
            input_unidade_medida_produto = st.selectbox(label='Unidade de Medida', options=opcoes_unidade_medida, placeholder='Selecione a unidade de medida', index=None, label_visibility='collapsed')
        input_botao_alterar_produto = st.form_submit_button('**Atualizar**')
    if input_botao_alterar_produto:
        try:
            controllers.update_produtos(
                models.Produto(input_id_produto, input_nome_produto, input_unidade_medida_produto)
            )
        except Exception as e:
            st.error(f'Erro durante update: {e}')
    else:
        pass
    

#compras
def update_compras():
    with st.form(key='update_compras'):
        opcoes_pagamento = ['Crédito', 'Débito', 'Dinheiro', 'PIX']
        col1, col2 = st.columns(2)
        with col1:
            st.write('**ID da Compra**')
            input_id_compra = st.selectbox(
                label='ID Compra', 
                placeholder='Selecione o ID da compra', 
                options=[row[0] for row in consulta_compras()],
                index=None,
                label_visibility='collapsed'
            )
        with col2:
            st.write('**ID da Fornecedor**')
            input_fornecedor_id_fornecedor = st.selectbox(
                label='ID Fornecedor', 
                placeholder='Selecione o ID do fornecedor',
                options=[row[0] for row in consulta_fornecedores()],
                index=None,
                label_visibility='collapsed'
            )
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Situação do Pagamento**')
            input_situacao_pagamento_compra = st.selectbox(label='Situação do Pagamento', options=['Não realizada', 'Realizado'], placeholder='Selecione a situação da pagamento', index=None, label_visibility='collapsed')
        with col2:
            st.write('**Situação da Entrega**')
            input_situacao_entrega_compra = st.selectbox(label='Situação da Entrega', options=['Não realizada', 'Realizado'], placeholder='Selecione a situação da entrega', index=None, label_visibility='collapsed')
        st.write('**Forma de Pagamento**')
        input_forma_pagamento_compra = st.selectbox(label='Forma de Pagamento', options=opcoes_pagamento, placeholder='Selecione a forma de pagamento', index=None, label_visibility='collapsed')
        input_botao_alterar_compra = st.form_submit_button('**Atualizar**')
    if input_botao_alterar_compra:
        try:
            controllers.update_compras(
                models.Compra(
                        input_id_compra, 0, input_fornecedor_id_fornecedor, 0, 
                        input_situacao_pagamento_compra, input_situacao_entrega_compra, input_forma_pagamento_compra
                    )
            )
        except Exception as e:
            st.error(f'Erro durante update: {e}')
    else:
        pass


#itens de compra
def update_compras_produtos():
    with st.form(key='update_compras_produtos'):
        col1, col2 = st.columns(2)
        with col1:
            st.write('**ID do Item da Compra**')
            input_id_compra_produto = st.selectbox(
                label='ID', 
                placeholder='Selecione o ID do item da compra', 
                options=[row[0] for row in consulta_compras_produtos()], 
                index=None, 
                label_visibility='collapsed'
            )
        with col2:
            st.write('**ID do Produto**')
            input_produto_ID_produto = st.selectbox(
                label='ID Produto',
                placeholder='Selecione o ID do produto',
                options=[row[0] for row in consulta_produtos()], 
                index=None,
                label_visibility='collapsed'
            )
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Preço Unitário (R$)**')
            input_preco_unitario_produto_compra = st.number_input(label='Preço Unitário', format='%.2f', step=float(1), label_visibility='collapsed')
        with col2:
            st.write('**Quantidade**')
            input_quantidade_produto_compra = st.text_input(label='Quantidade', label_visibility='collapsed')
        input_botao_alterar_item_compra = st.form_submit_button('**Atualizar**')
    if input_botao_alterar_item_compra:
        try:
            controllers.update_compras_produtos(
                models.CompraProduto(
                        input_id_compra_produto, 0, input_produto_ID_produto, input_preco_unitario_produto_compra, 
                        input_quantidade_produto_compra
                    )
            )
        except Exception as e:
            st.error(f'Erro durante update: {e}')
    else:
        pass
    

#vendas
def update_vendas():
    with st.form(key='update_vendas'):
        opcoes_pagamento = ['Crédito', 'Débito', 'Dinheiro', 'PIX']
        col1, col2 = st.columns(2)
        with col1:
            st.write('**ID da Venda**')
            input_id_venda = st.selectbox(
                        label='ID Venda', 
                        placeholder='Selecione o ID da venda', 
                        options=[row[0] for row in consulta_vendas()], 
                        index=None,
                        label_visibility='collapsed'
                    )
        with col2:
            st.write('**ID do Cliente**')
            input_cliente_id_cliente = st.selectbox(
                        label='ID Cliente', 
                        placeholder='Selecione o ID do cliente', 
                        options=[row[0] for row in consulta_clientes()],
                        index=None,
                        label_visibility='collapsed'
                    )
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Endereço**')
            input_endereco_entrega_venda = st.text_input(label='Endereço', max_chars=100, label_visibility='collapsed')
        with col2:
            st.write('**Bairro**')
            input_bairro_entrega_venda = st.text_input(label='Bairro', max_chars=50, label_visibility='collapsed')
        st.write('**Observações**')
        input_observacoes_venda = st.text_input(label='Observações', max_chars=255, label_visibility='collapsed')
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Situação do Pagamento**')
            input_situacao_pagamento_venda = st.selectbox(label='Situação do Pagamento', options=['Não realizada', 'Realizado'], placeholder='Selecione a situação do pagamento', index=None, label_visibility='collapsed')
        with col2:
            st.write('**Situação da Entrega**')
            input_situacao_entrega_venda = st.selectbox(label='Situação da Entrega', options=['Não realizada', 'Realizado'], placeholder='Selecione a situação do entrega', index=None, label_visibility='collapsed')
        st.write('**Forma de Pagamento**')
        input_forma_pagamento_venda = st.selectbox(label='Forma de Pagamento', options=opcoes_pagamento, placeholder='Selecione a forma de pagamento', index=None, label_visibility='collapsed')
        input_botao_alterar_venda = st.form_submit_button('**Atualizar**')
    if input_botao_alterar_venda:
        try:
            controllers.update_vendas(
                models.Venda(
                        input_id_venda, 0, input_cliente_id_cliente, input_endereco_entrega_venda, input_bairro_entrega_venda,
                        input_observacoes_venda, 0, input_situacao_pagamento_venda, input_situacao_entrega_venda, 
                        input_forma_pagamento_venda
                    )
            )
        except Exception as e:
            st.error(f'Erro durante update: {e}')
    else:
        pass


#itens de venda
def update_vendas_produtos():
    with st.form(key='update_vendas_produtos'):
        col1, col2 = st.columns(2)
        with col1:
            st.write('**ID do Item de Venda**')
            input_id_venda_produto = st.selectbox(
                    label='ID', 
                    placeholder='Selecione o ID do item da venda', 
                    options=[row[0] for row in consulta_vendas_produtos()], 
                    index=None,
                    label_visibility='collapsed'
                )
        with col2:
            st.write('**ID do Produto**')
            input_produto_ID_produto = st.selectbox(
                label='ID Produto',
                placeholder='Selecione o ID do produto',
                options=[row[0] for row in consulta_produtos()], 
                index=None,
                label_visibility='collapsed'
            )
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Preço Unitário (R$)**')
            input_preco_unitario_produto_venda = st.number_input(label='Preço Unitário', format='%.2f', step=float(1), label_visibility='collapsed')
        with col2:
            st.write('**Quantidade**')
            input_quantidade_produto_venda = st.text_input(label='Quantidade', label_visibility='collapsed')
        input_botao_alterar_item_venda = st.form_submit_button('**Atualizar**')
    if input_botao_alterar_item_venda:
        try:
            controllers.update_vendas_produtos(
                models.VendaProduto(
                        input_id_venda_produto, 0, input_produto_ID_produto, input_preco_unitario_produto_venda, 
                        input_quantidade_produto_venda
                    )
            )
        except Exception as e:
            st.error(f'Erro durante update: {e}')
    else:
        pass


#deletes
#---------------------------------------------------------------

#compras
def delete_compras():
    col1, _ = st.columns(2)
    with col1:
        with st.form(key='delete_compras'):
            st.write('**ID da Compra**')
            input_id_compra = st.selectbox(
                label='ID', 
                placeholder='Selecione o ID da compra', 
                options=[row[0] for row in consulta_compras()], 
                index=None,
                label_visibility='collapsed'

            )
            input_botao_excluir_compra = st.form_submit_button('**Excluír**')
    if input_botao_excluir_compra:
        try:
            controllers.delete_compras(input_id_compra)
        except Exception as e:
            st.error(f'Erro durante exclusão: {e}')
    else:
        pass


#itens de compra
def delete_compras_produtos():
    col1, _ = st.columns(2)
    with col1:
        with st.form(key='delete_compras_produtos'):
            st.write('**ID do Item da Compra**')
            input_id_compra_produto = st.selectbox(
                label='ID', 
                placeholder='Selecione o ID do item da compra', 
                options=[row[0] for row in consulta_compras_produtos()], 
                index=None,
                label_visibility='collapsed'
            )
            input_botao_excluir_item_compra = st.form_submit_button('**Excluír**')
    if input_botao_excluir_item_compra:
        try:
            controllers.delete_compras_produtos(input_id_compra_produto)
        except Exception as e:
            st.error(f'Erro durante exclusão: {e}')
    else:
        pass


#vendas
def delete_vendas():
    col1, _ = st.columns(2)
    with col1:
        with st.form(key='delete_vendas'):
            st.write('**ID da Venda**')
            input_id_venda = st.selectbox(
                label='ID', 
                placeholder='Selecione o ID da venda', 
                options=[row[0] for row in consulta_vendas()], 
                index=None,
                label_visibility='collapsed'
            )
            input_botao_excluir_venda = st.form_submit_button('**Excluír**')
    if input_botao_excluir_venda:
        try:
            controllers.delete_vendas(input_id_venda)
        except Exception as e:
            st.error(f'Erro durante exclusão: {e}')
    else:
        pass


#itens de venda
def delete_vendas_produtos():
    col1, _ = st.columns(2)
    with col1:
        with st.form(key='delete_compras_produtos'):
            st.write('**ID do Item da Venda**')
            input_id_venda_produto = st.selectbox(
                label='ID', 
                placeholder='Selecione o ID do item da venda', 
                options=[row[0] for row in consulta_vendas_produtos()], 
                index=None,
                label_visibility='collapsed'
            )
            input_botao_excluir_item_venda = st.form_submit_button('**Excluír**')
    if input_botao_excluir_item_venda:
        try:
            controllers.delete_vendas_produtos(input_id_venda_produto)
        except Exception as e:
            st.error(f'Erro durante exclusão: {e}')
    else:
        pass


#formatacoes
#---------------------------------------------------------------

#valores
def formata_valor(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'


#graficos
#---------------------------------------------------------------

#evolução de despesas no ano selecionado
def fig_evolucao_despesa(df, data):
    df_compras_custo_mensal = df.sort_values('Data')
    df_compras_custo_mensal['Data'] = df_compras_custo_mensal['Data'].dt.date
    df_compras_custo_mensal = df_compras_custo_mensal.groupby('Data')['Custo (R$)'].sum().reset_index()
    fig = px.line(
        data_frame=df_compras_custo_mensal, 
        x='Data', 
        y='Custo (R$)',
        hover_name='Data',
        labels={'Custo (R$)': 'Despesa (R$)'}
    )
    fig.update_layout(
        title=f'Evolução de Despesas em {data.year}',
        xaxis_title='Data', 
        yaxis_showticklabels=True,
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Data: %{hovertext}<br>Despesa: R$ %{y:.2f}'
    )
    st.plotly_chart(fig)


#despesa por fornecedor no ano selecionado
def fig_despesa_por_fornecedor(df, data):
    df_custo_por_fornecedor = df
    df_custo_por_fornecedor = df_custo_por_fornecedor.groupby('Nome')['Custo (R$)'].sum().reset_index()
    df_custo_por_fornecedor = df_custo_por_fornecedor.sort_values('Custo (R$)', ascending=False).head()
    df_custo_por_fornecedor['Custo (R$)'] = df_custo_por_fornecedor['Custo (R$)'].astype('float64')
    fig = px.bar(
        data_frame=df_custo_por_fornecedor, 
        x='Nome', 
        y='Custo (R$)',
        text=df_custo_por_fornecedor['Custo (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        color='Custo (R$)',
        hover_name='Nome',
        labels={'Custo (R$)': 'Despesa (R$)'}
    )
    fig.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        xaxis_type='category',
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        showlegend=False,
        textposition='outside',
        hovertemplate='Nome: %{hovertext}<br>Custo: R$ %{y:.2f}'
    )
    fig.update_xaxes(
        tickangle=45
    )
    st.plotly_chart(fig)


#evolução da média de custo por produto no ano selecionado
def fig_evolucao_preco_medio_produto_compra(df, data, produtos):
    df_custo_por_produto = df.sort_values('Data')
    df_custo_por_produto['Data'] = df_custo_por_produto['Data'].dt.date
    df_custo_por_produto = df_custo_por_produto.groupby(['Data', 'Nome'])['Preço Unitário (R$)'].median().reset_index().sort_values('Data')
    df_custo_por_produto = df_custo_por_produto[df_custo_por_produto['Nome'].isin(produtos)]
    fig = px.line(
        data_frame=df_custo_por_produto, 
        x='Data', 
        y='Preço Unitário (R$)',
        text=df_custo_por_produto['Preço Unitário (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        hover_name='Nome',
        color='Nome'
    )
    fig.update_layout(
        title=f'Evolução do Preço de Compra Médio Por Produto em {data.year}',
        xaxis_title='Data', 
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Produto: %{hovertext}<br>Preço Unitário (R$): %{y:.2f}<br>Data: %{x}'
    )
    st.plotly_chart(fig)


#evolucao do faturamento no ano selecionado
def fig_evolucao_faturamento(df, data):
    df_vendas_faturamento_mensal = df.sort_values('Data')
    df_vendas_faturamento_mensal['Data'] = df_vendas_faturamento_mensal['Data'].dt.date
    df_vendas_faturamento_mensal = df_vendas_faturamento_mensal[df_vendas_faturamento_mensal['Situação do Pagamento'] == 'Realizado']
    df_vendas_faturamento_mensal = df_vendas_faturamento_mensal.groupby('Data')['Faturamento (R$)'].sum().reset_index()
    fig = px.line(
        data_frame=df_vendas_faturamento_mensal, 
        x='Data', 
        y='Faturamento (R$)',
        hover_name='Data'
    )
    fig.update_layout(
        title=f'Faturamento Mensal em {data.year}',
        xaxis_title='Data',
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Data: %{hovertext}<br>Faturamento: R$ %{y:.2f}'
    )
    st.plotly_chart(fig)
    

#faturamento por cliente no ano selecionado
def fig_faturamento_por_cliente(df, data):
    df_faturamento_por_cliente = df[df['Situação do Pagamento'] == 'Realizado']
    df_faturamento_por_cliente = df_faturamento_por_cliente.groupby('Nome')['Faturamento (R$)'].sum().reset_index()
    df_faturamento_por_cliente = df_faturamento_por_cliente.sort_values('Faturamento (R$)', ascending=False).head()
    df_faturamento_por_cliente['Faturamento (R$)'] = df_faturamento_por_cliente['Faturamento (R$)'].astype('float64')
    fig = px.bar(
        data_frame=df_faturamento_por_cliente, 
        x='Nome', 
        y='Faturamento (R$)',
        text=df_faturamento_por_cliente['Faturamento (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        color='Faturamento (R$)',
        hover_name='Nome'
    )
    fig.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        xaxis_type='category',
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        showlegend=False,
        textposition='outside',
        hovertemplate='Nome: %{hovertext}<br>Faturamento: R$ %{y:.2f}'
    )
    fig.update_xaxes(
        tickangle=45
    )
    st.plotly_chart(fig)
    
#evolução da média de preços por produto no ano selecionad
def fig_evolucao_preco_medio_produto(df, data, produtos):
    df_custo_por_produto = df.sort_values('Data')
    df_custo_por_produto['Data'] = df_custo_por_produto['Data'].dt.date
    df_custo_por_produto = df_custo_por_produto.groupby(['Data', 'Nome'])['Preço Unitário (R$)'].median().reset_index().sort_values('Data')
    df_custo_por_produto = df_custo_por_produto[df_custo_por_produto['Nome'].isin(produtos)]
    fig = px.line(
        data_frame=df_custo_por_produto, 
        x='Data', 
        y='Preço Unitário (R$)',
        text=df_custo_por_produto['Preço Unitário (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        hover_name='Nome',
        color='Nome'
    )
    fig.update_layout(
        title=f'Evolução do Preço Médio Por Produto em {data.year}',
        xaxis_title='Data', 
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Produto: %{hovertext}<br>Preço Unitário (R$): %{y:.2f}<br>Data: %{x}'
    )
    st.plotly_chart(fig)
    

#evolução da média de faturamento por produto no ano selecionado
def fig_evolucao_preco_medio_produto_venda(df, data, produtos):
    df_faturamento_por_produto = df.sort_values('Data')
    df_faturamento_por_produto['Data'] = df_faturamento_por_produto['Data'].dt.date
    df_faturamento_por_produto = df_faturamento_por_produto.groupby(['Data', 'Nome'])['Preço Unitário (R$)'].median().reset_index().sort_values('Data')
    df_faturamento_por_produto = df_faturamento_por_produto[df_faturamento_por_produto['Nome'].isin(produtos)]
    fig = px.line(
        data_frame=df_faturamento_por_produto, 
        x='Data', 
        y='Preço Unitário (R$)',
        text=df_faturamento_por_produto['Preço Unitário (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        hover_name='Nome',
        color='Nome'
    )
    fig.update_layout(
        title=f'Evolução do Preço de Venda Médio Por Produto em {data.year}',
        xaxis_title='Data', 
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Produto: %{hovertext}<br>Preço Unitário (R$): %{y:.2f}<br>Data: %{x}'
    )
    st.plotly_chart(fig)