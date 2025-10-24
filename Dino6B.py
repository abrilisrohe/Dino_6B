# 🦕 Biblioteca de dinosaurios

# Lista prellenada de dinosaurios con su información
# Estructura: Nombre, Alimentación, Tamaño, Periodo, Características

dinosaurios = [
    ("Tiranosaurio Rex", "Carnivoro", "12 metros", "Cretacico", "Tenia brazos muy cortos pero mandibulas poderosas"),
    ("Triceratops", "Herbivoro", "9 metros", "Cretacico", "Tenia 3 cuernos y un gran volante oseo"),
    ("Velociraptor", "Carnivoro", "2 metros", "Cretacico", "Tenia una garra en forma de hoz en cada pata"),
    ("Brachiosaurus", "Herbivoro", "9 metros", "Jurasico", "Tenia un cuello muy largo para alcanzar hojas altas"),
    ("Stegosaurus", "Herbivoro", "9 metros", "Jurasico", "Tenia placas en la espalda y puas en la cola"),
    ("Spinosaurus", "Carnivoro", "15 metros", "Cretacico", "Tenia una vela en la espalda y era semiacuatico"),
    ("Ankylosaurus", "Herbivoro", "8 metros", "Cretacico", "Estaba acorazado y tenia una maza en la cola"),
    ("Pteranodon", "Carnivoro", "7 metros (envergadura)", "Cretacico", "Era un reptil volador, pero no era un dinosaurio"),
    ("Diplodocus", "Herbivoro", "10 metros", "Jurasico", "Uno de los dinosaurios mas largos que existieron"),
    ("Parasaurolophus", "Herbivoro", "10 metros", "Cretacico", "Tenia una cresta hueca para hacer sonidos"),
]


print("=" * 60)
print("🦖 Bienvenidos a la biblioteca de dinosaurios 🦕")
print("=" * 60)
print("Pregunta por cualquier dinosaurio y te dare su informacion.")
print("Escribe 'lista' para ver todos los dinosaurios disponibles.")
print("Escribe 'salir' para terminar.\n")


while True:
    consulta = input("¿Que dinosaurio quieres consultar? ").strip().lower()

    if consulta == "salir":
        print("😎 ¡Hasta luego explorador de dinosaurios!")
        break

    if consulta == "lista":
        print("\n📋 Dinosaurios disponibles")
        for i, (nombre, _, _, _, _) in enumerate(dinosaurios, start=1):
            print(f"{i}. {nombre}")
        print()
        continue

    encontrado = False
    for nombre, dieta, tamano, periodo, dato_curioso in dinosaurios:
        if consulta in nombre.lower():
            print("\n" + "=" * 60)
            print(f"🦕 {nombre}")
            print("=" * 60)
            print(f"🍖 Dieta: {dieta}")
            print(f"Tamaño: {tamano}")
            print(f"Periodo: {periodo}")
            print(f"Dato curioso: {dato_curioso}")
            print("=" * 60 + "\n")
            encontrado = True
            break

    if not encontrado:
        print(f"❌ No encontre informacion sobre '{consulta}'.")
        print("💡 Intenta escribir 'lista' para ver los dinosaurios disponibles.\n")