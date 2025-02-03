import yfinance as yf
import pandas as pd
import pandas_ta as ta
import tkinter as tk
from tkinter import messagebox

# Função para buscar dados do Bitcoin
def buscar_dados(ticker: str):
    try:
        # Obtém os dados históricos do Bitcoin
        dados = yf.download(ticker, period="5d", interval="5m", progress=False)
        if dados.empty:
            messagebox.showerror("Erro", f"Nenhum dado retornado para {ticker}. Verifique o código do ativo.")
        return dados
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar dados: {str(e)}")
        return pd.DataFrame()

# Função para analisar os dados
def analisar_dados(dados):
    if dados.empty or len(dados) < 20:
        return "Dados insuficientes para análise."

    # Calcula as EMAs
    dados["EMA5"] = ta.ema(dados["Close"], length=5)
    dados["EMA20"] = ta.ema(dados["Close"], length=20)

    # Pega os valores do último período
    ultima_linha = dados.iloc[-1]
    ema5 = ultima_linha["EMA5"]
    ema20 = ultima_linha["EMA20"]

    if pd.isna(ema5) or pd.isna(ema20):
        return "Não foi possível calcular as EMAs."

    return "Comprar" if ema5 > ema20 else "Vender"

# Função para realizar a análise e exibir o resultado
def executar_analise():
    ticker = entrada_ticker.get().strip().upper()
    if not ticker:
        messagebox.showwarning("Aviso", "Por favor, insira o código do ativo.")
        return

    # Defina o ticker como 'BTC-USD' para o Bitcoin
    if ticker == 'BTC':
        ticker = 'BTC-USD'
    
    dados = buscar_dados(ticker)
    if not dados.empty:
        resultado = analisar_dados(dados)
        texto_resultado.set(f"Sinal: {resultado}")

# Cria a interface principal
app = tk.Tk()
app.title("Análise de Bitcoin")
app.geometry("300x200")

# Título
titulo = tk.Label(app, text="Analisador de Bitcoin", font=("Arial", 14))
titulo.pack(pady=10)

# Resultado
texto_resultado = tk.StringVar()
resultado_label = tk.Label(app, textvariable=texto_resultado, font=("Arial", 12), fg="blue")
resultado_label.pack(pady=5)

# Campo de entrada
entrada_ticker = tk.Entry(app, font=("Arial", 12))
entrada_ticker.pack(pady=5)

# Botão para executar a análise
botao_analise = tk.Button(app, text="Analisar", command=executar_analise, font=("Arial", 12))
botao_analise.pack(pady=10)

# Executa a interface
tk.mainloop()
