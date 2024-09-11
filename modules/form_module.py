import streamlit as st
import pandas as pd
import controllers.controllers as controllers
import models.models as models
import modules.utils_module as utils
import warnings
warnings.filterwarnings('ignore')


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
        input_botao_inserir_cliente = st.form_submit_button('**Inserir**', type='primary')
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
        input_botao_inserir_fornecedor = st.form_submit_button('**Inserir**', type='primary')
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
        input_botao_inserir_produto = st.form_submit_button('**Inserir**', type='primary')
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
        input_fornecedor_id_fornecedor = st.selectbox(label='ID Fornecedor', options=[row[0] for row in utils.consulta_fornecedores()], placeholder='Selecione o ID do cliente', index=None, label_visibility='collapsed')
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
                    options=[row[0] for row in utils.consulta_produtos()],
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
        input_botao_inserir_compra = st.form_submit_button('**Inserir**', type='primary')
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
        input_cliente_id_cliente = st.selectbox(label='ID Cliente', options=[row[0] for row in utils.consulta_clientes()], placeholder='Selecione o ID cliente', index=None, label_visibility= 'collapsed')
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
                    options=[row[0] for row in utils.consulta_produtos()],
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
        input_botao_inserir_venda = st.form_submit_button('**Inserir**', type='primary')
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
    with st.form(key='update_clientes_busca'):
        #formulário
        cliente_selecionado = None
        col1, _ = st.columns([.3, .7])
        with col1:
            st.write('**ID do Cliente**')
            input_id_cliente = st.selectbox(
                label='ID Cliente', options=[row[0] for row in utils.consulta_clientes()], 
                placeholder='Selecione o ID do cliente', index=None, label_visibility='collapsed'
            )
        if input_id_cliente:
            cliente_selecionado = controllers.select_cliente_selecionado(input_id_cliente)
        st.form_submit_button('**Buscar**', type='primary')
    with st.form(key='update_clientes_dados'):    
        if cliente_selecionado:
            st.write('**Nome**')
            input_nome_cliente = st.text_input(
                label='Nome', value=cliente_selecionado.nome_cliente, max_chars=100, label_visibility='collapsed'
            )
            col1, col2 = st.columns([.6, .4])
            with col1:
                st.write('**CPF/CNPJ**')
                input_cpf_cnpj_cliente = st.text_input(
                    label='CPF/CNPJ', value=cliente_selecionado.cpf_cnpj_cliente, max_chars=18, label_visibility='collapsed'
                )
            with col2:
                st.write('**Telefone**')
                input_telefone_cliente = st.text_input(
                    label='Telefone', value=cliente_selecionado.telefone_cliente, max_chars=15, label_visibility='collapsed'
                )
            st.write('**Tipo**')
            input_tipo_cliente = st.selectbox(
                label='Tipo', options=['Pessoa Física', 'Pessoa Jurídica'], 
                index=[0 if cliente_selecionado.tipo_cliente == 'Pessoa Física' else 1][0], 
                placeholder='Selecione o tipo de cliente', label_visibility='collapsed'
            )
            col1, col2 = st.columns([.6, .4])
            with col1:
                st.write('**Endereço**')
                input_endereco_cliente = st.text_input(
                    label='Endereço', value=cliente_selecionado.endereco_cliente, max_chars=100, label_visibility='collapsed'
                )
            with col2:
                st.write('**Bairro**')
                input_bairro_cliente = st.text_input(
                    label='Bairro', value=cliente_selecionado.bairro_cliente, max_chars=50, label_visibility='collapsed'
                )
            st.write('**Referência**')
            input_referencia_cliente = st.text_input(
                label='Referência', value=cliente_selecionado.referencia_cliente, max_chars=255, label_visibility='collapsed'
            )
            st.write('**Situação**')
            input_situacao_cliente = st.selectbox(
                label='Situação', options=['Adimplente', 'Inadimplente'], 
                index=[0 if cliente_selecionado.situacao_cliente == 'Adimplente' else 1][0], 
                placeholder='Selecione a situação do cliente', label_visibility='collapsed'
            )
            input_botao_alterar_cliente = st.form_submit_button('**Atualizar**', type='primary')
            if input_botao_alterar_cliente:
                try:
                    controllers.update_clientes(
                        models.Cliente(
                            input_id_cliente, input_nome_cliente, input_tipo_cliente, input_cpf_cnpj_cliente, 
                            input_endereco_cliente, input_bairro_cliente, input_telefone_cliente, input_referencia_cliente, 
                            input_situacao_cliente
                        )
                    )
                except Exception as e:
                    st.error(f'Erro durante update: {e}')
        else:
            pass


