#  ADC Signal Conditioning — Raspberry Pi Pico 2 W

Práctica de lectura y acondicionamiento de una señal analógica utilizando el ADC de la **Raspberry Pi Pico 2 W** con MicroPython.

##  Objetivo

Leer una señal analógica mediante el ADC, aplicar un filtro de promedio móvil y clasificar el nivel de la señal en tres estados:

- 🟢 `NORMAL`
- 🟡 `WARNING`
- 🔴 `ALARM`

El estado se representa mediante tres LEDs conectados a la Raspberry Pi Pico 2 W.

---

##  ADC y `read_u16()`

Un **ADC (Analog-to-Digital Converter)** convierte una señal analógica, como el voltaje proveniente de un potenciómetro o sensor, en un valor digital que puede procesar el microcontrolador.

En MicroPython se utiliza:

```python
raw = sensor.read_u16()
```

`read_u16()` devuelve la lectura del ADC como un valor entre:

```text
0 ─────────────── 65535
0 V                3.3 V
```

Posteriormente, el programa convierte esta lectura a voltaje y porcentaje:

```python
voltaje = promedio * 3.3 / 65535
porcentaje = promedio * 100 / 65535
```

---

##  Circuito utilizado

| Componente | Pin |
|---|---|
| Entrada analógica / sensor | GP26 / ADC0 |
| LED verde | GP13 |
| LED amarillo | GP14 |
| LED rojo | GP15 |

El sensor entrega una señal analógica a **GP26**, mientras que los LEDs muestran visualmente el estado detectado.

---

##  Filtro

Para reducir variaciones rápidas o ruido en la lectura del ADC se utiliza un **promedio móvil de 10 muestras**.

Cada nueva lectura se almacena en una lista:

```python
lecturas.append(raw)
```

Cuando existen más de 10 muestras, se elimina la más antigua:

```python
if len(lecturas) > N:
    lecturas.pop(0)
```

Finalmente se obtiene el promedio:

```python
promedio = sum(lecturas) / len(lecturas)
```

De esta manera, el estado del sistema depende de una señal filtrada y no de una sola lectura instantánea.

---

## 🚦 Umbrales

Se definieron los siguientes niveles:

| Porcentaje | Estado | LED |
|---:|---|---|
| `< 50%` | `NORMAL` | 🟢 Verde |
| `50% – 74.9%` | `WARNING` | 🟡 Amarillo |
| `≥ 75%` | `ALARM` | 🔴 Rojo |

Los umbrales utilizados son:

```python
WARNING = 50
ALARM = 75
```

---

##  Tabla de pruebas

| Prueba | Entrada aproximada | Resultado esperado | LED |
|---|---:|---|---|
| 1 | 25% | `NORMAL` | 🟢 |
| 2 | 49% | `NORMAL` | 🟢 |
| 3 | 50% | `WARNING` | 🟡 |
| 4 | 65% | `WARNING` | 🟡 |
| 5 | 75% | `ALARM` | 🔴 |
| 6 | 100% | `ALARM` | 🔴 |

---

##  Ejecución

Con la Raspberry Pi Pico 2 W conectada:

```bash
mpremote run main.py
```

El programa muestra continuamente la lectura del ADC, voltaje, porcentaje y estado detectado.

```text
Raw: 32768 | Voltaje: 1.65 | Porcentaje: 50.0 | Estado: WARNING
```
