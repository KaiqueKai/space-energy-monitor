import random

# ==========================================
# SPACE ENERGY MONITOR
# Global Solution - FIAP
# ==========================================

alertas = []


def gerar_dados():
    dados = {
        "temperatura": random.randint(20, 100),
        "energia": random.randint(0, 100),
        "comunicacao": random.choice(["Online", "Offline"]),
        "habitacao": random.choice(
            ["Operacional", "Atenção", "Crítico"]
        ),
        "energia_solar": random.randint(50, 150),
        "consumo": random.randint(40, 120)
    }

    return dados


def verificar_alertas(dados):
    global alertas

    alertas = []

    if dados["temperatura"] > 80:
        alertas.append(
            "Temperatura crítica detectada!"
        )

    if dados["energia"] < 20:
        alertas.append(
            "Energia abaixo de 20%!"
        )

    if dados["comunicacao"] == "Offline":
        alertas.append(
            "Falha de comunicação!"
        )

    if dados["habitacao"] == "Crítico":
        alertas.append(
            "Módulo habitacional em estado crítico!"
        )


def tomada_decisao(dados):
    print("\n===== RESPOSTAS AUTOMÁTICAS =====")

    acao = False

    if dados["temperatura"] > 80:
        print(
            "- Sistema de resfriamento ativado."
        )
        acao = True

    if dados["energia"] < 20:
        print(
            "- Modo economia de energia ativado."
        )
        acao = True

    if dados["comunicacao"] == "Offline":
        print(
            "- Tentativa automática de reconexão."
        )
        acao = True

    if dados["habitacao"] == "Crítico":
        print(
            "- Equipe direcionada para área segura."
        )
        acao = True

    if not acao:
        print(
            "- Nenhuma ação necessária."
        )


def visualizar_modulos(dados):
    print("\n========== DADOS DA MISSÃO ==========")

    print(f"\nTemperatura: {dados['temperatura']} °C")
    print(f"Energia: {dados['energia']} %")
    print(f"Comunicação: {dados['comunicacao']}")
    print(f"Habitação: {dados['habitacao']}")

    print(
        f"Produção Solar: {dados['energia_solar']} kW"
    )

    print(
        f"Consumo Energético: {dados['consumo']} kW"
    )


def mostrar_alertas():
    print("\n========== ALERTAS ==========")

    if len(alertas) == 0:
        print("Nenhum alerta ativo.")
    else:
        for alerta in alertas:
            print(f"- {alerta}")


def relatorio_sustentabilidade(dados):
    print(
        "\n===== RELATÓRIO DE SUSTENTABILIDADE ====="
    )

    eficiencia = (
        dados["energia_solar"]
        / dados["consumo"]
    ) * 100

    print(
        f"Energia Solar Gerada: {dados['energia_solar']} kW"
    )

    print(
        f"Consumo Energético: {dados['consumo']} kW"
    )

    print(
        f"Eficiência Energética: {eficiencia:.1f}%"
    )

    if eficiencia >= 100:
        print(
            "Status: Sistema altamente sustentável."
        )

    elif eficiencia >= 70:
        print(
            "Status: Sistema sustentável."
        )

    else:
        print(
            "Status: Necessita otimização energética."
        )


dados_missao = gerar_dados()

while True:

    print("\n")
    print("=" * 40)
    print("SPACE ENERGY MONITOR")
    print("=" * 40)

    print("1 - Atualizar dados da missão")
    print("2 - Visualizar módulos")
    print("3 - Ver alertas")
    print("4 - Relatório sustentável")
    print("5 - Encerrar missão")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        dados_missao = gerar_dados()

        verificar_alertas(dados_missao)

        print(
            "\nDados atualizados com sucesso!"
        )

        tomada_decisao(dados_missao)

    elif opcao == "2":

        visualizar_modulos(dados_missao)

    elif opcao == "3":

        mostrar_alertas()

    elif opcao == "4":

        relatorio_sustentabilidade(
            dados_missao
        )

    elif opcao == "5":

        print(
            "\nEncerrando missão..."
        )

        print(
            "Sistema finalizado com sucesso."
        )

        break

    else:

        print(
            "\nOpção inválida."
        )