#fornecedores
def update_fornecedores():
    with st.form(key='update_fornedores_busca'):
        #formulário
        fornecedor_selecionado = None
        col1, _ = st.columns([.3, .7])
        with col1:
            st.write('**ID do Fornecedor**')
            input_id_fornecedor = st.selectbox(
                label='ID Fornecedor', options=[row[0] for row in utils.consulta_fornecedores()], 
                placeholder='Selecione o ID do fornecedor', index=None, label_visibility='collapsed'
            )
        if input_id_fornecedor:
            fornecedor_selecionado = controllers.select_fornecedor_selecionado(input_id_fornecedor)
        st.form_submit_button('**Buscar**', type='primary')
    with st.form(key='update_fornedores_dados'):
        if fornecedor_selecionado:
            st.write('**Nome**')
            input_nome_fornecedor = st.text_input(
                label='Nome', value=fornecedor_selecionado.nome_fornecedor, max_chars=100, label_visibility='collapsed'
            )
            col1, col2 = st.columns([.6, .4])
            with col1:
                st.write('**CNPJ**')
                input_cnpj_fornecedor = st.text_input(
                    label='CNPJ', value=fornecedor_selecionado.cnpj_fornecedor, max_chars=18, label_visibility='collapsed'
                )
            with col2:
                st.write('**Telefone**')
                input_telefone_fornecedor = st.text_input(
                    label='Telefone', value=fornecedor_selecionado.telefone_fornecedor, max_chars=15, label_visibility='collapsed'
                )
            col1, col2 = st.columns([.6, .4])
            with col1:
                st.write('**Endereço**')
                input_endereco_fornecedor = st.text_input(
                    label='Endereço', value=fornecedor_selecionado.endereco_fornecedor, max_chars=100, label_visibility='collapsed'
                )
            with col2:
                st.write('**Bairro**')
                input_bairro_fornecedor = st.text_input(
                    label='Bairro', value=fornecedor_selecionado.bairro_fornecedor, max_chars=50, label_visibility='collapsed'
                )
            input_botao_alterar_fornecedor = st.form_submit_button('**Atualizar**', type='primary')
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
    with st.form(key='update_produtos_busca'):
        opcoes_unidade_medida = ['un', 'm', 'm²', 'm³', 'l', 'kg', 'lata', 'caminhão']
        #formulário
        produto_selecionado = None
        col1, _ = st.columns([.3, .7])
        with col1:
            st.write('**ID do Produto**')
            input_id_produto = st.selectbox(
                label='ID Produto', options=[row[0] for row in utils.consulta_produtos()], 
                placeholder='Selecione o ID do produto', index=None, label_visibility='collapsed'
            )
        if input_id_produto:
            produto_selecionado = controllers.select_produto_selecionado(input_id_produto)
        st.form_submit_button('**Buscar**', type='primary')
    with st.form(key='update_produtos_dados'):    
        if produto_selecionado:
            st.write('**Nome**')
            input_nome_produto = st.text_input(
                label='Nome', value=produto_selecionado.nome_produto, max_chars=255, label_visibility='collapsed'
            )
            col1, _ = st.columns([.3, .7])
            with col1:
                st.write('**Unidade de Medida**')
                input_unidade_medida_produto = st.selectbox(
                    label='Unidade de Medida', options=opcoes_unidade_medida, 
                    index=opcoes_unidade_medida.index(produto_selecionado.unidade_medida_produto), 
                    placeholder='Selecione a unidade de medida', label_visibility='collapsed'
                )
            input_botao_alterar_produto = st.form_submit_button('**Atualizar**', type='primary')
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
    with st.form(key='update_compras_busca'):
        opcoes_pagamento = ['Crédito', 'Débito', 'Dinheiro', 'PIX']
        #formulário
        compra_selecionada = None
        col1, _ = st.columns([.3, .7])
        with col1:
            st.write('**ID da Compra**')
            input_id_compra = st.selectbox(
                label='ID Compra', 
                placeholder='Selecione o ID da compra', 
                options=[row[0] for row in utils.consulta_compras()],
                index=None,
                label_visibility='collapsed'
            )
        if input_id_compra:
            compra_selecionada = controllers.select_compra_selecionada(input_id_compra)
        st.form_submit_button('**Buscar**', type='primary')
    with st.form(key='update_compras_dados'):    
        if compra_selecionada:
            st.write('**ID do Fornecedor**')
            input_fornecedor_id_fornecedor = st.selectbox(
                label='ID Fornecedor', 
                placeholder='Selecione o ID do fornecedor',
                options=[row[0] for row in utils.consulta_fornecedores()],
                index=[row[0] for row in utils.consulta_fornecedores()].index(compra_selecionada.fornecedor_id_fornecedor),
                label_visibility='collapsed'
            )
            col1, col2 = st.columns(2)
            with col1:
                st.write('**Situação do Pagamento**')
                input_situacao_pagamento_compra = st.selectbox(
                    label='Situação do Pagamento', 
                    options=['Não realizada', 'Realizado'], 
                    index=[0 if compra_selecionada.situacao_pagamento_compra == 'Não realizada' else 1][0], 
                    placeholder='Selecione a situação da pagamento', label_visibility='collapsed'
                )
            with col2:
                st.write('**Situação da Entrega**')
                input_situacao_entrega_compra = st.selectbox(
                    label='Situação da Entrega', 
                    options=['Não realizada', 'Realizado'], 
                    index=[0 if compra_selecionada.situacao_entrega_compra == 'Não realizada' else 1][0], 
                    placeholder='Selecione a situação da entrega', label_visibility='collapsed'
                )
            st.write('**Forma de Pagamento**')
            input_forma_pagamento_compra = st.selectbox(
                label='Forma de Pagamento', 
                options=opcoes_pagamento, 
                index=opcoes_pagamento.index(compra_selecionada.forma_pagamento_compra), 
                placeholder='Selecione a forma de pagamento', label_visibility='collapsed'
            )
            input_botao_alterar_compra = st.form_submit_button('**Atualizar**', type='primary')
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
    with st.form(key='update_compras_produtos_busca'):
        #formulário
        compra_produto_selecionado = None
        col1, _ = st.columns([.3, .7])
        with col1:
            st.write('**ID do Item da Compra**')
            input_id_compra_produto = st.selectbox(
                label='ID', 
                placeholder='Selecione o ID do item da compra', 
                options=[row[0] for row in utils.consulta_compras_produtos()], 
                index=None, 
                label_visibility='collapsed'
            )
        if input_id_compra_produto:
            compra_produto_selecionado = controllers.select_compras_produtos_selecionado(input_id_compra_produto)
        st.form_submit_button('**Buscar**', type='primary')
    with st.form(key='update_compras_produtos_dados'):
        if compra_produto_selecionado:
            st.write('**ID do Produto**')
            input_produto_ID_produto = st.selectbox(
                label='ID Produto',
                placeholder='Selecione o ID do produto',
                options=[row[0] for row in utils.consulta_produtos()], 
                index=[row[0] for row in utils.consulta_produtos()].index(compra_produto_selecionado.produto_id_produto),
                label_visibility='collapsed'
            )
            col1, col2 = st.columns(2)
            with col1:
                st.write('**Preço Unitário (R$)**')
                input_preco_unitario_produto_compra = st.number_input(
                    label='Preço Unitário (R$)', 
                    format='%.2f', 
                    step=float(1),
                    value=float(compra_produto_selecionado.preco_unitario_produto_compra),
                    label_visibility='collapsed'
                )
            with col2:
                st.write('**Quantidade**')
                input_quantidade_produto_compra = st.text_input(
                    label='Quantidade', 
                    value=int(compra_produto_selecionado.quantidade_produto_compra),
                    label_visibility='collapsed'
                )
            input_botao_alterar_item_compra = st.form_submit_button('**Atualizar**', type='primary')
            if input_botao_alterar_item_compra:
                try:
                    controllers.update_compras_produtos(
                        models.CompraProduto(
                            input_id_compra_produto, 0, input_produto_ID_produto, 
                            input_preco_unitario_produto_compra, input_quantidade_produto_compra
                        )
                    )
                except Exception as e:
                    st.error(f'Erro durante update: {e}')
        else:
            pass
        
