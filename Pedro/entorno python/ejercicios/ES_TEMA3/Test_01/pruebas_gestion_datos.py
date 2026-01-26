import unittest

from gestion_datos import (
    personas,
    eventos,
    agregar_persona,
    obtener_persona,
    buscar_persona,
    agregar_evento,
    agregar_participante,
    eventos_comunes,
    evento_mayor
)

class TestGestionDatos(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada test
        personas.clear()
        eventos.clear()

    def test_agregar_persona(self):
        resultado = agregar_persona(personas, "Sergio", "Guerrero", "+34111222333")
        self.assertTrue(resultado)
        self.assertIn(1111, personas)
        self.assertEqual(
            personas[1111],
            ("Sergio", "Guerrero", "+34111222333"),
        )

    def test_obtener_persona(self):
        personas[1111] = ("Sergio", "Guerrero", "+34111222333")
        persona = obtener_persona(personas, 1111)
        self.assertEqual(persona, ("Sergio", "Guerrero", "+34111222333"))
        self.assertIsNone(obtener_persona(personas, 9999))

    def test_buscar_persona(self):
        personas[1111] = ("Sergio", "Guerrero", "+34111222333")
        self.assertEqual(
            buscar_persona(personas, "Sergio", "Guerrero"),
            1111,
        )
        self.assertIsNone(buscar_persona(personas, "Ana", "López"))

    def test_eventos_y_participantes(self):
        agregar_evento(eventos, "Cumpleaños")
        agregar_evento(eventos, "Concierto")
        agregar_persona(personas, "Sergio", "Guerrero", "+34111222333")
        agregar_persona(personas, "Ana", "López", "+34222333444")

        agregar_participante(eventos, personas, "Cumpleaños", 1111)
        agregar_participante(eventos, personas, "Cumpleaños", 1112)
        agregar_participante(eventos, personas, "Concierto", 1111)

        self.assertEqual(evento_mayor(eventos), ("Cumpleaños", 2))
        self.assertEqual(
            set(eventos_comunes(eventos, [1111])),
            {"Cumpleaños", "Concierto"},
        )
        self.assertEqual(
            eventos_comunes(eventos, [1111, 1112]),
            ("Cumpleaños",),
        )

if __name__ == "__main__":
    unittest.main()

