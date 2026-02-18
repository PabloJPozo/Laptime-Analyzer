#Laptime analyzer

def leer_tiempos():
    try:
        with open("tiempos.txt", "r") as archivo:
            tiempos = [linea.strip() for linea in archivo.readlines()]
    except FileNotFoundError:
        tiempos = []
    return tiempos


def convertir_a_segundos(tiempo_str):
    minutos, resto = tiempo_str.split(":")
    segundos = float(resto)
    total = int(minutos) * 60 + segundos
    return total

def convertir_a_minutos(segundos_totales):
    minutos = int(segundos_totales // 60)
    segundos = segundos_totales % 60
    return f"{minutos}:{segundos:06.3f}"


def main():
    tiempos = leer_tiempos()

    if not tiempos :
        print("No hay tiempos registrados en la lista")
        return

    print("\nLos tiempos son: ", tiempos)
    
    tiempos_en_seg = [convertir_a_segundos(t) for t in tiempos]
    print("En segundos: ", tiempos_en_seg)   

    vuelta_mas_rapida = min(tiempos_en_seg)
    print("La vuelta mas rapida es: ", convertir_a_minutos(vuelta_mas_rapida))

    promedio_vueltas = sum(tiempos_en_seg) / len(tiempos_en_seg)
    print("El promedio de es: ", convertir_a_minutos(promedio_vueltas))

    deltas = []

    for i in range (1, len(tiempos_en_seg)):
        deltas.append(tiempos_en_seg[i] - tiempos_en_seg[i - 1])

    print("Delta:")
    for d in deltas:
        print("%.3f" % d)


if __name__ == "__main__":
    main()