#vendas
def update_vendas():
    with st.form(key='update_vendas_busca'):
        opcoes_pagamento = ['Crédito', 'Débito', 'Dinheiro', 'PIX']
        #formulário
        venda_selecionada = None
        col1, _ = st.columns([.3, .7])
        with col1:
            st.write('**ID da Venda**')
            input_id_venda = st.selectbox(
                label='ID Venda', 
                placeholder='Selecione o ID da venda', 
                options=[row[0] for row in utils.consulta_vendas()], 
                index=None,
                label_visibility='collapsed'
            )
        if input_id_venda:
            venda_selecionada = controllers.select_venda_selecionada(input_id_venda)
        st.form_submit_button('**Buscar**', type='primary')
    with st.form(key='update_vendas_dados'):    
        if venda_selecionada:
            st.write('**ID do Cliente**')
            input_cliente_id_cliente = st.selectbox(
                label='ID Cliente', 
                placeholder='Selecione o ID do cliente', 
                options=[row[0] for row in utils.consulta_clientes()],
                index=[row[0] for row in utils.consulta_clientes()].index(venda_selecionada.cliente_id_cliente),
                label_visibility='collapsed'
            )
            col1, col2 = st.columns([.6, .4])
            with col1:
                st.write('**Endereço**')
                input_endereco_entrega_venda = st.text_input(
                    label='Endereço', 
                    value=venda_selecionada.endereco_entrega_venda, 
                    max_chars=100, 
                    label_visibility='collapsed'
                )
            with col2:
                st.write('**Bairro**')
                input_bairro_entrega_venda = st.text_input(
                    label='Bairro', 
                    value=venda_selecionada.bairro_entrega_venda, 
                    max_chars=50, 
                    label_visibility='collapsed'
                )
            st.write('**Observações**')
            input_observacoes_venda = st.text_input(
                label='Observações', 
                value=venda_selecionada.observacoes_venda, 
                max_chars=255, 
                label_visibility='collapsed'
            )
            col1, col2 = st.columns(2)
            with col1:
                st.write('**Situação do Pagamento**')
                input_situacao_pagamento_venda = st.selectbox(
                    label='Situação do Pagamento', 
                    options=['Não realizada', 'Realizado'], 
                    index=[0 if venda_selecionada.situacao_pagamento_venda == 'Não realizada' else 1][0], 
                    placeholder='Selecione a situação do pagamento', 
                    label_visibility='collapsed'
                )
            with col2:
                st.write('**Situação da Entrega**')
                input_situacao_entrega_venda = st.selectbox(
                    label='Situação da Entrega', 
                    options=['Não realizada', 'Realizado'], 
                    index=[0 if venda_selecionada.situacao_entrega_venda == 'Não realizada' else 1][0], 
                    placeholder='Selecione a situação do entrega', 
                    label_visibility='collapsed'
                )
            st.write('**Forma de Pagamento**')
            input_forma_pagamento_venda = st.selectbox(
                label='Forma de Pagamento', 
                options=opcoes_pagamento, 
                index=opcoes_pagamento.index(venda_selecionada.forma_pagamento_venda), 
                placeholder='Selecione a forma de pagamento', 
                label_visibility='collapsed'
            )
            input_botao_alterar_venda = st.form_submit_button('**Atualizar**', type='primary')
            if input_botao_alterar_venda:
                try:
                    controllers.update_vendas(
                        models.Venda(
                            input_id_venda, 0, input_cliente_id_cliente, 
                            input_endereco_entrega_venda, input_bairro_entrega_venda,
                            input_observacoes_venda, 0, 
                            input_situacao_pagamento_venda, input_situacao_entrega_venda, 
                            input_forma_pagamento_venda
                        )
                    )
                except Exception as e:
                    st.error(f'Erro durante update: {e}')
        else:
            pass
        

#itens de venda
def update_vendas_produtos():
    with st.form(key='update_vendas_produtos_busca'):
        #formulário
        venda_produto_selecionado = None
        col1, _ = st.columns([.3, .7])
        with col1:
            st.write('**ID do Item de Venda**')
            input_id_venda_produto = st.selectbox(
                label='ID', 
                placeholder='Selecione o ID do item da venda', 
                options=[row[0] for row in utils.consulta_vendas_produtos()], 
                index=None,
                label_visibility='collapsed'
            )
            if input_id_venda_produto:
                venda_produto_selecionado = controllers.select_vendas_produtos_selecionado(input_id_venda_produto)
        st.form_submit_button('**Buscar**', type='primary')
    with st.form(key='update_vendas_produtos_dados'):    
        if venda_produto_selecionado:
            st.write('**ID do Produto**')
            input_produto_ID_produto = st.selectbox(
                label='ID Produto',
                placeholder='Selecione o ID do produto',
                options=[row[0] for row in utils.consulta_produtos()], 
                index=[row[0] for row in utils.consulta_produtos()].index(venda_produto_selecionado.produto_id_produto),
                label_visibility='collapsed'
            )
            col1, col2 = st.columns(2)
            with col1:
                st.write('**Preço Unitário (R$)**')
                input_preco_unitario_produto_venda = st.number_input(
                    label='Preço Unitário', 
                    format='%.2f', 
                    step=float(1), 
                    value=float(venda_produto_selecionado.preco_unitario_produto_venda),
                    label_visibility='collapsed'
                )
            with col2:
                st.write('**Quantidade**')
                input_quantidade_produto_venda = st.text_input(
                    label='Quantidade', 
                    value=int(venda_produto_selecionado.quantidade_produto_venda),
                    label_visibility='collapsed'
                )
            input_botao_alterar_item_venda = st.form_submit_button('**Atualizar**', type='primary')
            if input_botao_alterar_item_venda:
                try:
                    controllers.update_vendas_produtos(
                        models.VendaProduto(
                            input_id_venda_produto, 0, input_produto_ID_produto, 
                            input_preco_unitario_produto_venda, input_quantidade_produto_venda
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
                options=[row[0] for row in utils.consulta_compras()], 
                index=None,
                label_visibility='collapsed'

            )
            input_botao_excluir_compra = st.form_submit_button('**Excluír**', type='primary')
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
                options=[row[0] for row in utils.consulta_compras_produtos()], 
                index=None,
                label_visibility='collapsed'
            )
            input_botao_excluir_item_compra = st.form_submit_button('**Excluír**', type='primary')
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
                options=[row[0] for row in utils.consulta_vendas()], 
                index=None,
                label_visibility='collapsed'
            )
            input_botao_excluir_venda = st.form_submit_button('**Excluír**', type='primary')
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
                options=[row[0] for row in utils.consulta_vendas_produtos()], 
                index=None,
                label_visibility='collapsed'
            )
            input_botao_excluir_item_venda = st.form_submit_button('**Excluír**', type='primary')
    if input_botao_excluir_item_venda:
        try:
            controllers.delete_vendas_produtos(input_id_venda_produto)
        except Exception as e:
            st.error(f'Erro durante exclusão: {e}')
    else:
        pass